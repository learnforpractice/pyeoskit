import os
import sys
import time
import pytest
import logging
import asyncio

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(lineno)d %(module)s %(message)s')
logger=logging.getLogger(__name__)
test_dir = os.path.dirname(__file__)


from uuoskit.chainapi import ChainApi, ChainApiAsync
from uuoskit import wallet, config

@pytest.fixture
def event_loop():
    pass

class Test(object):

    @classmethod
    def setup_class(cls):
        pass

    @classmethod
    def teardown_class(cls):
        pass

    def setup_method(self, method):
        pass

    def teardown_method(self, method):
        pass

    async def set_code_get_code_async(self):
        api = ChainApiAsync('http://127.0.0.1:8888', 'UUOS')
        api.set_code('hello', b'abc')
        assert await api.get_code('hello') == b'abc'

    def test_set_code_get_code(self):
        api = ChainApi('http://127.0.0.1:8888', 'UUOS')
        api.set_code('hello', b'abc')
        assert api.get_code('hello') == b'abc'

    def test_set_code_get_code_async(self):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.set_code_get_code_async())
        loop.close()