# encoding: utf-8
import sys
import unittest

import mock
from requests import exceptions as requests_ex
from snmpagent_unity import factory

from pysnmp.proto import rfc1902
from storops.connection import exceptions as storops_ex

AGENT_VERSION = b'1.1'
NUMBER_OF_DISK = 30
NONE_STRING = b'n/a'
ERROR_NUMBER = -999
CONNECTION_ERROR_MSG = factory.CONNECTION_ERROR_MSG


class FakeStringMibScalarInstance(object):
    def getSyntax(self):
        return rfc1902.OctetString()


class FakeIntegerMibScalarInstance(object):
    def getSyntax(self):
        return rfc1902.Integer32()


class FakeAgentVersionImpl(object):
    def read_get(self, *args):
        return AGENT_VERSION


class FakeNumberOfDiskImpl(object):
    def read_get(self, *args):
        return NUMBER_OF_DISK


class FakeMibVersionImpl(object):
    def read_get(self, *args):
        raise requests_ex.ConnectionError('err')


class FakeNumberOfFanImpl(object):
    def read_get(self, *args):
        raise storops_ex.HttpError('401')


class TestScalarInstanceFactory(unittest.TestCase):
    def setUp(self):
        self.mib_oid = (1, 3, 6, 1, 4, 1, 1139, 103, 1, 19, 29, 1, 1)
        self.inst_oid = (3, 97, 98, 99)
        self.unity_client = 'FakeUnityClient'

    @mock.patch('snmpagent_unity.agent.engine.SnmpEngine')
    def test_build_string_scalar_instance_class(self, snmp_engine):
        class_name = 'FakeAgentVersion'
        base_class = FakeStringMibScalarInstance
        impl_class = FakeAgentVersionImpl

        scalar_instance_clz = factory.ScalarInstanceFactory.build(
            name=class_name,
            base_class=base_class,
            impl_class=impl_class)

        # check the basic info for generated class
        self.assertTrue(issubclass(scalar_instance_clz, base_class))
        self.assertEqual(scalar_instance_clz.__name__,
                         class_name + 'ScalarInstance')

        # check the read_get method for generated class
        scalar_instance = scalar_instance_clz()
        scalar_instance.instId = self.inst_oid
        self.assertEqual(scalar_instance.impl_class, impl_class)

        name = self.mib_oid
        result = scalar_instance.readGet(name, None, 0, (1, snmp_engine))

        self.assertEqual(result[0], name)
        self.assertTrue(isinstance(result[1], rfc1902.OctetString))
        self.assertEqual(result[1]._value, AGENT_VERSION)

    @mock.patch('snmpagent_unity.agent.engine.SnmpEngine')
    def test_build_integer_scalar_instance_class(self, snmp_engine):
        class_name = 'FakeNumberOfDisk'
        base_class = FakeIntegerMibScalarInstance
        impl_class = FakeNumberOfDiskImpl

        scalar_instance_clz = factory.ScalarInstanceFactory.build(
            name=class_name,
            base_class=base_class,
            impl_class=impl_class)

        # check the basic info for generated class
        self.assertTrue(issubclass(scalar_instance_clz, base_class))
        self.assertEqual(scalar_instance_clz.__name__,
                         class_name + 'ScalarInstance')

        # check the read_get method for generated class
        scalar_instance = scalar_instance_clz()
        scalar_instance.instId = self.inst_oid
        self.assertEqual(scalar_instance.impl_class, impl_class)

        name = self.mib_oid
        result = scalar_instance.readGet(name, None, 0, (1, snmp_engine))

        self.assertEqual(result[0], name)
        self.assertTrue(isinstance(result[1], rfc1902.Integer32))
        self.assertEqual(result[1]._value, NUMBER_OF_DISK)

    @mock.patch('snmpagent_unity.agent.engine.SnmpEngine')
    def test_failed_to_build_string_scalar_instance_class(self, snmp_engine):
        class_name = 'FakeMibVersion'
        base_class = FakeStringMibScalarInstance
        impl_class = FakeMibVersionImpl

        scalar_instance_clz = factory.ScalarInstanceFactory.build(
            name=class_name,
            base_class=base_class,
            impl_class=impl_class)

        # check the basic info for generated class
        self.assertTrue(issubclass(scalar_instance_clz, base_class))
        self.assertEqual(scalar_instance_clz.__name__,
                         class_name + 'ScalarInstance')

        # check the read_get method for generated class
        scalar_instance = scalar_instance_clz()
        scalar_instance.instId = self.inst_oid
        self.assertEqual(scalar_instance.impl_class, impl_class)

        name = self.mib_oid
        result = scalar_instance.readGet(name, None, 0, (1, snmp_engine))

        self.assertEqual(result[0], name)
        self.assertTrue(isinstance(result[1], rfc1902.OctetString))
        if sys.version_info.major == 3:
            err_msg = str(result[1]._value, 'utf-8')
        else:
            err_msg = str(result[1]._value)
        self.assertEqual(err_msg, CONNECTION_ERROR_MSG)

    @mock.patch('snmpagent_unity.agent.engine.SnmpEngine')
    def test_failed_to_build_integer_scalar_instance_class(self, snmp_engine):
        class_name = 'FakeNumberOfFan'
        base_class = FakeIntegerMibScalarInstance
        impl_class = FakeNumberOfFanImpl

        scalar_instance_clz = factory.ScalarInstanceFactory.build(
            name=class_name,
            base_class=base_class,
            impl_class=impl_class)

        # check the basic info for generated class
        self.assertTrue(issubclass(scalar_instance_clz, base_class))
        self.assertEqual(scalar_instance_clz.__name__,
                         class_name + 'ScalarInstance')

        # check the read_get method for generated class
        scalar_instance = scalar_instance_clz()
        scalar_instance.instId = self.inst_oid
        self.assertEqual(scalar_instance.impl_class, impl_class)

        name = self.mib_oid
        result = scalar_instance.readGet(name, None, 0, (1, snmp_engine))

        self.assertEqual(result[0], name)
        self.assertTrue(isinstance(result[1], rfc1902.Integer32))
        self.assertEqual(result[1]._value, ERROR_NUMBER)

