'''
Created on Sep 21, 2016

@author: paolo
'''
from happybase.table import Table
from happybase.util import thrift_type_to_dict
from tornado import gen



class TornadoTable(Table):
    
    @gen.coroutine
    def families(self):
        """ASYNCHRONOUS Retrieve the column families for this table.

        :return: Mapping from column family name to settings dict
        :rtype: dict
        """
        descriptors = yield self.connection.client.getColumnDescriptors(self.name)
        families = dict()
        for name, descriptor in descriptors.items():
            name = name.rstrip(b':')
            families[name] = thrift_type_to_dict(descriptor)
        raise gen.Return(families)
