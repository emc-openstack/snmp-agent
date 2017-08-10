import logging

from pyasn1.type import univ
from pysnmp.proto import rfc1902
from pysnmp.smi import error as pysnmp_ex
from snmpagent import exceptions as snmp_ex

LOG = logging.getLogger(__name__)
NONE_STRING = 'n/a'


def error_message(syntax):
    if isinstance(syntax, rfc1902.Integer32):
        msg = -999
    if isinstance(syntax, rfc1902.OctetString):
        msg = NONE_STRING

    return syntax.clone(msg)


def connection_check(snmp_engine):
    if snmp_engine.unity_client == None:
        LOG.info(
            'Reconnecting to unity: ip: {}, agent port: {}'.format(
                snmp_engine.parent.array_config.mgmt_ip,
                snmp_engine.parent.port))
        snmp_engine.parent.connect_backend_device()

    if snmp_engine.unity_client == None:
        raise snmp_ex.UnityConnectionError(
            'Connection failed: ip: {}, agent port: {}'.format(
                snmp_engine.parent.array_config.mgmt_ip,
                snmp_engine.parent.port))


class ScalarInstanceFactory(object):
    @staticmethod
    def build(name, base_class, impl_class):
        def __init__(self, *args, **kwargs):
            self.impl_class = impl_class
            base_class.__init__(self, *args, **kwargs)

        def __read_get__(self, name, val, idx, acInfo):
            try:
                engine = acInfo[1]
                connection_check(engine)

                idx_len = self.instId[0]
                idx_name = ''.join(
                    [chr(x) for x in self.instId[1: idx_len + 1]])

                result = self.impl_class().read_get(name, idx_name,
                                                    engine.unity_client)
                syntax = self.getSyntax()

                if isinstance(syntax, rfc1902.OctetString):
                    return name, syntax.clone(result, encoding='utf-8')
                else:
                    return name, syntax.clone(result)

            except Exception as exc:
                LOG.error('{}: {}'.format(exc.__class__.__name__, exc))
                return name, error_message(self.getSyntax())

        newclass = type(name + "ScalarInstance", (base_class,),
                        {"__init__": __init__,
                         "readGet": __read_get__
                         })
        return newclass


class TableColumnInstanceFactory(object):
    @staticmethod
    def build(name, base_class, proto_inst, entry, impl_class):
        def __init__(self, *args, **kwargs):
            self.entry = entry
            self.impl_class = impl_class
            self.maxAccess = 'readcreate'
            base_class.__init__(self, *args, **kwargs)

        def __read_getnext__(self, name, val, idx, acInfo, oName=None):
            try:
                engine = acInfo[1]
                connection_check(engine)

                if self.name == name:
                    row_list = self.impl_class().get_idx(name, idx,
                                                         engine.unity_client)
                    # Destory table rows, otherwise deleted items will
                    # exist in table
                    self.unregisterSubtrees(*self._vars.keys())
                    for row in row_list:
                        row_instance_id = self.entry.getInstIdFromIndices(row)
                        # Create table row and set default value
                        # DisplayString: null, Integer32: 0
                        # Only two types of data now: DisplayString, Integer32
                        # If new data types added, need to consider how to set val
                        if isinstance(val, univ.Null) and isinstance(
                                self.syntax, rfc1902.Integer32):
                            val = 0
                        self.createTest(name + row_instance_id, val, idx,
                                        acInfo)
                        self.createCommit(name + row_instance_id, val, idx,
                                          acInfo)
                next_node = self.getNextNode(name, idx)
                return next_node.readGet(next_node.name, val, idx, acInfo)

            except pysnmp_ex.NoSuchInstanceError:
                # Need to raise NoSuchInstanceError, client will handle it
                raise

            except Exception as exc:
                LOG.error('{}: {}'.format(exc.__class__.__name__, exc))
                return name, error_message(self.getSyntax())

        newclass = type(name + "Instance", (base_class,),
                        {"__init__": __init__,
                         "protoInstance": proto_inst,
                         "readGetNext": __read_getnext__})
        return newclass
