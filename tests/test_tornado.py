'''
Created on Sep 21, 2016

@author: paolo
'''
from happybase.tornado_connection import TornadoConnection
from tests.test_api import HAPPYBASE_HOST, HAPPYBASE_PORT, TABLE_PREFIX,\
    HAPPYBASE_COMPAT

from tornado.testing import AsyncTestCase, gen_test


tornado_connection_kwargs = dict(
    host=HAPPYBASE_HOST,
    port=HAPPYBASE_PORT,
    table_prefix=None,
    compat=HAPPYBASE_COMPAT,
)

import unittest

class TornadoBaseTest(AsyncTestCase):

    def setUp(self):
        AsyncTestCase.setUp(self)
        
        self.connection = TornadoConnection(**tornado_connection_kwargs)
        

    def tearDown(self):
        AsyncTestCase.tearDown(self)


class TornadoConnectionTest(TornadoBaseTest):
    
    @gen_test
    def test_open(self):
        yield self.connection.open()
        

class TornadoTableTest(TornadoBaseTest):
    
    @gen_test
    def test_tabale_families(self):
        yield self.connection.open()
        
        table = self.connection.table('test_purpose_table')
        
        families = yield table.families()
        
        self.assertListEqual(families.keys(), [u'foo'])
        
        
    


    
if __name__ == '__main__':
    unittest.main()


