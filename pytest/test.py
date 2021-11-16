import os
import sys
import time
import pytest
import logging
from pyeoskit import _pyeoskit

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(lineno)d %(module)s %(message)s')
logger=logging.getLogger(__name__)
test_dir = os.path.dirname(__file__)


from pyeoskit.chainapi import ChainApi

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

    def test_basic(self):
        logger.info('hello,world')
        api = ChainApi('http://127.0.0.1:8888')
        logger.info(api.get_info())

    def test_api(self):
        assert(_pyeoskit.n2s(_pyeoskit.s2n('zzzzzzzzzzzzj')) == 'zzzzzzzzzzzzj')
        assert _pyeoskit.n2sym((_pyeoskit.sym2n('EOS', 4))) == '4,EOS'
        from pyeoskit.chainnative import ChainNative
        c = ChainNative()
        n = c.string_to_symbol('4,EOS')
        assert '4,EOS' == _pyeoskit.n2sym(n)
