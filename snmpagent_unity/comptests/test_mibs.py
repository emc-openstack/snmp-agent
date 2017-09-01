import collections
import functools
import sys
import unittest

import snmpagent_unity
from snmpagent_unity import clients
from snmpagent_unity.comptests import snmpclient

import storops

try:
    import urllib3

    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
except:
    pass

NONE_STRING = clients.NONE_STRING

FC_PORT_TYPE = clients.FC_PORT_TYPE
ISCSI_PORT_TYPE = clients.ISCSI_PORT_TYPE
DAE_TYPE = clients.DAE_TYPE
DPE_TYPE = clients.DPE_TYPE


def to_camel(string):
    components = string.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])


def get_column_mib(table, column, index):
    return '{}.{}'.format(to_camel('{}_{}'.format(table, column)), index)


def get_scalar_mib(mib_name):
    return mib_name + '.0'


def get_nested_value(obj, *args):
    values = collections.deque(args)
    while values:
        attr = values.popleft()
        if hasattr(obj, attr) and getattr(obj, attr) is not None:
            obj = getattr(obj, attr)
        else:
            obj = None
            break

    return obj


def byte_to_gb(size):
    if size == 0:
        return size
    else:
        return round(size / 2 ** 30, 3)


def strip_type(string, *type_list):
    lst = string.split('.')
    if len(lst) == 2:
        index = lst[1]
        for type in type_list:
            if index.startswith(type):
                index = index.replace(type, '', 1)
        return lst[0] + '.' + index
    else:
        return string


def has_str_value(value):
    if sys.version_info.major == 2:
        return isinstance(value, unicode) and bool(value)
    if sys.version_info.major == 3:
        return isinstance(value, str) and bool(value)


def has_num_value(value):
    return isinstance(value, (int, float))


