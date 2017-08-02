import unittest

import ddt
import mock
from snmpagent import clients
from snmpagent.tests import mocks


@ddt.ddt
class TestUnityClient(unittest.TestCase):
    # @mock.patch(target='storops.UnitySystem',
    #             new=mocks.MockUnitySystem)
    @mock.patch(target='snmpagent.clients.storops.UnitySystem',
                new=mocks.MockUnitySystem)
    def setUp(self):
        self.client = clients.UnityClient()

    # system
    def test_get_agent_version(self):
        self.assertEqual('1.0', self.client.get_agent_version())

    def test_get_mib_version(self):
        self.assertEqual('1.0', self.client.get_mib_version())

    def test_get_manufacturer(self):
        self.assertEqual('DellEMC', self.client.get_manufacturer())

    def test_system_model(self):
        self.assertEqual('Unity 500', self.client.get_model())

    def test_get_serial_number(self):
        self.assertEqual('FNM00150600267', self.client.get_serial_number())

    def test_get_operation_environment_version(self):
        self.assertEqual('4.2.0',
                         self.client.get_operation_environment_version())

    def test_get_mgmt_ip(self):
        self.assertEqual('10.10.10.10, 10.10.10.11', self.client.get_mgmt_ip())

    def test_get_current_power(self):
        self.assertEqual('542', self.client.get_current_power())

    def test_get_avg_power(self):
        self.assertEqual('540', self.client.get_avg_power())

    def test_get_number_of_sp(self):
        self.assertEqual(2, self.client.get_number_of_sp())

    def test_get_number_of_enclosure(self):
        self.assertEqual(4, self.client.get_number_of_enclosure())

    def test_get_number_of_power_supply(self):
        self.assertEqual(4, self.client.get_number_of_power_supply())

    def test_get_number_of_fan(self):
        self.assertEqual(10, self.client.get_number_of_fan())

    def test_get_number_of_disk(self):
        self.assertEqual(2, self.client.get_number_of_disk())

    def test_get_number_of_frontend_port(self):
        self.assertEqual(4, self.client.get_number_of_frontend_port())

    def test_get_number_of_backend_port(self):
        self.assertEqual(2, self.client.get_number_of_backend_port())

    def test_get_total_capacity(self):
        self.assertEqual('10000', self.client.get_total_capacity())

    def test_get_used_capacity(self):
        self.assertEqual('3000', self.client.get_used_capacity())

    def test_get_free_capacity(self):
        self.assertEqual('7000', self.client.get_free_capacity())

    def test_get_total_iops(self):
        self.assertEqual('0.53', self.client.get_total_iops())

    def test_get_read_iops(self):
        self.assertEqual('0.13', self.client.get_read_iops())

    def test_get_write_iops(self):
        self.assertEqual('0.4', self.client.get_write_iops())

    def test_get_total_byte_rate(self):
        self.assertEqual('2.74', self.client.get_total_byte_rate())

    def test_get_read_byte_rate(self):
        self.assertEqual('0.18', self.client.get_read_byte_rate())

    def test_get_write_byte_rate(self):
        self.assertEqual('2.56', self.client.get_write_byte_rate())

    # storageProcessorTable
    def test_get_sps(self):
        items = self.client.get_sps()
        self.assertEqual(2, len(items))
        self.assertEqual({'SP A', 'SP B'}, set(items))

    @ddt.data({'key': 'SP A', 'emc_serial_number': 'CF2HF144300003'},
              {'key': 'SP B', 'emc_serial_number': 'CF2HF144600021'}, )
    def test_get_sp_serial_number(self, param_dict):
        self.assertEqual(param_dict['emc_serial_number'],
                         self.client.get_sp_serial_number(param_dict['key']))

    @ddt.data({'key': 'SP A', 'health': 'OK'},
              {'key': 'SP B', 'health': 'OK'}, )
    def test_get_sp_health_status(self, param_dict):
        self.assertEqual(param_dict['health'],
                         self.client.get_sp_health_status(param_dict['key']))

    @ddt.data({'key': 'SP A', 'utilization': '2.62'},
              {'key': 'SP B', 'utilization': '29.03'}, )
    def test_get_sp_utilization(self, param_dict):
        self.assertEqual(param_dict['utilization'],
                         self.client.get_sp_utilization(param_dict['key']))

    @ddt.data({'key': 'SP A', 'block_total_iops': '0.53'},
              {'key': 'SP B', 'block_total_iops': '0'}, )
    def test_get_sp_block_total_iops(self, param_dict):
        self.assertEqual(param_dict['block_total_iops'],
                         self.client.get_sp_block_total_iops(
                             param_dict['key']))

    @ddt.data({'key': 'SP A', 'block_read_iops': '0.13'},
              {'key': 'SP B', 'block_read_iops': '0'}, )
    def test_get_sp_block_read_iops(self, param_dict):
        self.assertEqual(param_dict['block_read_iops'],
                         self.client.get_sp_block_read_iops(
                             param_dict['key']))

    @ddt.data({'key': 'SP A', 'block_write_iops': '0.4'},
              {'key': 'SP B', 'block_write_iops': '0'}, )
    def test_get_sp_block_write_iops(self, param_dict):
        self.assertEqual(param_dict['block_write_iops'],
                         self.client.get_sp_block_write_iops(
                             param_dict['key']))

    @ddt.data({'key': 'SP A', 'total_byte_rate': '2756.26'},
              {'key': 'SP B', 'total_byte_rate': '0'}, )
    def test_get_sp_total_byte_rate(self, param_dict):
        self.assertEqual(param_dict['total_byte_rate'],
                         self.client.get_sp_total_byte_rate(
                             param_dict['key']))

    @ddt.data({'key': 'SP A', 'read_byte_rate': '187.73'},
              {'key': 'SP B', 'read_byte_rate': '0'}, )
    def test_get_sp_read_byte_rate(self, param_dict):
        self.assertEqual(param_dict['read_byte_rate'],
                         self.client.get_sp_read_byte_rate(param_dict['key']))

    @ddt.data({'key': 'SP A', 'write_byte_rate': '2568.53'},
              {'key': 'SP B', 'write_byte_rate': '0'}, )
    def test_get_sp_write_byte_rate(self, param_dict):
        self.assertEqual(param_dict['write_byte_rate'],
                         self.client.get_sp_write_byte_rate(
                             param_dict['key']))

    @ddt.data({'key': 'SP A', 'block_cache_dirty_size': '65'},
              {'key': 'SP B', 'block_cache_dirty_size': '92'}, )
    def test_get_sp_cache_dirty_size(self, param_dict):
        self.assertEqual(param_dict['block_cache_dirty_size'],
                         self.client.get_sp_cache_dirty_size(
                             param_dict['key']))

    @ddt.data({'key': 'SP A', 'block_cache_read_hit_ratio': '100.53'},
              {'key': 'SP B', 'block_cache_read_hit_ratio': '100.00'}, )
    def test_get_sp_block_cache_read_hit_ratio(self, param_dict):
        self.assertEqual(param_dict['block_cache_read_hit_ratio'],
                         self.client.get_sp_block_cache_read_hit_ratio(
                             param_dict['key']))

    @ddt.data({'key': 'SP A', 'block_cache_write_hit_ratio': '81.96'},
              {'key': 'SP B', 'block_cache_write_hit_ratio': '38.02'}, )
    def test_get_sp_block_cache_write_hit_ratio(self, param_dict):
        self.assertEqual(param_dict['block_cache_write_hit_ratio'],
                         self.client.get_sp_block_cache_write_hit_ratio(
                             param_dict['key']))

    # poolTable
    def test_get_pools(self):
        items = self.client.get_pools()
        self.assertEqual(2, len(items))
        self.assertEqual({'Beijing', 'Shanghai'}, set(items))

    @ddt.data({'key': 'Beijing', 'tiers': 'Extreme Performance, Performance, Capacity'},
              {'key': 'Shanghai', 'tiers': 'Extreme Performance, Performance'}, )
    def test_get_pool_disk_types(self, param_dict):
        self.assertEqual(param_dict['tiers'],
                         self.client.get_pool_disk_types(param_dict['key']))

    @ddt.data({'key': 'Beijing', 'raid_type': 'RAID10'},
              {'key': 'Shanghai', 'raid_type': 'RAID5'}, )
    def test_get_pool_raid_levels(self, param_dict):
        self.assertEqual(param_dict['raid_type'],
                         self.client.get_pool_raid_levels(param_dict['key']))

    @ddt.data({'key': 'Beijing', 'is_fast_cache_enabled': 'True'},
              {'key': 'Shanghai', 'is_fast_cache_enabled': 'False'}, )
    def test_get_pool_fast_cache_status(self, param_dict):
        self.assertEqual(param_dict['is_fast_cache_enabled'],
                         self.client.get_pool_fast_cache_status(param_dict['key']))

    @ddt.data({'key': 'Beijing', 'disk_count': 30},
              {'key': 'Shanghai', 'disk_count': 20}, )
    def test_get_pool_number_of_disk(self, param_dict):
        self.assertEqual(param_dict['disk_count'],
                         self.client.get_pool_number_of_disk(param_dict['key']))

    @ddt.data({'key': 'Beijing', 'size_total': '3000.00'},
              {'key': 'Shanghai', 'size_total': '3000.00'}, )
    def test_get_pool_size_total(self, param_dict):
        self.assertEqual(param_dict['size_total'],
                         self.client.get_pool_size_total(param_dict['key']))

    @ddt.data({'key': 'Beijing', 'size_free': '1000.00'},
              {'key': 'Shanghai', 'size_free': '2000.00'}, )
    def test_get_pool_size_free(self, param_dict):
        self.assertEqual(param_dict['size_free'],
                         self.client.get_pool_size_free(param_dict['key']))

    @ddt.data({'key': 'Beijing', 'size_used': '2000.00'},
              {'key': 'Shanghai', 'size_used': '1000.00'}, )
    def test_get_pool_size_used(self, param_dict):
        self.assertEqual(param_dict['size_used'],
                         self.client.get_pool_size_used(param_dict['key']))

    @ddt.data({'key': 'Beijing', 'size_ultilization': '33.33'},
              {'key': 'Shanghai', 'size_ultilization': '66.66'}, )
    def test_get_pool_size_ultilization(self, param_dict):
        self.assertEqual(param_dict['size_ultilization'],
                         self.client.get_pool_size_ultilization(param_dict['key']))

    # volumeTable
    def test_get_luns(self):
        items = self.client.get_luns()
        self.assertEqual(2, len(items))
        self.assertEqual({'sv_1', 'sv_2'}, set(items))

    @ddt.data({'key': 'sv_1', 'name': 'Yangpu'},
              {'key': 'sv_2', 'name': "Jing'an"}, )
    def test_get_lun_name(self, param_dict):
        self.assertEqual(param_dict['name'],
                         self.client.get_lun_name(param_dict['key']))

    @ddt.data({'key': 'sv_1', 'raid_type': 'RAID10'},
              {'key': 'sv_2', 'raid_type': ""}, )
    def test_get_lun_raid_type(self, param_dict):
        self.assertEqual(param_dict['raid_type'],
                         self.client.get_lun_raid_type(param_dict['key']))

    @ddt.data({'key': 'sv_1', 'size_allocated': '81.92'},
              {'key': 'sv_2', 'size_allocated': '0'}, )
    def test_get_lun_size_allocated(self, param_dict):
        self.assertEqual(param_dict['size_allocated'],
                         self.client.get_lun_size_allocated(param_dict['key']))

    @ddt.data({'key': 'sv_1', 'size_total': '107.37400'},
              {'key': 'sv_2', 'size_total': '0'}, )
    def test_get_lun_size_total(self, param_dict):
        self.assertEqual(param_dict['size_total'],
                         self.client.get_lun_size_total(param_dict['key']))

    @ddt.data({'key': 'sv_1', 'health': 'OK'},
              {'key': 'sv_2', 'health': 'OK BUT'}, )
    def test_get_lun_health_status(self, param_dict):
        self.assertEqual(param_dict['health'],
                         self.client.get_lun_health_status(param_dict['key']))

    @ddt.data({'key': 'sv_1', 'is_fast_cache_enabled': 'False'},
              {'key': 'sv_2', 'is_fast_cache_enabled': 'True'}, )
    def test_get_lun_fast_cache_status(self, param_dict):
        self.assertEqual(param_dict['is_fast_cache_enabled'],
                         self.client.get_lun_fast_cache_status(param_dict['key']))

    @ddt.data({'key': 'sv_1', 'default_node': 'SP B'},
              {'key': 'sv_2', 'default_node': 'SP A'}, )
    def test_get_lun_default_sp(self, param_dict):
        self.assertEqual(param_dict['default_node'],
                         self.client.get_lun_default_sp(param_dict['key']))

    @ddt.data({'key': 'sv_1', 'current_node': 'SP A'},
              {'key': 'sv_2', 'current_node': 'SP B'}, )
    def test_get_lun_current_sp(self, param_dict):
        self.assertEqual(param_dict['current_node'],
                         self.client.get_lun_current_sp(param_dict['key']))

    @ddt.data({'key': 'sv_1', 'response_time': '5079.65'},
              {'key': 'sv_2', 'response_time': '0'}, )
    def test_get_lun_response_time(self, param_dict):
        self.assertEqual(param_dict['response_time'],
                         self.client.get_lun_response_time(param_dict['key']))

    @ddt.data({'key': 'sv_1', 'queue_length': '0.01'},
              {'key': 'sv_2', 'queue_length': '0'}, )
    def test_get_lun_queue_length(self, param_dict):
        self.assertEqual(param_dict['queue_length'],
                         self.client.get_lun_queue_length(param_dict['key']))

    @ddt.data({'key': 'sv_1', 'total_iops': '0.43'},
              {'key': 'sv_2', 'total_iops': '0'}, )
    def test_get_lun_total_iops(self, param_dict):
        self.assertEqual(param_dict['total_iops'],
                         self.client.get_lun_total_iops(param_dict['key']))

    @ddt.data({'key': 'sv_1', 'read_iops': '0.03'},
              {'key': 'sv_2', 'read_iops': '0'}, )
    def test_get_lun_read_iops(self, param_dict):
        self.assertEqual(param_dict['read_iops'],
                         self.client.get_lun_read_iops(param_dict['key']))

    @ddt.data({'key': 'sv_1', 'write_iops': '0.40'},
              {'key': 'sv_2', 'write_iops': '0'}, )
    def test_get_lun_write_iops(self, param_dict):
        self.assertEqual(param_dict['write_iops'],
                         self.client.get_lun_write_iops(param_dict['key']))

    @ddt.data({'key': 'sv_1', 'total_byte_rate': '2705.06'},
              {'key': 'sv_2', 'total_byte_rate': '0'}, )
    def test_get_lun_total_byte_rate(self, param_dict):
        self.assertEqual(param_dict['total_byte_rate'],
                         self.client.get_lun_total_byte_rate(param_dict['key']))

    @ddt.data({'key': 'sv_1', 'read_byte_rate': '136.53'},
              {'key': 'sv_2', 'read_byte_rate': '0'}, )
    def test_get_lun_read_byte_rate(self, param_dict):
        self.assertEqual(param_dict['read_byte_rate'],
                         self.client.get_lun_read_byte_rate(param_dict['key']))

    @ddt.data({'key': 'sv_1', 'write_byte_rate': '2568.53'},
              {'key': 'sv_2', 'write_byte_rate': '0'}, )
    def test_get_lun_write_byte_rate(self, param_dict):
        self.assertEqual(param_dict['write_byte_rate'],
                         self.client.get_lun_write_byte_rate(param_dict['key']))

    @ddt.data({'key': 'sv_1', 'fast_cache_read_hits': '30.00'},
              {'key': 'sv_2', 'fast_cache_read_hits': '0'}, )
    def test_get_lun_fast_cache_read_hits(self, param_dict):
        self.assertEqual(param_dict['fast_cache_read_hits'],
                         self.client.get_lun_fast_cache_read_hits(param_dict['key']))

    @ddt.data({'key': 'sv_1', 'fast_cache_write_hits': '30.00'},
              {'key': 'sv_2', 'fast_cache_write_hits': '0'}, )
    def test_get_lun_fast_cache_write_hits(self, param_dict):
        self.assertEqual(param_dict['fast_cache_write_hits'],
                         self.client.get_lun_fast_cache_write_hits(param_dict['key']))

    @ddt.data({'key': 'sv_1', 'fast_cache_read_hit_rate': '30.00'},
              {'key': 'sv_2', 'fast_cache_read_hit_rate': '0'}, )
    def test_get_lun_fast_cache_read_hit_rate(self, param_dict):
        self.assertEqual(param_dict['fast_cache_read_hit_rate'],
                         self.client.get_lun_fast_cache_read_hit_rate(param_dict['key']))

    @ddt.data({'key': 'sv_1', 'fast_cache_write_hit_rate': '30.00'},
              {'key': 'sv_2', 'fast_cache_write_hit_rate': '0'}, )
    def test_get_lun_fast_cache_write_hit_rate(self, param_dict):
        self.assertEqual(param_dict['fast_cache_write_hit_rate'],
                         self.client.get_lun_fast_cache_write_hit_rate(param_dict['key']))

    @ddt.data({'key': 'sv_1', 'utilization': '0.08'},
              {'key': 'sv_2', 'utilization': '0'}, )
    def test_get_lun_utilization(self, param_dict):
        self.assertEqual(param_dict['utilization'],
                         self.client.get_lun_utilization(param_dict['key']))

    @ddt.data({'key': 'sv_1', 'host_access': 'ESD-HOST193221.meng.lab.emc.com, 10.245.54.151, VPI25224'},
              {'key': 'sv_2', 'host_access': ''}, )
    def test_get_lun_host_access(self, param_dict):
        self.assertEqual(param_dict['host_access'],
                         self.client.get_lun_host_access(param_dict['key']))

    # diskTable
    def test_get_disks(self):
        items = self.client.get_disks()
        self.assertEqual(2, len(items))
        self.assertEqual({'DPE Drive 0', 'DAE 0 1 Drive 0'}, set(items))

    @ddt.data({'key': 'DPE Drive 0', 'mdoel': 'HU415606 EMC600'},
              {'key': 'DAE 0 1 Drive 0', 'mdoel': 'ST2000NK EMC2000'}, )
    def test_get_disk_model(self, param_dict):
        self.assertEqual(param_dict['model'],
                         self.client.get_disk_model(param_dict['key']))

    @ddt.data({'key': 'DPE Drive 0', 'emc_serial_number': '0XG507BJ'},
              {'key': 'DAE 0 1 Drive 0', 'emc_serial_number': 'Z4H027TW'}, )
    def test_get_disk_serial_number(self, param_dict):
        self.assertEqual(param_dict['emc_serial_number'],
                         self.client.get_disk_serial_number(param_dict['key']))

    @ddt.data({'key': 'DPE Drive 0', 'version': 'K7P0'},
              {'key': 'DAE 0 1 Drive 0', 'version': 'MN16'}, )
    def test_get_disk_version(self, param_dict):
        self.assertEqual(param_dict['version'],
                         self.client.get_disk_version(param_dict['key']))

    @ddt.data({'key': 'DPE Drive 0', 'disk_technology': 'SAS'},
              {'key': 'DAE 0 1 Drive 0', 'disk_technology': 'NL_SAS'}, )
    def test_get_disk_type(self, param_dict):
        self.assertEqual(param_dict['disk_technology'],
                         self.client.get_disk_type(param_dict['key']))

    @ddt.data({'key': 'DPE Drive 0', 'slot_number': '0'},
              {'key': 'DAE 0 1 Drive 0', 'slot_number': '1'}, )
    def test_get_disk_slot_number(self, param_dict):
        self.assertEqual(param_dict['slot_number'],
                         self.client.get_disk_slot_number(param_dict['key']))

    @ddt.data({'key': 'DPE Drive 0', 'health': 'OK'},
              {'key': 'DAE 0 1 Drive 0', 'health': 'MAJOR'}, )
    def test_get_disk_health_status(self, param_dict):
        self.assertEqual(param_dict['health'],
                         self.client.get_disk_health_status(param_dict['key']))

    @ddt.data({'key': 'DPE Drive 0', 'raw_size': '590.89'},
              {'key': 'DAE 0 1 Drive 0', 'raw_size': '0'}, )
    def test_get_disk_raw_size(self, param_dict):
        self.assertEqual(param_dict['raw_size'],
                         self.client.get_disk_raw_size(param_dict['key']))

    @ddt.data({'key': 'DPE Drive 0', 'pool': ''},
              {'key': 'DAE 0 1 Drive 0', 'pool': 'Shanghai'}, )
    def test_get_disk_current_pool(self, param_dict):
        self.assertEqual(param_dict['pool'],
                         self.client.get_disk_current_pool(param_dict['key']))

    @ddt.data({'key': 'DPE Drive 0', 'response_time': '35337.37'},
              {'key': 'DAE 0 1 Drive 0', 'response_time': '0'}, )
    def test_get_disk_response_time(self, param_dict):
        self.assertEqual(param_dict['response_time'],
                         self.client.get_disk_response_time(param_dict['key']))

    @ddt.data({'key': 'DPE Drive 0', 'queue_length': '1.21'},
              {'key': 'DAE 0 1 Drive 0', 'queue_length': '1.21'}, )
    def test_get_disk_queue_length(self, param_dict):
        self.assertEqual(param_dict['queue_length'],
                         self.client.get_disk_queue_length(param_dict['key']))

    @ddt.data({'key': 'DPE Drive 0', 'total_iops': '2.20'},
              {'key': 'DAE 0 1 Drive 0', 'total_iops': '0'}, )
    def test_get_disk_total_iops(self, param_dict):
        self.assertEqual(param_dict['total_iops'],
                         self.client.get_disk_total_iops(param_dict['key']))

    @ddt.data({'key': 'DPE Drive 0', 'read_iops': '1.41'},
              {'key': 'DAE 0 1 Drive 0', 'read_iops': '0'}, )
    def test_get_disk_read_iops(self, param_dict):
        self.assertEqual(param_dict['read_iops'],
                         self.client.get_disk_read_iops(param_dict['key']))

    @ddt.data({'key': 'DPE Drive 0', 'write_iops': '0.78'},
              {'key': 'DAE 0 1 Drive 0', 'write_iops': '0'}, )
    def test_get_disk_write_iops(self, param_dict):
        self.assertEqual(param_dict['write_iops'],
                         self.client.get_disk_write_iops(param_dict['key']))

    @ddt.data({'key': 'DPE Drive 0', 'total_byte_rate': '1330312.53'},
              {'key': 'DAE 0 1 Drive 0', 'total_byte_rate': '0'}, )
    def test_get_disk_total_byte_rate(self, param_dict):
        self.assertEqual(param_dict['total_byte_rate'],
                         self.client.get_disk_total_byte_rate(param_dict['key']))

    @ddt.data({'key': 'DPE Drive 0', 'read_byte_rate': '1123601.06'},
              {'key': 'DAE 0 1 Drive 0', 'read_byte_rate': '0'}, )
    def test_get_disk_read_byte_rate(self, param_dict):
        self.assertEqual(param_dict['read_byte_rate'],
                         self.client.get_disk_read_byte_rate(param_dict['key']))

    @ddt.data({'key': 'DPE Drive 0', 'write_byte_rate': '206711.46'},
              {'key': 'DAE 0 1 Drive 0', 'write_byte_rate': '0'}, )
    def test_get_disk_write_byte_rate(self, param_dict):
        self.assertEqual(param_dict['write_byte_rate'],
                         self.client.get_disk_write_byte_rate(param_dict['key']))

    @ddt.data({'key': 'DPE Drive 0', 'utilization': '22.45'},
              {'key': 'DAE 0 1 Drive 0', 'utilization': '0'}, )
    def test_get_disk_utilization(self, param_dict):
        self.assertEqual(param_dict['utilization'],
                         self.client.get_disk_utilization(param_dict['key']))

    # # frontendPortTable
    # def test_get_frontend_ports(self):
    #     items = self.client.get_frontend_ports()
    #     self.assertEqual(4, len(items))
    #     # self.assertEqual({'spa_fc4', 'spb_fc4', 'iscsinode_spa_eth2', 'iscsinode_spb_eth2'}, set(items))
    # 
    # @ddt.data({'key': 'spa_fc4', 'id': 'spa_fc4'},
    #           {'key': 'iscsinode_spa_eth2', 'id': 'iscsinode_spa_eth2'}, )
    # def test_get_frontend_port_id(self, param_dict):
    #     self.assertEqual(param_dict['id'],
    #                      self.client.get_frontend_port_id(param_dict['key']))

    # def test_get_frontend_port_name(self, param_dict):
    #     self.assertEqual(param_dict['name'],
    #                      self.client.get_frontend_port_name(param_dict['key']))
    #
    # def test_get_frontend_port_address(self, param_dict):
    #     self.assertEqual(param_dict['address'],
    #                      self.client.get_frontend_port_address(param_dict['key']))
    #
    # def test_get_frontend_port_type(self, param_dict):
    #     self.assertEqual(param_dict['port_type'],
    #                      self.client.get_frontend_port_type(param_dict['key']))
    #
    # def test_get_frontend_port_current_speed(self, param_dict):
    #     self.assertEqual(param_dict['current_speed'],
    #                      self.client.get_frontend_port_current_speed(param_dict['key']))
    #
    # def test_get_frontend_port_supported_speed(self, param_dict):
    #     self.assertEqual(param_dict['support_speed'],
    #                      self.client.get_frontend_port_supported_speed(param_dict['key']))
    #
    # def test_get_frontend_port_health_status(self, param_dict):
    #     self.assertEqual(param_dict['health'],
    #                      self.client.get_frontend_port_health_status(param_dict['key']))
    #
    # def test_get_frontend_port_total_iops(self, param_dict):
    #     self.assertEqual(param_dict['total_iops'],
    #                      self.client.get_frontend_port_total_iops(param_dict['key']))
    #
    # def test_get_frontend_port_read_iops(self, param_dict):
    #     self.assertEqual(param_dict['read_iops'],
    #                      self.client.get_frontend_port_read_iops(param_dict['key']))
    #
    # def test_get_frontend_port_write_iops(self, param_dict):
    #     self.assertEqual(param_dict['write_iops'],
    #                      self.client.get_frontend_port_write_iops(param_dict['key']))
    #
    # def test_get_frontend_port_total_byte_rate(self, param_dict):
    #     self.assertEqual(param_dict['total_byte_rate'],
    #                      self.client.get_frontend_port_total_byte_rate(param_dict['key']))
    #
    # def test_get_frontend_port_read_byte_rate(self, param_dict):
    #     self.assertEqual(param_dict['read_byte_rate'],
    #                      self.client.get_frontend_port_read_byte_rate(param_dict['key']))
    #
    # def test_get_frontend_port_write_byte_rate(self, param_dict):
    #     self.assertEqual(param_dict['write_byte_rate'],
    #                      self.client.get_frontend_port_write_byte_rate(param_dict['key']))