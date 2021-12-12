# coding=utf-8
import json
import logging
import socket
import time
from http.client import RemoteDisconnected
from itertools import cycle
from json import JSONDecodeError
from urllib.parse import urlparse

import requests
import requests_unixsocket
import httpx

import certifi
import urllib3
from .exceptions import (
    NoResponse,
    ChainException,
)
from urllib3.connection import HTTPConnection
from urllib3.exceptions import (
    MaxRetryError,
    ReadTimeoutError,
    ProtocolError,
)

logger = logging.getLogger(__name__)


class HttpClient(object):
    """ Http client for handling eosd connections.

    This class serves as an abstraction layer for underlying HTTP requests.

    Args:
      nodes (list): A list of Eos HTTP RPC nodes to connect to.

    .. code-block:: python

       from eosapi.http_client import HttpClient
       rpc = HttpClient(['https://eosnode.com'])

    any call available to that port can be issued using the instance
    via the syntax ``rpc.exec('command', *parameters)``.

    """

    def __init__(self, nodes, _async = False, **kwargs):
        self.api_version = kwargs.get('api_version', 'v1')
        self.max_retries = kwargs.get('max_retries', 2)
        self.json_decode = kwargs.get('json_decode', True)

        if kwargs.get('tcp_keepalive', True):
            socket_options = HTTPConnection.default_socket_options + \
                             [(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1), ]
        else:
            socket_options = HTTPConnection.default_socket_options

        timeout = urllib3.Timeout(
            connect=kwargs.get('connect_timeout', 10),
            read=kwargs.get('timeout', 10))

        self.http = urllib3.poolmanager.PoolManager(
            num_pools=kwargs.get('num_pools', 50),
            maxsize=kwargs.get('maxsize', 10),
            block=kwargs.get('pool_block', False),
            retries=kwargs.get('http_retries', 1),
            timeout=timeout,
            socket_options=socket_options,
            headers={'Content-Type': 'application/json'},
            cert_reqs='CERT_REQUIRED',
            ca_certs=certifi.where())
        '''
            urlopen(method, url, body=None, headers=None, retries=None,
            redirect=True, assert_same_host=True, timeout=<object object>,
            pool_timeout=None, release_conn=None, chunked=False, body_pos=None,
            **response_kw)
        '''
        self.set_nodes(nodes)

        log_level = kwargs.get('log_level', logging.INFO)
        logger.setLevel(log_level)

        self.session_unix = requests_unixsocket.Session()
        self.session = requests.Session()
        self.timeout = 5
        self._async = _async

        if _async:
            self.async_client = httpx.AsyncClient(proxies={})
        else:
            self.async_client = None

    def set_nodes(self, nodes):
        self.nodes_cache = self._nodes(nodes)
        self.nodes = cycle(self.nodes_cache)
        self.node_url = ''
        self.next_node()

    def get_nodes(self):
        return self.nodes_cache

    def add_node(self, url):
        self.nodes_cache.insert(0, url)
        self.set_nodes(self.nodes_cache)

    def next_node(self):
        """ Switch to the next available node.

        This method will change base URL of our requests.
        Use it when the current node goes down to change to a fallback node. """
        self.set_node(next(self.nodes))

    def set_node(self, node_url):
        """ Change current node to provided node URL. """
        self.node_url = node_url

    @property
    def hostname(self):
        return urlparse(self.node_url).hostname

    def rpc_request(self, api, endpoint, body=None):
        if self._async:
            return self.async_exec(api, endpoint, body)
        else:
            return self.sync_exec(api, endpoint, body)

    def sync_exec(self, api, endpoint, body=None):
        """ Execute a method against eosd RPC.

        Warnings:
            This command will auto-retry in case of node failure, as well as handle
            node fail-over, unless we are broadcasting a transaction.
            In latter case, the exception is **re-raised**.
        """
        logger.debug(f'{endpoint} {body}')
        body = self._body(body)
        method = 'POST' if body else 'GET'
        if self.node_url.startswith('unix://'):
            url = "http+{}/{}/{}/{}".format(self.node_url, self.api_version, api, endpoint)
            try:
                if body:
                    r = self.session_unix.post(url, data = body)
                else:
                    r = self.session_unix.get(url)
                if not r.status_code in [200, 202, 201]:
                    raise ChainException(r.text, r.status_code)

                if self.json_decode:
                    return json.loads(r.text)
                else:
                    return r.text

            except Exception as e:
                extra = dict(err=e, url=url, body=body, method=method)
                logger.info('Request error', extra=extra)
                raise e
        else:
            url = "{}/{}/{}/{}".format(self.node_url, self.api_version, api, endpoint)
            try:
                response = self.http.urlopen(method, url, body=body)
            except Exception as e:
                extra = dict(err=e, url=url, body=body, method=method)
                logger.info('Request error', extra=extra)
                raise e
            else:
                ret = self._return(response=response, body=body)
                return ret

    async def async_exec(self, api, endpoint, body=None):
        url = f'{self.node_url}/v1/{api}/{endpoint}'
        if not body:
            r = await self.async_client.get(url)
        else:
            body = self._body(body)
            r = await self.async_client.post(url, data=body)

        result = r.text
        if not r.status_code in [200, 202, 201] or not result:
            raise ChainException(result, r.status_code)

        ret = json.loads(r.text)
        if 'error' in ret:
            raise ChainException(ret, r.status_code)
        return ret

    def _return(self, response=None, body=None):
        """ Process the response status code and body (json).

        Note:
            If re_raise flag is set, this method will raise an
            exception instead of returning None.

        Exceptions:
            NoResponse on no response.
            ChainException on non-200 response.

        Returns:
            Parsed response body.
        """

        if not response:
            raise NoResponse('eosd nodes have failed to respond, all retries exhausted.')
        result = response.data.decode('cp437')
        if not response.status in [200, 202, 201] or not result:
            extra = dict(result=result, response=response, request_body=body)
            logger.info('non ok response: %s',
                        response.status,
                        extra=extra)
            try:
                result = json.loads(result)
            except JSONDecodeError as e:
                pass
            raise ChainException(result, response.status)
        try:
            if self.json_decode:
                result = json.loads(result)
                if 'error' in result:
                    raise ChainException(result, response.status)
        except JSONDecodeError as e:
            extra = dict(response=response, request_body=body, err=e)
            logger.info('failed to parse response', extra=extra)
        return result

    @staticmethod
    def _body(body):
        if type(body) not in [str, dict, list, type(None)]:
            raise ValueError(
                'Request body is of an invalid type %s' % type(body))
        if type(body) in [dict, list]:
            return json.dumps(body)
        return body

    @staticmethod
    def _nodes(nodes):
        if type(nodes) == str:
            nodes = nodes.split(',')
        return [x.rstrip('/') for x in nodes]


if __name__ == '__main__':
    unix_socket = 'unix://%2FUsers%2Fnewworld%2Fdev%2Fpyeos%2Fbuild%2Fprograms%2Fdata-dir%2Fpyeos.sock'
    h = HttpClient([unix_socket, "http://localhost:8888", "http://localhost:8899"])
    print(h.exec('chain', 'get_block', {"block_num_or_id": 1}))
    print(h.exec('chain', 'get_info'))
    # h.exec('get_block', '{"block_num_or_id":5}')
