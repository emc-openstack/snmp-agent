import collections
import functools
import os
import re
import time

from pysnmp.hlapi import *
from pysnmp.proto import rfc1902
from pysnmp.smi import builder as snmp_builder


def time_it(func):
    @functools.wraps(func)
    def _inner(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        time_used = end - start

        return result, time_used

    return _inner


class SNMPClient(object):
    def __init__(self, agent_ip, agent_port, community):
        self.mib_name = 'Unity-MIB'
        self.agent_ip = agent_ip
        self.agent_port = agent_port
        self.community = community

        self.engine = SnmpEngine()
        self._set_mib_source()

    def _set_mib_source(self):
        builder = self.engine.msgAndPduDsp.mibInstrumController.mibBuilder
        mib_dir_path = os.path.join(os.path.dirname(__file__), '..', 'mibs')
        builder.setMibSources(
            snmp_builder.DirMibSource(mib_dir_path),
            *builder.getMibSources())

    def _parse_var_bind(self, var_bind):
        # example: Unity-MIB::storageProcessorId.spa = spa
        pattern = re.compile(r'(.*)::(.*?)\s*=\s*(.*)')
        return pattern.findall(str(var_bind))[0]

    def _get(self, obj_identity):
        args = self.engine, \
               CommunityData(self.community), \
               UdpTransportTarget((self.agent_ip, self.agent_port)), \
               ContextData(), \
               ObjectType(obj_identity)

        kwargs = {'lexicographicMode': False}

        result = {}

        for (errorIndication,
             errorStatus,
             errorIndex,
             varBinds) in getCmd(*args, **kwargs):
            if errorIndication:
                print(errorIndication)
                break
            elif errorStatus:
                print('%s at %s' % (errorStatus.prettyPrint(),
                                    errorIndex and
                                    varBinds[int(errorIndex) - 1][0] or '?'))
                break
            else:
                for varBind in varBinds:
                    res = self._parse_var_bind(varBind)
                    value = varBind[1]
                    if isinstance(value, rfc1902.Integer32):
                        result[res[1]] = int(res[2])
                    else:
                        result[res[1]] = varBind[1]._value.decode('utf-8')

        return result

    def _get_next(self, obj_identity):
        args = self.engine, \
               CommunityData(self.community), \
               UdpTransportTarget((self.agent_ip, self.agent_port)), \
               ContextData(), \
               ObjectType(obj_identity)

        kwargs = {'lexicographicMode': False}

        result = {}

        for (errorIndication,
             errorStatus,
             errorIndex,
             varBinds) in nextCmd(*args, **kwargs):
            if errorIndication:
                print(errorIndication)
                break
            elif errorStatus:
                print('%s at %s' % (errorStatus.prettyPrint(),
                                    errorIndex and
                                    varBinds[int(errorIndex) - 1][0] or '?'))
                break
            else:
                for varBind in varBinds:
                    res = self._parse_var_bind(varBind)
                    value = varBind[1]
                    if isinstance(value, rfc1902.Integer32):
                        result[res[1]] = int(res[2])
                    else:
                        # result[res[1]] = varBind[1]._value
                        result[res[1]] = varBind[1]._value.decode('utf-8')

        return result

    def get_bulk(self):
        pass

    @time_it
    def get(self, mib_name):
        obj_identity = ObjectIdentity(self.mib_name, mib_name, 0)
        return self._get(obj_identity)

    @time_it
    def walk(self):
        obj_identity = ObjectIdentity(self.mib_name)
        self._get_next(obj_identity)

    @time_it
    def table_view(self, table_name):
        obj_identity = ObjectIdentity(self.mib_name, table_name)
        return self._get_next(obj_identity)

    def view_tables(self, tables):
        test_result = collections.OrderedDict()

        for table in tables:
            start = time.time()
            self.table_view(table)
            end = time.time()
            time_used = end - start
            test_result[table] = time_used

        for k, v in test_result.items():
            print('-' * 20)
            print('%s: %s' % (k, v))


if __name__ == '__main__':
    # tables = ['bbuTable', 'fanTable', 'powerSupplyTable', 'enclosureTable',
    #           'hostTable', 'backendPortTable', 'frontendPortTable',
    #           'diskTable', 'volumeTable', 'poolTable',
    #           'storageProcessorTable']
    # tables = ['diskTable']
    # tables = ['volumeTable']
    # tables = ['diskTable', 'volumeTable']
    tables = ['bbuTable']

    snmp_client = SNMPClient('192.168.56.1', 11161, 'public')

    # snmp_client.view_tables(tables)

    # start = time.time()
    # snmp_client.snmp_walk()
    # end = time.time()
    # time_used = end - start
    # print('-' * 20)
    # print('snmp walk: %s' % time_used)

    print(snmp_client.get('agentVersion'))