# class FakeMibTableColumn(object):
#     pass
#
#
# class FakeDiskNameColumnImpl(object):
#     # def __init__(self):
#     #     self._vars = {}
#
#     def get_idx(self, *args):
#         return ['id_disk_1', 'id_disk_2', 'id_disk_3']
#
#     def unregisterSubtrees(self, *args):
#         return
#
#
# class TestTableColumnInstanceFactory(unittest.TestCase):
#     def setUp(self):
#         self.entry = (1, 3, 6, 1, 4, 1, 1139, 103, 1, 19, 29, 1)
#         self.mib_oid = self.entry + (2,)
#         self.unity_client = 'FakeUnityClient'
#         # self.inst_oid = (3, 97, 98, 99)
#         # self.unity_client = 'FakeUnityClient'
#
#     @mock.patch('snmpagent_unity.agent.engine.SnmpEngine')
#     def test_build_column_instance_class(self, snmp_engine):
#         class_name = 'FakeDiskName'
#         base_class = FakeMibTableColumn
#         impl_class = FakeDiskNameColumnImpl
#         proto_inst = 1
#         entry = self.entry
#
#         column_instance_clz = factory.TableColumnInstanceFactory.build(
#             name=class_name,
#             base_class=base_class,
#             proto_inst=proto_inst,
#             entry=entry,
#             impl_class=impl_class)
#
#         # check the basic info for generated class
#         self.assertTrue(issubclass(column_instance_clz, base_class))
#         self.assertEqual(column_instance_clz.__name__,
#                          class_name + 'Instance')
#
#         # check the read_getnext method for generated class
#         column_instance = column_instance_clz()
#         # self.assertEqual(column_instance.impl_class, impl_class)
#         column_instance.name = self.mib_oid
#         column_instance._vars = {}
#
#         def effect():
#             snmp_engine.unity_client = self.unity_client
#
#         parent_engine = mock.MagicMock()
#         parent_engine.connect_backend_device.side_effect = effect
#
#         snmp_engine.unity_client = None
#         snmp_engine.parent = parent_engine
#
#         name = self.mib_oid
#         result = column_instance.readGetNext(name, None, 0, (1, snmp_engine))
#
#         # self.assertEqual(result[0], name)
#         # self.assertTrue(isinstance(result[1], rfc1902.OctetString))
#         # self.assertEqual(result[1]._value, AGENT_VERSION)
#         # self.assertEqual(snmp_engine.unity_client, self.unity_client)
