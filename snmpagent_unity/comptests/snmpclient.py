import functools
import os
import re
import time

from pysnmp import hlapi
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
    mib_name = 'Unity-MIB'

    def __init__(self):
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
        args = self.snmp_basic_info + (hlapi.ObjectType(obj_identity),)

        kwargs = {'lexicographicMode': False}

        result = {}

        for (errorIndication,
             errorStatus,
             errorIndex,
             varBinds) in hlapi.getCmd(*args, **kwargs):
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
        args = self.snmp_basic_info + (hlapi.ObjectType(obj_identity),)

        kwargs = {'lexicographicMode': False}

        result = {}

        for (errorIndication,
             errorStatus,
             errorIndex,
             varBinds) in hlapi.nextCmd(*args, **kwargs):
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

    @time_it
    def get_bulk(self):
        pass

    @time_it
    def get(self, mib_name):
        obj_identity = hlapi.ObjectIdentity(self.mib_name, mib_name, 0)
        return self._get(obj_identity)

    @time_it
    def walk(self):
        obj_identity = hlapi.ObjectIdentity(self.mib_name)
        self._get_next(obj_identity)

    @time_it
    def table_view(self, table_name):
        obj_identity = hlapi.ObjectIdentity(self.mib_name, table_name)
        return self._get_next(obj_identity)


class SNMPv2Client(SNMPClient):
    def __init__(self, agent_ip, agent_port, community):
        self.agent_ip = agent_ip
        self.agent_port = agent_port

        # SNMPv2 community
        self.community = community
        self.engine = hlapi.SnmpEngine()
        self.community_data = hlapi.CommunityData(self.community)
        self.transport_target = hlapi.UdpTransportTarget(
            (self.agent_ip, self.agent_port))
        self.context_data = hlapi.ContextData()

        self.snmp_basic_info = (self.engine,
                                self.community_data,
                                self.transport_target,
                                self.context_data)

        super(SNMPv2Client, self).__init__()


class SNMPv3Client(SNMPClient):
    def __init__(self, agent_ip, agent_port, user_name, auth_key,
                 priv_key=None, auth_proto=None, priv_proto=None):
        self.agent_ip = agent_ip
        self.agent_port = agent_port

        # SNMPv3 user
        self.user_name = user_name
        self.auth_key = auth_key
        self.priv_key = priv_key
        self.auth_proto = auth_proto
        self.priv_proto = priv_proto

        args = (self.user_name,)
        kwargs = self._get_user_data()
        self.user_data = hlapi.UsmUserData(*args, **kwargs)

        self.engine = hlapi.SnmpEngine()
        self.transport_target = hlapi.UdpTransportTarget(
            (self.agent_ip, self.agent_port))
        self.context_data = hlapi.ContextData()

        self.snmp_basic_info = (self.engine,
                                self.user_data,
                                self.transport_target,
                                self.context_data)

        super(SNMPv3Client, self).__init__()

    def _get_user_data(self):
        if self.auth_key is None:
            return {}

        kwargs = {'authKey': self.auth_key}

        if self.priv_key is not None:
            kwargs['privKey'] = self.priv_key

        if self.auth_proto == 'sha':
            kwargs['authProtocol'] = hlapi.usmHMACSHAAuthProtocol

        if self.priv_proto == 'aes':
            kwargs['privProtocol'] = hlapi.usmAesCfb128Protocol

        return kwargs


if __name__ == '__main__':
    agent_ip = '192.168.56.1'
    agent_port = 11161

    # SNMPv2 community: public
    snmpclient_v2_community = SNMPv2Client(agent_ip, agent_port, 'public')

    # SNMPv3: auth MD5, privacy AES
    snmpclient_v3_md5_aes = SNMPv3Client(agent_ip, agent_port, 'user-md5-aes',
                                         auth_key='12345678',
                                         priv_key='12345678', priv_proto='aes')

    # SNMPv3: auth MD5, privacy DES
    snmpclient_v3_md5_des = SNMPv3Client(agent_ip, agent_port, 'user-md5-des',
                                         auth_key='12345678',
                                         priv_key='12345678')

    # SNMPv3: auth MD5, no privacy
    snmpclient_v3_md5 = SNMPv3Client(agent_ip, agent_port, 'user-md5',
                                     auth_key='12345678')

    # SNMPv3: auth SHA, privacy AES128
    snmpclient_v3_sha_aes = SNMPv3Client(agent_ip, agent_port, 'user-sha-aes',
                                         auth_key='12345678',
                                         priv_key='12345678', auth_proto='sha',
                                         priv_proto='aes')

    # SNMPv3: auth SHA, privacy AES128
    snmpclient_v3_sha_des = SNMPv3Client(agent_ip, agent_port, 'user-sha-des',
                                         auth_key='12345678',
                                         priv_key='12345678', auth_proto='sha',
                                         priv_proto='des')

    # SNMPv3: auth SHA, privacy AES128
    snmpclient_v3_sha = SNMPv3Client(agent_ip, agent_port, 'user-sha',
                                     auth_key='12345678', auth_proto='sha')

    # tables = ['bbuTable', 'fanTable', 'powerSupplyTable', 'enclosureTable',
    #           'hostTable', 'backendPortTable', 'frontendPortTable',
    #           'diskTable', 'volumeTable', 'poolTable',
    #           'storageProcessorTable']
    tables = ['bbuTable']

    for snmpclient in (
            snmpclient_v3_md5_aes, snmpclient_v3_md5_des, snmpclient_v3_md5,
            snmpclient_v3_sha_aes, snmpclient_v3_sha_des, snmpclient_v3_sha):
        print('SNMP Client: {}'.format(snmpclient))
        print(snmpclient.get('agentVersion'))

        for table in tables:
            result, time_used = snmpclient.table_view(table)
            print('Table: {}, time used: {}'.format(table, time_used))
            print(result)