class TestUnityMibs(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        agent_ip = '127.0.0.1'
        agent_port = 11161
        community = 'public'
        cls._snmp_client = snmpclient.SNMPClient(agent_ip, agent_port,
                                                 community)

        cls._unity_system = storops.UnitySystem('10.245.101.39', 'admin',
                                                'Password123!')
        cls._unity_system.enable_perf_stats()

    def _assert_equal(self, expect, actual):
        if isinstance(expect, bool):
            expect = str(expect)

        if expect is None or expect == '':
            self.assertEqual(NONE_STRING, actual)
        else:
            self.assertEqual(expect, actual)

    def _assert_in(self, expect, actual):
        if isinstance(expect, bool):
            expect = str(expect)

        if expect is None or expect == '':
            self.assertEqual(NONE_STRING, actual)
        else:
            self.assertIn(expect, actual)

    def _assert_less_equal(self, a, b):
        self.assertLessEqual(a, b)

    def _assert_has_str_value(self, value):
        self.assertTrue(has_str_value(value))

    def _assert_has_num_value(self, value):
        self.assertTrue(has_num_value(value))

    def _assert_close_to(self, expect, actual, num):
        if actual == NONE_STRING:
            self.assertEqual(expect, actual)
        else:
            rst = abs(float(expect) - float(actual)) < float(num)
            self.assertTrue(rst)

    def _check_parent_enclosure(self, item, actual):
        if hasattr(item, 'parent_dpe') and item.parent_dpe is not None:
            self._assert_equal(get_nested_value(item, 'parent_dpe', 'name'),
                               actual)
        if hasattr(item, 'parent_dae') and item.parent_dae is not None:
            self._assert_equal(get_nested_value(item, 'parent_dae', 'name'),
                               actual)

    def test_agent_version(self):
        mib_name = 'agentVersion'
        result, time_used = self._snmp_client.get(mib_name)

        print('Time used for Agent version get: {}'.format(time_used))
        self._assert_less_equal(time_used, 5)

        self._assert_equal(snmpagent_unity.__version__,
                           result.get(get_scalar_mib(mib_name)))

    def test_mib_version(self):
        mib_name = 'mibVersion'
        result, time_used = self._snmp_client.get(mib_name)

        print('Time used for Mib version get: {}'.format(time_used))
        self._assert_less_equal(time_used, 5)

        self._assert_equal('1.0', result.get(get_scalar_mib(mib_name)))

    def test_manufacturer(self):
        mib_name = 'manufacturer'
        result, time_used = self._snmp_client.get(mib_name)

        print('Time used for Manufacturer get: {}'.format(time_used))
        self._assert_less_equal(time_used, 5)

        self._assert_equal('DellEMC', result.get(get_scalar_mib(mib_name)))

    def test_model(self):
        mib_name = 'model'
        result, time_used = self._snmp_client.get(mib_name)

        print('Time used for Model get: {}'.format(time_used))
        self._assert_less_equal(time_used, 10)

        item = self._unity_system.model
        self._assert_equal(item, result.get(get_scalar_mib(mib_name)))

    def test_serial_number(self):
        mib_name = 'serialNumber'
        result, time_used = self._snmp_client.get(mib_name)

        print('Time used for Serial number get: {}'.format(time_used))
        self._assert_less_equal(time_used, 10)

        item = self._unity_system.serial_number
        self._assert_equal(item, result.get(get_scalar_mib(mib_name)))

    def test_operation_environment_version(self):
        mib_name = 'operationEnvironmentVersion'
        result, time_used = self._snmp_client.get(mib_name)

        print('Time used for Operation environment version get: {}'.format(
            time_used))
        self._assert_less_equal(time_used, 10)

        item = self._unity_system.system_version
        self._assert_equal(item, result.get(get_scalar_mib(mib_name)))

    def test_management_ip(self):
        mib_name = 'managementIP'
        result, time_used = self._snmp_client.get(mib_name)

        print('Time used for Management IP get: {}'.format(time_used))
        self._assert_less_equal(time_used, 10)

        items = self._unity_system.get_mgmt_interface()

        for item in items:
            self._assert_in(item.ip_address,
                            result.get(get_scalar_mib(mib_name)))

    def test_current_power(self):
        mib_name = 'currentPower'
        result, time_used = self._snmp_client.get(mib_name)

        print('Time used for Current power get: {}'.format(time_used))
        self._assert_less_equal(time_used, 10)

        # The value change frequently, so only check it has value
        # self._unity_system.update()
        # item = self._unity_system.current_power
        # self._assert_equal(str(item), result.get(get_scalar_mib(mib_name)))
        self._assert_has_str_value(result.get(get_scalar_mib(mib_name)))

    def test_average_power(self):
        mib_name = 'averagePower'
        result, time_used = self._snmp_client.get(mib_name)

        print('Time used for Average power get: {}'.format(time_used))
        self._assert_less_equal(time_used, 10)

        # The value change frequently, so only check it has value
        # self._unity_system.update()
        # item = self._unity_system.avg_power
        # self._assert_equal(str(item), result.get(get_scalar_mib(mib_name)))
        self._assert_has_str_value(result.get(get_scalar_mib(mib_name)))

    def test_number_of_storage_processor(self):
        mib_name = 'numberOfStorageProcessor'
        result, time_used = self._snmp_client.get(mib_name)

        print(
            'Number of storage processor get: {}'.format(time_used))
        self._assert_less_equal(time_used, 10)

        item = len(self._unity_system.get_sp())
        self._assert_equal(item, result.get(get_scalar_mib(mib_name)))

    def test_number_of_enclosure(self):
        mib_name = 'numberOfEnclosure'
        result, time_used = self._snmp_client.get(mib_name)

        print('Time used for Number of enclosure get: {}'.format(time_used))
        self._assert_less_equal(time_used, 10)

        item = len(self._unity_system.get_dpe()) + len(
            self._unity_system.get_dae())
        self._assert_equal(item, result.get(get_scalar_mib(mib_name)))

    def test_number_of_power_supply(self):
        mib_name = 'numberOfPowerSupply'
        result, time_used = self._snmp_client.get(mib_name)

        print('Time used for Number of power supply get: {}'.format(time_used))
        self._assert_less_equal(time_used, 10)

        item = len(self._unity_system.get_power_supply())
        self._assert_equal(item, result.get(get_scalar_mib(mib_name)))

    def test_number_of_fan(self):
        mib_name = 'numberOfFan'
        result, time_used = self._snmp_client.get(mib_name)

        print('Time used for Number of fan get: {}'.format(time_used))
        self._assert_less_equal(time_used, 10)

        item = len(self._unity_system.get_fan())
        self._assert_equal(item, result.get(get_scalar_mib(mib_name)))

    def test_number_of_physical_disk(self):
        mib_name = 'numberOfPhysicalDisk'
        result, time_used = self._snmp_client.get(mib_name)

        print('Time used for Number of physical disk get: {}'.format(time_used))
        self._assert_less_equal(time_used, 10)

        item = len(self._unity_system.get_disk())
        self._assert_equal(item, result.get(get_scalar_mib(mib_name)))

    def test_number_of_frontend_port(self):
        mib_name = 'numberOfFrontendPort'
        result, time_used = self._snmp_client.get(mib_name)

        print('Time used for Number of frontend port get: {}'.format(time_used))
        self._assert_less_equal(time_used, 10)

        item = len(self._unity_system.get_fc_port()) + len(
            self._unity_system.get_iscsi_node())
        self._assert_equal(item, result.get(get_scalar_mib(mib_name)))

    def test_number_of_backend_port(self):
        mib_name = 'numberOfBackendPort'
        result, time_used = self._snmp_client.get(mib_name)

        print('Time used for Number of backend port get: {}'.format(time_used))
        self._assert_less_equal(time_used, 10)

        print(result)
        item = len(self._unity_system.get_sas_port())
        self._assert_equal(item, result.get(get_scalar_mib(mib_name)))

    def test_total_capacity(self):
        mib_name = 'totalCapacity'
        result, time_used = self._snmp_client.get(mib_name)

        print('Time used for Total capacity get: {}'.format(time_used))
        self._assert_less_equal(time_used, 10)

        item = self._unity_system.get_system_capacity()[0].size_total
        self._assert_close_to(byte_to_gb(item),
                              result.get(get_scalar_mib(mib_name)), 1)

    def test_used_capacity(self):
        mib_name = 'usedCapacity'
        result, time_used = self._snmp_client.get(mib_name)

        print('Time used for Used capacity get: {}'.format(time_used))
        self._assert_less_equal(time_used, 10)

        item = self._unity_system.get_system_capacity()[0].size_used
        self._assert_close_to(byte_to_gb(item),
                              result.get(get_scalar_mib(mib_name)), 1)

    def test_free_capacity(self):
        mib_name = 'freeCapacity'
        result, time_used = self._snmp_client.get(mib_name)

        print('Time used for Free capacity get: {}'.format(time_used))
        self._assert_less_equal(time_used, 10)

        item = self._unity_system.get_system_capacity()[0].size_free
        self._assert_close_to(byte_to_gb(item),
                              result.get(get_scalar_mib(mib_name)), 1)

    # metric
    def test_total_throughput(self):
        mib_name = 'totalThroughput'
        result, time_used = self._snmp_client.get(mib_name)

        print('Time used for Total throughput get: {}'.format(time_used))
        self._assert_less_equal(time_used, 10)

        self._assert_has_str_value(result.get(get_scalar_mib(mib_name)))

    def test_read_throughput(self):
        mib_name = 'readThroughput'
        result, time_used = self._snmp_client.get(mib_name)

        print('Time used for Read throughput get: {}'.format(time_used))
        self._assert_less_equal(time_used, 10)

        self._assert_has_str_value(result.get(get_scalar_mib(mib_name)))

    def test_write_throughput(self):
        mib_name = 'writeThroughput'
        result, time_used = self._snmp_client.get(mib_name)

        print('Time used for Write throughput get: {}'.format(time_used))
        self._assert_less_equal(time_used, 10)

        self._assert_has_str_value(result.get(get_scalar_mib(mib_name)))

    def test_total_bandwidth(self):
        mib_name = 'totalBandwidth'
        result, time_used = self._snmp_client.get(mib_name)

        print('Time used for Total bandwidth get: {}'.format(time_used))
        self._assert_less_equal(time_used, 10)

        self._assert_has_str_value(result.get(get_scalar_mib(mib_name)))

    def test_read_bandwidth(self):
        mib_name = 'readBandwidth'
        result, time_used = self._snmp_client.get(mib_name)

        print('Time used for Read bandwidth get: {}'.format(time_used))
        self._assert_less_equal(time_used, 10)

        self._assert_has_str_value(result.get(get_scalar_mib(mib_name)))

    def test_write_bandwidth(self):
        mib_name = 'writeBandwidth'
        result, time_used = self._snmp_client.get(mib_name)

        print('Time used for Write bandwidth get: {}'.format(time_used))
        self._assert_less_equal(time_used, 10)

        self._assert_has_str_value(result.get(get_scalar_mib(mib_name)))

    def test_storage_processor_table_view(self):
        table_name = 'storageProcessor'
        mib_name = table_name + 'Table'
        result, time_used = self._snmp_client.table_view(mib_name)

        print('Time used for Storage processor table view: {}'.format(time_used))
        self._assert_less_equal(time_used, 30)

        items = self._unity_system.get_sp()

        column_mib = functools.partial(get_column_mib, table_name)
        for item in items:
            self._assert_equal(item.id, result.get(column_mib('id', item.id)))
            self._assert_equal(item.name,
                               result.get(column_mib('name', item.id)))
            self._assert_equal(item.emc_serial_number, result.get(
                column_mib('serial_number', item.id)))
            self._assert_equal(
                get_nested_value(item, 'health', 'value', 'name'),
                result.get(column_mib('operational_state', item.id)))

            # metric
            self._assert_has_str_value(
                result.get(column_mib('cpu_utilization', item.id)))
            self._assert_has_str_value(
                result.get(column_mib('total_throughput', item.id)))
            self._assert_has_str_value(
                result.get(column_mib('read_throughput', item.id)))
            self._assert_has_str_value(
                result.get(column_mib('write_throughput', item.id)))
            self._assert_has_str_value(
                result.get(column_mib('total_bandwidth', item.id)))
            self._assert_has_str_value(
                result.get(column_mib('read_bandwidth', item.id)))
            self._assert_has_str_value(
                result.get(column_mib('write_bandwidth', item.id)))
            self._assert_has_str_value(
                result.get(column_mib('cache_dirty_size', item.id)))
            self._assert_has_str_value(
                result.get(column_mib('read_cache_state', item.id)))
            self._assert_has_str_value(
                result.get(column_mib('write_cache_state', item.id)))

    def test_pool_table_view(self):
        table_name = 'pool'
        mib_name = table_name + 'Table'
        result, time_used = self._snmp_client.table_view(mib_name)

        print('Time used for Pool table view: {}'.format(time_used))
        self._assert_less_equal(time_used, 30)

        items = self._unity_system.get_pool()

        column_mib = functools.partial(get_column_mib, table_name)
        for item in items:
            self._assert_equal(item.id, result.get(column_mib('id', item.id)))
            self._assert_equal(item.name,
                               result.get(column_mib('name', item.id)))

            disk_types_by_snmp = result.get(column_mib('disk_types', item.id))
            disk_types_by_storops = item.tiers
            if disk_types_by_storops:
                for disk_type in disk_types_by_storops:
                    self._assert_in(disk_type.name, disk_types_by_snmp)
            else:
                self._assert_equal(NONE_STRING, disk_types_by_snmp)

            self._assert_equal(get_nested_value(item, 'raid_type', 'name'),
                               result.get(column_mib('raid_levels', item.id)))
            self._assert_equal(item.is_fast_cache_enabled, result.get(
                column_mib('fast_cache_status', item.id)))

            number_of_disk_by_snmp = result.get(
                column_mib('number_of_physical_disk', item.id))
            number_of_disk_by_storops = sum(x.disk_count for x in item.tiers)
            self._assert_equal(number_of_disk_by_storops,
                               number_of_disk_by_snmp)

            self._assert_close_to(byte_to_gb(item.size_total), result.get(
                column_mib('total_capacity', item.id)), 1)
            self._assert_close_to(byte_to_gb(item.size_free), result.get(
                column_mib('remaining_capacity', item.id)), 1)
            self._assert_close_to(byte_to_gb(item.size_used), result.get(
                column_mib('used_capacity', item.id)), 1)
            utilization = round(
                byte_to_gb(item.size_used) / byte_to_gb(item.size_total), 3)
            self._assert_close_to(utilization, result.get(
                column_mib('capacity_utilization', item.id)), 1)

    def test_volume_table_view(self):
        table_name = 'volume'
        mib_name = table_name + 'Table'
        result, time_used = self._snmp_client.table_view(mib_name)

        print('Time used for Volume table view: {}'.format(time_used))
        self._assert_less_equal(time_used, 90)

        items = self._unity_system.get_lun()

        column_mib = functools.partial(get_column_mib, table_name)
        for item in items:
            self._assert_equal(item.id, result.get(column_mib('id', item.id)))
            self._assert_equal(item.name,
                               result.get(column_mib('name', item.id)))
            self._assert_equal(
                get_nested_value(item, 'pool', 'raid_type', 'name'),
                result.get(column_mib('raid_levels', item.id)))
            self._assert_close_to(byte_to_gb(item.size_allocated), result.get(
                column_mib('allocated_size', item.id)), 1)
            self._assert_close_to(byte_to_gb(item.size_total),
                                  result.get(column_mib('size', item.id)), 1)
            self._assert_equal(
                get_nested_value(item, 'health', 'value', 'name'),
                result.get(column_mib('operational_state', item.id)))
            self._assert_equal(
                str(get_nested_value(item, 'pool', 'is_fast_cache_enabled')),
                result.get(column_mib('fast_cache_state', item.id)))
            self._assert_equal(get_nested_value(item, 'default_node', 'name'),
                               result.get(
                                   column_mib('default_storage_processor',
                                              item.id)))
            self._assert_equal(get_nested_value(item, 'current_node', 'name'),
                               result.get(
                                   column_mib('current_storage_processor',
                                              item.id)))

            # metric
            self._assert_has_str_value(
                result.get(column_mib('response_time', item.id)))
            self._assert_has_str_value(
                result.get(column_mib('queue_length', item.id)))
            self._assert_has_str_value(
                result.get(column_mib('total_throughput', item.id)))
            self._assert_has_str_value(
                result.get(column_mib('read_throughput', item.id)))
            self._assert_has_str_value(
                result.get(column_mib('write_throughput', item.id)))
            self._assert_has_str_value(
                result.get('volumeFastCacheReadHitIOs.' + item.id))
            self._assert_has_str_value(
                result.get('volumeFastCacheWriteHitIOs.' + item.id))
            self._assert_has_str_value(
                result.get(column_mib('total_bandwidth', item.id)))
            self._assert_has_str_value(
                result.get(column_mib('read_bandwidth', item.id)))
            self._assert_has_str_value(
                result.get(column_mib('write_bandwidth', item.id)))
            self._assert_has_str_value(
                result.get(column_mib('fast_cache_read_hit_rate', item.id)))
            self._assert_has_str_value(
                result.get(column_mib('fast_cache_write_hit_rate', item.id)))
            self._assert_has_str_value(
                result.get(column_mib('utilization', item.id)))

            host_access_by_snmp = result.get(column_mib('host_info', item.id))
            host_access_by_storops = item.host_access
            if host_access_by_storops:
                for host_access in host_access_by_storops:
                    self._assert_in(
                        get_nested_value(host_access, 'host', 'name'),
                        host_access_by_snmp)
            else:
                self._assert_equal(NONE_STRING, host_access_by_snmp)

    def test_disk_table_view(self):
        table_name = 'disk'
        mib_name = table_name + 'Table'
        result, time_used = self._snmp_client.table_view(mib_name)

        print('Time used for Disk table view: {}'.format(time_used))
        self._assert_less_equal(time_used, 90)

        items = self._unity_system.get_disk()

        column_mib = functools.partial(get_column_mib, table_name)
        for item in items:
            self._assert_equal(item.id, result.get(column_mib('id', item.id)))
            self._assert_equal(item.name,
                               result.get(column_mib('name', item.id)))
            self._assert_equal(item.model,
                               result.get(column_mib('model', item.id)))
            self._assert_equal(item.emc_serial_number, result.get(
                column_mib('serial_number', item.id)))
            self._assert_equal(item.version, result.get(
                column_mib('firmware_version', item.id)))
            self._assert_equal(
                get_nested_value(item, 'disk_technology', 'name'),
                result.get(column_mib('type', item.id)))
            self._assert_equal(str(item.slot_number), result.get(
                column_mib('physical_location', item.id)))
            self._assert_equal(
                get_nested_value(item, 'health', 'value', 'name'),
                result.get(column_mib('status', item.id)))
            self._assert_close_to(byte_to_gb(item.raw_size), result.get(
                column_mib('raw_capacity', item.id)), 1)
            self._assert_equal(get_nested_value(item, 'pool', 'name'),
                               result.get(column_mib('current_pool', item.id)))

            # metric
            self._assert_has_str_value(
                result.get(column_mib('response_time', item.id)))
            self._assert_has_str_value(
                result.get(column_mib('queue_length', item.id)))
            self._assert_has_str_value(
                result.get(column_mib('total_throughput', item.id)))
            self._assert_has_str_value(
                result.get(column_mib('read_throughput', item.id)))
            self._assert_has_str_value(
                result.get(column_mib('write_throughput', item.id)))
            self._assert_has_str_value(
                result.get(column_mib('total_bandwidth', item.id)))
            self._assert_has_str_value(
                result.get(column_mib('read_bandwidth', item.id)))
            self._assert_has_str_value(
                result.get(column_mib('write_bandwidth', item.id)))
            self._assert_has_str_value(
                result.get(column_mib('utilization', item.id)))

    def test_frontend_port_table_view(self):
        table_name = 'frontendPort'
        mib_name = table_name + 'Table'
        result, time_used = self._snmp_client.table_view(mib_name)
        result = {strip_type(k, FC_PORT_TYPE, ISCSI_PORT_TYPE): v for k, v in
                  result.items()}

        print('Time used for Fronend port table view: {}'.format(time_used))
        self._assert_less_equal(time_used, 30)

        items = self._unity_system.get_fc_port() + self._unity_system \
            .get_iscsi_node()

        column_mib = functools.partial(get_column_mib, table_name)
        for item in items:
            self._assert_equal(item.id, result.get(column_mib('id', item.id)))
            self._assert_equal(item.name,
                               result.get(column_mib('name', item.id)))

            address_by_snmp = result.get(column_mib('address', item.id))
            if hasattr(item, 'ethernet_port'):
                portal_lst = [portal for portal in
                              self._unity_system.get_iscsi_portal() if
                              portal.iscsi_node.name == item.name]
                for portal in portal_lst:
                    self._assert_in(portal.ip_address, address_by_snmp)

            type_by_snmp = result.get(column_mib('type', item.id))
            if hasattr(item, 'connector_type'):
                self._assert_equal(
                    get_nested_value(item, 'connector_type', 'name'),
                    type_by_snmp)
            if hasattr(item, 'ethernet_port'):
                self._assert_equal(
                    get_nested_value(item, 'ethernet_port', 'connector_type',
                                     'name'), type_by_snmp)

            current_speed_by_snmp = result.get(
                column_mib('current_speed', item.id))
            if hasattr(item, 'current_speed'):
                self._assert_equal(
                    get_nested_value(item, 'current_speed', 'name'),
                    current_speed_by_snmp)
            if hasattr(item, 'ethernet_port'):
                self._assert_equal(
                    get_nested_value(item, 'ethernet_port', 'speed', 'name'),
                    current_speed_by_snmp)

            supported_speed_by_snmp = result.get(
                column_mib('supported_speed', item.id))
            if hasattr(item, 'available_speeds'):
                speeds = item.available_speeds
                for speed in speeds:
                    self._assert_in(speed.name, supported_speed_by_snmp)
            if hasattr(item, 'ethernet_port'):
                speeds = get_nested_value(item, 'ethernet_port',
                                          'supported_speeds')
                for speed in speeds:
                    self._assert_in(speed.name, supported_speed_by_snmp)

            health_status_by_snmp = result.get(column_mib('status', item.id))
            if hasattr(item, 'ethernet_port'):
                self._assert_equal(
                    get_nested_value(item, 'ethernet_port', 'health', 'value',
                                     'name'), health_status_by_snmp)
            else:
                self._assert_equal(
                    get_nested_value(item, 'health', 'value', 'name'),
                    health_status_by_snmp)

            # metric
            self._assert_has_str_value(
                result.get(column_mib('total_throughput', item.id)))
            self._assert_has_str_value(
                result.get(column_mib('read_throughput', item.id)))
            self._assert_has_str_value(
                result.get(column_mib('write_throughput', item.id)))
            self._assert_has_str_value(
                result.get(column_mib('total_bandwidth', item.id)))
            self._assert_has_str_value(
                result.get(column_mib('read_bandwidth', item.id)))
            self._assert_has_str_value(
                result.get(column_mib('write_bandwidth', item.id)))

    def test_backend_port_table_view(self):
        table_name = 'backendPort'
        mib_name = table_name + 'Table'
        result, time_used = self._snmp_client.table_view(mib_name)

        print('Time used for Backend port table view: {}'.format(time_used))
        self._assert_less_equal(time_used, 30)

        items = self._unity_system.get_sas_port()

        column_mib = functools.partial(get_column_mib, table_name)
        for item in items:
            self._assert_equal(item.id, result.get(column_mib('id', item.id)))
            self._assert_equal(item.name,
                               result.get(column_mib('name', item.id)))
            self._assert_equal(item.connector_type.name,
                               result.get(column_mib('type', item.id)))
            self._assert_equal(str(item.port),
                               result.get(column_mib('port_number', item.id)))
            self._assert_equal(get_nested_value(item, 'current_speed', 'name'),
                               result.get(
                                   column_mib('current_speed', item.id)))
            self._assert_equal(
                get_nested_value(item, 'parent_io_module', 'name'),
                result.get(column_mib('parent_io_module', item.id)))
            self._assert_equal(
                get_nested_value(item, 'parent_storage_processor', 'name'),
                result.get(column_mib('parent_storage_processor', item.id)))
            self._assert_equal(
                get_nested_value(item, 'health', 'value', 'name'),
                result.get(column_mib('status', item.id)))

    def test_host_table_view(self):
        table_name = 'host'
        mib_name = table_name + 'Table'
        result, time_used = self._snmp_client.table_view(mib_name)

        print('Time used for Host table view: {}'.format(time_used))
        self._assert_less_equal(time_used, 60)

        items = self._unity_system.get_host()

        column_mib = functools.partial(get_column_mib, table_name)
        for item in items:
            self._assert_equal(item.id, result.get(column_mib('id', item.id)))
            self._assert_equal(item.name,
                               result.get(column_mib('name', item.id)))

            host_ip_by_snmp = result.get(
                column_mib('network_address', item.id))
            host_ip_by_storops = item.host_ip_ports
            if host_ip_by_storops:
                for host_ip in host_ip_by_storops:
                    self._assert_in(host_ip.address, host_ip_by_snmp)
            else:
                self._assert_equal(NONE_STRING, host_ip_by_snmp)

            initiators_by_snmp = result.get(column_mib('initiators', item.id))
            initiators_by_storops = []
            if hasattr(item, 'fc_host_initiators') and item \
                    .fc_host_initiators is not None:
                initiators_by_storops.extend(item.fc_host_initiators)
            if hasattr(item, 'iscsi_host_initiators') and item \
                    .iscsi_host_initiators is not None:
                initiators_by_storops.extend(item.iscsi_host_initiators)
            if initiators_by_storops:
                for initiator in initiators_by_storops:
                    self._assert_in(initiator.initiator_id, initiators_by_snmp)
            else:
                self._assert_equal(NONE_STRING, initiators_by_snmp)

            self._assert_equal(item.os_type, result.get(
                column_mib('operation_system_version', item.id)))

            host_luns_by_snmp = result.get(
                column_mib('assigned_storage_volumes', item.id))
            host_luns_by_storops = item.host_luns
            if host_luns_by_storops:
                for host_lun in host_luns_by_storops:
                    self._assert_in(get_nested_value(host_lun, 'lun', 'name'),
                                    host_luns_by_snmp)
            else:
                self._assert_equal(NONE_STRING, host_luns_by_snmp)

    def test_enclosure_table_view(self):
        table_name = 'enclosure'
        mib_name = table_name + 'Table'
        result, time_used = self._snmp_client.table_view(mib_name)
        result = {strip_type(k, DAE_TYPE, DPE_TYPE): v for k, v in
                  result.items()}

        print('Time used for Enclosure table view: {}'.format(time_used))
        self._assert_less_equal(time_used, 30)

        items = self._unity_system.get_dae() + self._unity_system.get_dpe()

        column_mib = functools.partial(get_column_mib, table_name)
        for item in items:
            self._assert_equal(item.id, result.get(column_mib('id', item.id)))
            self._assert_equal(item.name,
                               result.get(column_mib('name', item.id)))
            self._assert_equal(item.model,
                               result.get(column_mib('model', item.id)))
            self._assert_equal(item.emc_serial_number, result.get(
                column_mib('serial_number', item.id)))
            self._assert_equal(item.emc_part_number,
                               result.get(column_mib('part_number', item.id)))
            self._assert_equal(
                get_nested_value(item, 'health', 'value', 'name'),
                result.get(column_mib('health_status', item.id)))
            self._assert_equal(str(item.current_power), result.get(
                column_mib('current_power', item.id)))
            self._assert_equal(str(item.avg_power), result.get(
                column_mib('average_power', item.id)))
            self._assert_equal(str(item.max_power),
                               result.get(column_mib('max_power', item.id)))
            self._assert_equal(str(item.current_temperature), result.get(
                column_mib('current_temperature', item.id)))
            self._assert_equal(str(item.avg_temperature), result.get(
                column_mib('average_temperature', item.id)))
            self._assert_equal(str(item.max_temperature), result.get(
                column_mib('max_temperature', item.id)))

    def test_power_supply_table_view(self):
        table_name = 'powerSupply'
        mib_name = table_name + 'Table'
        result, time_used = self._snmp_client.table_view(mib_name)

        print('Time used for Power supply table view: {}'.format(time_used))
        self._assert_less_equal(time_used, 30)

        items = self._unity_system.get_power_supply()

        column_mib = functools.partial(get_column_mib, table_name)
        for item in items:
            self._assert_equal(item.id, result.get(column_mib('id', item.id)))
            self._assert_equal(item.name,
                               result.get(column_mib('name', item.id)))
            self._assert_equal(item.manufacturer,
                               result.get(column_mib('manufacturer', item.id)))
            self._assert_equal(item.model,
                               result.get(column_mib('model', item.id)))
            self._assert_equal(item.firmware_version, result.get(
                column_mib('firmware_version', item.id)))
            self._check_parent_enclosure(item, result.get(
                column_mib('parent_enclosure', item.id)))
            self._assert_equal(
                get_nested_value(item, 'storage_processor', 'name'),
                result.get(column_mib('storage_processor', item.id)))
            self._assert_equal(
                get_nested_value(item, 'health', 'value', 'name'),
                result.get(column_mib('health_status', item.id)))

    def test_fan_table_view(self):
        table_name = 'fan'
        mib_name = table_name + 'Table'
        result, time_used = self._snmp_client.table_view(mib_name)

        print('Time used for Fan table view: {}'.format(time_used))
        self._assert_less_equal(time_used, 30)

        items = self._unity_system.get_fan()

        column_mib = functools.partial(get_column_mib, table_name)
        for item in items:
            self._assert_equal(item.id, result.get(column_mib('id', item.id)))
            self._assert_equal(item.name,
                               result.get(column_mib('name', item.id)))
            self._assert_equal(str(item.slot_number),
                               result.get(column_mib('slot_number', item.id)))
            self._check_parent_enclosure(item, result.get(
                column_mib('parent_enclosure', item.id)))
            self._assert_equal(
                get_nested_value(item, 'health', 'value', 'name'),
                result.get(column_mib('health_status', item.id)))

    def test_bbu_table_view(self):
        table_name = 'bbu'
        mib_name = table_name + 'Table'
        result, time_used = self._snmp_client.table_view(mib_name)

        print('Time used for Bbu table view: {}'.format(time_used))
        self._assert_less_equal(time_used, 30)

        items = self._unity_system.get_battery()

        column_mib = functools.partial(get_column_mib, table_name)
        for item in items:
            self._assert_equal(item.id, result.get(column_mib('id', item.id)))
            self._assert_equal(item.name,
                               result.get(column_mib('name', item.id)))
            self._assert_equal(item.manufacturer,
                               result.get(column_mib('manufacturer', item.id)))
            self._assert_equal(item.model,
                               result.get(column_mib('model', item.id)))
            self._assert_equal(item.firmware_version,
                               result.get(
                                   column_mib('firmware_version', item.id)))
            self._assert_equal(
                get_nested_value(item, 'parent_storage_processor', 'name'),
                result.get(column_mib('parent_storage_processor', item.id)))
            self._assert_equal(
                get_nested_value(item, 'health', 'value', 'name'),
                result.get(column_mib('health_status', item.id)))
