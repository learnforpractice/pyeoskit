# coding=utf-8
import json
import logging
import socket
import time
from http.client import RemoteDisconnected
from itertools import cycle
from json import JSONDecodeError
from urllib.parse import urlparse

import requests_unixsocket

import certifi
import urllib3
from .exceptions import (
    EosdNoResponse,
    HttpAPIError,
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

    def __init__(self, nodes, **kwargs):
        self.api_version = kwargs.get('api_version', 'v1')
        self.max_retries = kwargs.get('max_retries', 10)

        if kwargs.get('tcp_keepalive', True):
            socket_options = HTTPConnection.default_socket_options + \
                             [(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1), ]
        else:
            socket_options = HTTPConnection.default_socket_options

        timeout = urllib3.Timeout(
            connect=kwargs.get('connect_timeout', 5),
            read=kwargs.get('timeout', 5))

        self.http = urllib3.poolmanager.PoolManager(
            num_pools=kwargs.get('num_pools', 50),
            maxsize=kwargs.get('maxsize', 10),
            block=kwargs.get('pool_block', False),
            retries=kwargs.get('http_retries', 5),
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

        self.session = requests_unixsocket.Session()

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

    def exec(self, api, endpoint, body=None, _ret_cnt=0):
        """ Execute a method against eosd RPC.

        Warnings:
            This command will auto-retry in case of node failure, as well as handle
            node fail-over, unless we are broadcasting a transaction.
            In latter case, the exception is **re-raised**.
        """
        body = self._body(body)
        method = 'POST' if body else 'GET'
        if self.node_url.startswith('unix://'):
            url = "http+{}/{}/{}/{}".format(self.node_url, self.api_version, api, endpoint)
            try:
                if body:
                    r = self.session.post(url, data = body)
                else:
                    r = self.session.get(url)
                return json.loads(r.text)
            except Exception as e:
                extra = dict(err=e, url=url, body=body, method=method)
                logger.info('Request error', extra=extra)
                raise e
        else:
            url = "{}/{}/{}/{}".format(self.node_url, self.api_version, api, endpoint)
            try:
                response = self.http.urlopen(method, url, body=body)
            except (MaxRetryError,
                    ConnectionResetError,
                    ReadTimeoutError,
                    RemoteDisconnected,
                    ProtocolError) as e:
    
                if _ret_cnt >= self.max_retries:
                    raise e
    
                # try switching nodes before giving up
                time.sleep(_ret_cnt)
                self.next_node()
                logging.debug('Switched node to %s due to exception: %s' %
                              (self.hostname, e.__class__.__name__))
                return self.exec(api, endpoint, body, _ret_cnt=_ret_cnt + 1)
            except Exception as e:
                extra = dict(err=e, url=url, body=body, method=method)
                logger.info('Request error', extra=extra)
                raise e
            else:
                return self._return(
                    response=response,
                    body=body)

    @staticmethod
    def _return(response=None, body=None):
        """ Process the response status code and body (json).

        Note:
            If re_raise flag is set, this method will raise an
            exception instead of returning None.

        Exceptions:
            EosdNoResponse on no response.
            HttpAPIError on non-200 response.

        Returns:
            Parsed response body.
        """

        if not response:
            raise EosdNoResponse(
                'eosd nodes have failed to respond, all retries exhausted.')
        result = response.data.decode('cp437')
        if not response.status in [200, 202, 201] or not result:
            extra = dict(result=result, response=response, request_body=body)
            logger.info('non ok response: %s',
                        response.status,
                        extra=extra)
            raise HttpAPIError(response.status, result)

        try:
            response_json = json.loads(result)
        except JSONDecodeError as e:
            extra = dict(response=response, request_body=body, err=e)
            logger.info('failed to parse response', extra=extra)
        else:
            result = response_json

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
