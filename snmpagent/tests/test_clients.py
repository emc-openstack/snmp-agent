import unittest

import ddt
from snmpagent import clients
from snmpagent.tests import patches

NONE_STRING = 'n/a'


@ddt.ddt
class TestUnityClient(unittest.TestCase):
    @patches.unity_system
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
        self.assertEqual(3, self.client.get_number_of_sp())

    def test_get_number_of_enclosure(self):
        self.assertEqual(4, self.client.get_number_of_enclosure())

    def test_get_number_of_power_supply(self):
        self.assertEqual(2, self.client.get_number_of_power_supply())

    def test_get_number_of_fan(self):
        self.assertEqual(4, self.client.get_number_of_fan())

    def test_get_number_of_disk(self):
        self.assertEqual(4, self.client.get_number_of_disk())

    def test_get_number_of_frontend_port(self):
        self.assertEqual(4, self.client.get_number_of_frontend_port())

    def test_get_number_of_backend_port(self):
        self.assertEqual(2, self.client.get_number_of_backend_port())

    def test_get_total_capacity(self):
        self.assertEqual('10240.0', self.client.get_total_capacity())

    def test_get_used_capacity(self):
        self.assertEqual('3072.0', self.client.get_used_capacity())

    def test_get_free_capacity(self):
        self.assertEqual('7168.0', self.client.get_free_capacity())

    def test_get_total_iops(self):
        self.assertEqual('0.533', self.client.get_total_iops())

    def test_get_read_iops(self):
        self.assertEqual('0.133', self.client.get_read_iops())

    def test_get_write_iops(self):
        self.assertEqual('0.4', self.client.get_write_iops())

    def test_get_total_byte_rate(self):
        self.assertEqual('2.628', self.client.get_total_byte_rate())

    def test_get_read_byte_rate(self):
        self.assertEqual('0.178', self.client.get_read_byte_rate())

    def test_get_write_byte_rate(self):
        self.assertEqual('2.449', self.client.get_write_byte_rate())

    # storageProcessorTable
    def test_get_sps(self):
        items = self.client.get_sps()
        self.assertEqual(3, len(items))
        self.assertEqual({'spa', 'spb', 'spc'}, set(items))

    @ddt.data({'key': 'spa', 'name': 'SP A'},
              {'key': 'spb', 'name': NONE_STRING}, )
    def test_get_sp_name(self, param_dict):
        self.assertEqual(param_dict['name'],
                         self.client.get_sp_name(param_dict['key']))

    @ddt.data({'key': 'spa', 'emc_serial_number': 'CF2HF144300003'},
              {'key': 'spb', 'emc_serial_number': NONE_STRING}, )
    def test_get_sp_serial_number(self, param_dict):
        self.assertEqual(param_dict['emc_serial_number'],
                         self.client.get_sp_serial_number(param_dict['key']))

    @ddt.data({'key': 'spa', 'health': 'OK'},
              {'key': 'spb', 'health': NONE_STRING},
              {'key': 'spc', 'health': NONE_STRING}, )
    def test_get_sp_health_status(self, param_dict):
        self.assertEqual(param_dict['health'],
                         self.client.get_sp_health_status(param_dict['key']))

    @ddt.data({'key': 'spa', 'utilization': '2.629'},
              {'key': 'spb', 'utilization': '0'},
              {'key': 'spc', 'utilization': '0'}, )
    def test_get_sp_utilization(self, param_dict):
        self.assertEqual(param_dict['utilization'],
                         self.client.get_sp_utilization(param_dict['key']))

    @ddt.data({'key': 'spa', 'block_total_iops': '0.533'},
              {'key': 'spb', 'block_total_iops': '0'},
              {'key': 'spc', 'block_total_iops': '0'}, )
    def test_get_sp_block_total_iops(self, param_dict):
        self.assertEqual(param_dict['block_total_iops'],
                         self.client.get_sp_block_total_iops(
                             param_dict['key']))

    @ddt.data({'key': 'spa', 'block_read_iops': '0.133'},
              {'key': 'spb', 'block_read_iops': '0'},
              {'key': 'spc', 'block_read_iops': '0'}, )
    def test_get_sp_block_read_iops(self, param_dict):
        self.assertEqual(param_dict['block_read_iops'],
                         self.client.get_sp_block_read_iops(
                             param_dict['key']))

    @ddt.data({'key': 'spa', 'block_write_iops': '0.4'},
              {'key': 'spb', 'block_write_iops': '0'},
              {'key': 'spc', 'block_write_iops': '0'}, )
    def test_get_sp_block_write_iops(self, param_dict):
        self.assertEqual(param_dict['block_write_iops'],
                         self.client.get_sp_block_write_iops(
                             param_dict['key']))

    @ddt.data({'key': 'spa', 'total_byte_rate': '2.628'},
              {'key': 'spb', 'total_byte_rate': '0'},
              {'key': 'spc', 'total_byte_rate': '0'}, )
    def test_get_sp_total_byte_rate(self, param_dict):
        self.assertEqual(param_dict['total_byte_rate'],
                         self.client.get_sp_total_byte_rate(
                             param_dict['key']))

    @ddt.data({'key': 'spa', 'read_byte_rate': '0.178'},
              {'key': 'spb', 'read_byte_rate': '0'},
              {'key': 'spc', 'read_byte_rate': '0'}, )
    def test_get_sp_read_byte_rate(self, param_dict):
        self.assertEqual(param_dict['read_byte_rate'],
                         self.client.get_sp_read_byte_rate(param_dict['key']))

    @ddt.data({'key': 'spa', 'write_byte_rate': '2.449'},
              {'key': 'spb', 'write_byte_rate': '0'},
              {'key': 'spc', 'write_byte_rate': '0'}, )
    def test_get_sp_write_byte_rate(self, param_dict):
        self.assertEqual(param_dict['write_byte_rate'],
                         self.client.get_sp_write_byte_rate(
                             param_dict['key']))

    @ddt.data({'key': 'spa', 'block_cache_dirty_size': '65'},
              {'key': 'spb', 'block_cache_dirty_size': '0'},
              {'key': 'spc', 'block_cache_dirty_size': '0'}, )
    def test_get_sp_cache_dirty_size(self, param_dict):
        self.assertEqual(param_dict['block_cache_dirty_size'],
                         self.client.get_sp_cache_dirty_size(
                             param_dict['key']))

    @ddt.data({'key': 'spa', 'block_cache_read_hit_ratio': '100.533'},
              {'key': 'spb', 'block_cache_read_hit_ratio': '0'},
              {'key': 'spc', 'block_cache_read_hit_ratio': '0'}, )
    def test_get_sp_block_cache_read_hit_ratio(self, param_dict):
        self.assertEqual(param_dict['block_cache_read_hit_ratio'],
                         self.client.get_sp_block_cache_read_hit_ratio(
                             param_dict['key']))

    @ddt.data({'key': 'spa', 'block_cache_write_hit_ratio': '81.967'},
              {'key': 'spb', 'block_cache_write_hit_ratio': '0'},
              {'key': 'spc', 'block_cache_write_hit_ratio': '0'}, )
    def test_get_sp_block_cache_write_hit_ratio(self, param_dict):
        self.assertEqual(param_dict['block_cache_write_hit_ratio'],
                         self.client.get_sp_block_cache_write_hit_ratio(
                             param_dict['key']))

    # poolTable
    def test_get_pools(self):
        items = self.client.get_pools()
        self.assertEqual(3, len(items))
        self.assertEqual({'pool_1', 'pool_2', 'pool_3'}, set(items))

    @ddt.data({'key': 'pool_1', 'name': 'Beijing'},
              {'key': 'pool_2', 'name': NONE_STRING}, )
    def test_get_pool_name(self, param_dict):
        self.assertEqual(param_dict['name'],
                         self.client.get_pool_name(param_dict['key']))

    @ddt.data({'key': 'pool_1',
               'tiers': 'Extreme Performance, Performance, Capacity'},
              {'key': 'pool_2', 'tiers': NONE_STRING}, )
    def test_get_pool_disk_types(self, param_dict):
        self.assertEqual(param_dict['tiers'],
                         self.client.get_pool_disk_types(param_dict['key']))

    @ddt.data({'key': 'pool_1', 'raid_type': 'RAID10'},
              {'key': 'pool_2', 'raid_type': NONE_STRING}, )
    def test_get_pool_raid_levels(self, param_dict):
        self.assertEqual(param_dict['raid_type'],
                         self.client.get_pool_raid_levels(param_dict['key']))

    @ddt.data({'key': 'pool_1', 'is_fast_cache_enabled': 'True'},
              {'key': 'pool_2', 'is_fast_cache_enabled': NONE_STRING}, )
    def test_get_pool_fast_cache_status(self, param_dict):
        self.assertEqual(param_dict['is_fast_cache_enabled'],
                         self.client.get_pool_fast_cache_status(
                             param_dict['key']))

    # TODO:
    @ddt.data({'key': 'pool_1', 'disk_count': '30'},
              {'key': 'pool_2', 'disk_count': '0'}, )
    def test_get_pool_number_of_disk(self, param_dict):
        self.assertEqual(param_dict['disk_count'],
                         self.client.get_pool_number_of_disk(
                             param_dict['key']))

    @ddt.data({'key': 'pool_1', 'size_total': '2793.968'},
              {'key': 'pool_2', 'size_total': '0'}, )
    def test_get_pool_size_total(self, param_dict):
        self.assertEqual(param_dict['size_total'],
                         self.client.get_pool_size_total(param_dict['key']))

    @ddt.data({'key': 'pool_1', 'size_free': '931.323'},
              {'key': 'pool_2', 'size_free': '0'}, )
    def test_get_pool_size_free(self, param_dict):
        self.assertEqual(param_dict['size_free'],
                         self.client.get_pool_size_free(param_dict['key']))

    @ddt.data({'key': 'pool_1', 'size_used': '1862.645'},
              {'key': 'pool_2', 'size_used': '0'}, )
    def test_get_pool_size_used(self, param_dict):
        self.assertEqual(param_dict['size_used'],
                         self.client.get_pool_size_used(param_dict['key']))

    @ddt.data({'key': 'pool_1', 'size_ultilization': '0.667'},
              {'key': 'pool_2', 'size_ultilization': '0'}, )
    def test_get_pool_size_ultilization(self, param_dict):
        self.assertEqual(param_dict['size_ultilization'],
                         self.client.get_pool_size_ultilization(
                             param_dict['key']))

    # volumeTable
    def test_get_luns(self):
        items = self.client.get_luns()
        self.assertEqual(4, len(items))
        self.assertEqual({'sv_1', 'sv_2', 'sv_3', 'sv_4'}, set(items))

    @ddt.data({'key': 'sv_1', 'name': 'Yangpu'},
              {'key': 'sv_2', 'name': "n/a"}, )
    def test_get_lun_name(self, param_dict):
        self.assertEqual(param_dict['name'],
                         self.client.get_lun_name(param_dict['key']))

    @ddt.data({'key': 'sv_1', 'raid_type': 'RAID10'},
              {'key': 'sv_2', 'raid_type': NONE_STRING},
              {'key': 'sv_3', 'raid_type': NONE_STRING}, )
    def test_get_lun_raid_type(self, param_dict):
        self.assertEqual(param_dict['raid_type'],
                         self.client.get_lun_raid_type(param_dict['key']))

    @ddt.data({'key': 'sv_1', 'size_allocated': '0.0'},
              {'key': 'sv_2', 'size_allocated': '0'},
              {'key': 'sv_3', 'size_allocated': '0'},
              {'key': 'sv_4', 'size_allocated': NONE_STRING}, )
    def test_get_lun_size_allocated(self, param_dict):
        self.assertEqual(param_dict['size_allocated'],
                         self.client.get_lun_size_allocated(param_dict['key']))

    @ddt.data({'key': 'sv_1', 'size_total': '100.0'},
              {'key': 'sv_2', 'size_total': '0'},
              {'key': 'sv_3', 'size_total': '0'},
              {'key': 'sv_4', 'size_total': NONE_STRING}, )
    def test_get_lun_size_total(self, param_dict):
        self.assertEqual(param_dict['size_total'],
                         self.client.get_lun_size_total(param_dict['key']))

    @ddt.data({'key': 'sv_1', 'health': 'OK'},
              {'key': 'sv_2', 'health': NONE_STRING},
              {'key': 'sv_3', 'health': NONE_STRING},
              {'key': 'sv_4', 'health': 'OK BUT'}, )
    def test_get_lun_health_status(self, param_dict):
        self.assertEqual(param_dict['health'],
                         self.client.get_lun_health_status(param_dict['key']))

    @ddt.data({'key': 'sv_1', 'is_fast_cache_enabled': 'False'},
              {'key': 'sv_2', 'is_fast_cache_enabled': NONE_STRING},
              {'key': 'sv_3', 'is_fast_cache_enabled': NONE_STRING},
              {'key': 'sv_4', 'is_fast_cache_enabled': 'True'}, )
    def test_get_lun_fast_cache_status(self, param_dict):
        self.assertEqual(param_dict['is_fast_cache_enabled'],
                         self.client.get_lun_fast_cache_status(
                             param_dict['key']))

    @ddt.data({'key': 'sv_1', 'default_node': 'SP B'},
              {'key': 'sv_2', 'default_node': NONE_STRING},
              {'key': 'sv_3', 'default_node': NONE_STRING}, )
    def test_get_lun_default_sp(self, param_dict):
        self.assertEqual(param_dict['default_node'],
                         self.client.get_lun_default_sp(param_dict['key']))

    @ddt.data({'key': 'sv_1', 'current_node': 'SP A'},
              {'key': 'sv_2', 'current_node': NONE_STRING},
              {'key': 'sv_3', 'current_node': NONE_STRING}, )
    def test_get_lun_current_sp(self, param_dict):
        self.assertEqual(param_dict['current_node'],
                         self.client.get_lun_current_sp(param_dict['key']))

    @ddt.data({'key': 'sv_1', 'response_time': '5.08'},
              {'key': 'sv_2', 'response_time': '0'},
              {'key': 'sv_3', 'response_time': '0'},
              {'key': 'sv_4', 'response_time': NONE_STRING}, )
    def test_get_lun_response_time(self, param_dict):
        self.assertEqual(param_dict['response_time'],
                         self.client.get_lun_response_time(param_dict['key']))

    @ddt.data({'key': 'sv_1', 'queue_length': '0.01'},
              {'key': 'sv_2', 'queue_length': '0'},
              {'key': 'sv_3', 'queue_length': '0'},
              {'key': 'sv_4', 'queue_length': NONE_STRING}, )
    def test_get_lun_queue_length(self, param_dict):
        self.assertEqual(param_dict['queue_length'],
                         self.client.get_lun_queue_length(param_dict['key']))

    @ddt.data({'key': 'sv_1', 'total_iops': '0.433'},
              {'key': 'sv_2', 'total_iops': '0'},
              {'key': 'sv_3', 'total_iops': '0'},
              {'key': 'sv_4', 'total_iops': NONE_STRING}, )
    def test_get_lun_total_iops(self, param_dict):
        self.assertEqual(param_dict['total_iops'],
                         self.client.get_lun_total_iops(param_dict['key']))

    @ddt.data({'key': 'sv_1', 'read_iops': '0.033'},
              {'key': 'sv_2', 'read_iops': '0'},
              {'key': 'sv_3', 'read_iops': '0'},
              {'key': 'sv_4', 'read_iops': NONE_STRING}, )
    def test_get_lun_read_iops(self, param_dict):
        self.assertEqual(param_dict['read_iops'],
                         self.client.get_lun_read_iops(param_dict['key']))

    @ddt.data({'key': 'sv_1', 'write_iops': '0.4'},
              {'key': 'sv_2', 'write_iops': '0'},
              {'key': 'sv_3', 'write_iops': '0'},
              {'key': 'sv_4', 'write_iops': NONE_STRING}, )
    def test_get_lun_write_iops(self, param_dict):
        self.assertEqual(param_dict['write_iops'],
                         self.client.get_lun_write_iops(param_dict['key']))

    @ddt.data({'key': 'sv_1', 'total_byte_rate': '0.003'},
              {'key': 'sv_2', 'total_byte_rate': '0'},
              {'key': 'sv_3', 'total_byte_rate': '0'},
              {'key': 'sv_4', 'total_byte_rate': NONE_STRING}, )
    def test_get_lun_total_byte_rate(self, param_dict):
        self.assertEqual(param_dict['total_byte_rate'],
                         self.client.get_lun_total_byte_rate(
                             param_dict['key']))

    @ddt.data({'key': 'sv_1', 'read_byte_rate': '0.0'},
              {'key': 'sv_2', 'read_byte_rate': '0'},
              {'key': 'sv_3', 'read_byte_rate': '0'},
              {'key': 'sv_4', 'read_byte_rate': NONE_STRING}, )
    def test_get_lun_read_byte_rate(self, param_dict):
        self.assertEqual(param_dict['read_byte_rate'],
                         self.client.get_lun_read_byte_rate(param_dict['key']))

    @ddt.data({'key': 'sv_1', 'write_byte_rate': '0.002'},
              {'key': 'sv_2', 'write_byte_rate': '0'},
              {'key': 'sv_3', 'write_byte_rate': '0'},
              {'key': 'sv_4', 'write_byte_rate': NONE_STRING}, )
    def test_get_lun_write_byte_rate(self, param_dict):
        self.assertEqual(param_dict['write_byte_rate'],
                         self.client.get_lun_write_byte_rate(
                             param_dict['key']))

    @ddt.data({'key': 'sv_1', 'fast_cache_read_hits': '30.0'},
              {'key': 'sv_2', 'fast_cache_read_hits': '0'},
              {'key': 'sv_3', 'fast_cache_read_hits': '0'},
              {'key': 'sv_4', 'fast_cache_read_hits': NONE_STRING}, )
    def test_get_lun_fast_cache_read_hits(self, param_dict):
        self.assertEqual(param_dict['fast_cache_read_hits'],
                         self.client.get_lun_fast_cache_read_hits(
                             param_dict['key']))

    @ddt.data({'key': 'sv_1', 'fast_cache_write_hits': '30.0'},
              {'key': 'sv_2', 'fast_cache_write_hits': '0'},
              {'key': 'sv_3', 'fast_cache_write_hits': '0'},
              {'key': 'sv_4', 'fast_cache_write_hits': NONE_STRING}, )
    def test_get_lun_fast_cache_write_hits(self, param_dict):
        self.assertEqual(param_dict['fast_cache_write_hits'],
                         self.client.get_lun_fast_cache_write_hits(
                             param_dict['key']))

    @ddt.data({'key': 'sv_1', 'fast_cache_read_hit_rate': '30.0'},
              {'key': 'sv_2', 'fast_cache_read_hit_rate': '0'},
              {'key': 'sv_3', 'fast_cache_read_hit_rate': '0'},
              {'key': 'sv_4', 'fast_cache_read_hit_rate': NONE_STRING}, )
    def test_get_lun_fast_cache_read_hit_rate(self, param_dict):
        self.assertEqual(param_dict['fast_cache_read_hit_rate'],
                         self.client.get_lun_fast_cache_read_hit_rate(
                             param_dict['key']))

    @ddt.data({'key': 'sv_1', 'fast_cache_write_hit_rate': '30.03'},
              {'key': 'sv_2', 'fast_cache_write_hit_rate': '0'},
              {'key': 'sv_3', 'fast_cache_write_hit_rate': '0'},
              {'key': 'sv_4', 'fast_cache_write_hit_rate': NONE_STRING}, )
    def test_get_lun_fast_cache_write_hit_rate(self, param_dict):
        self.assertEqual(param_dict['fast_cache_write_hit_rate'],
                         self.client.get_lun_fast_cache_write_hit_rate(
                             param_dict['key']))

    @ddt.data({'key': 'sv_1', 'utilization': '0.081'},
              {'key': 'sv_2', 'utilization': '0'},
              {'key': 'sv_3', 'utilization': '0'},
              {'key': 'sv_4', 'utilization': NONE_STRING}, )
    def test_get_lun_utilization(self, param_dict):
        self.assertEqual(param_dict['utilization'],
                         self.client.get_lun_utilization(param_dict['key']))

    @ddt.data({'key': 'sv_1',
               'host_access': 'ESD-HOST193221.meng.lab.emc.com, \
10.245.54.151, VPI25224'},
              {'key': 'sv_2', 'host_access': NONE_STRING},
              {'key': 'sv_3', 'host_access': NONE_STRING}, )
    def test_get_lun_host_access(self, param_dict):
        self.assertEqual(param_dict['host_access'],
                         self.client.get_lun_host_access(param_dict['key']))

    # diskTable
    def test_get_disks(self):
        items = self.client.get_disks()
        self.assertEqual(4, len(items))
        self.assertEqual({'dpe_drive_0', 'dpe_drive_1', 'dae_drive_0',
                          'dae_drive_1'}, set(items))

    @ddt.data({'key': 'dpe_drive_0', 'name': 'DPE Drive 0'},
              {'key': 'dpe_drive_1', 'name': NONE_STRING}, )
    def test_get_disk_name(self, param_dict):
        self.assertEqual(param_dict['name'],
                         self.client.get_disk_name(param_dict['key']))

    @ddt.data({'key': 'dpe_drive_0', 'model': 'HU415606 EMC600'},
              {'key': 'dpe_drive_1', 'model': NONE_STRING}, )
    def test_get_disk_model(self, param_dict):
        self.assertEqual(param_dict['model'],
                         self.client.get_disk_model(param_dict['key']))

    @ddt.data({'key': 'dpe_drive_0', 'emc_serial_number': '0XG507BJ'},
              {'key': 'dpe_drive_1', 'emc_serial_number': NONE_STRING}, )
    def test_get_disk_serial_number(self, param_dict):
        self.assertEqual(param_dict['emc_serial_number'],
                         self.client.get_disk_serial_number(param_dict['key']))

    @ddt.data({'key': 'dpe_drive_0', 'version': 'K7P0'},
              {'key': 'dpe_drive_1', 'version': NONE_STRING}, )
    def test_get_disk_version(self, param_dict):
        self.assertEqual(param_dict['version'],
                         self.client.get_disk_version(param_dict['key']))

    @ddt.data({'key': 'dpe_drive_0', 'disk_technology': 'SAS'},
              {'key': 'dpe_drive_1', 'disk_technology': NONE_STRING}, )
    def test_get_disk_type(self, param_dict):
        self.assertEqual(param_dict['disk_technology'],
                         self.client.get_disk_type(param_dict['key']))

    @ddt.data({'key': 'dpe_drive_0', 'slot_number': '0'},
              {'key': 'dpe_drive_1', 'slot_number': NONE_STRING}, )
    def test_get_disk_slot_number(self, param_dict):
        self.assertEqual(param_dict['slot_number'],
                         self.client.get_disk_slot_number(param_dict['key']))

    @ddt.data({'key': 'dpe_drive_0', 'health': 'OK'},
              {'key': 'dpe_drive_1', 'health': NONE_STRING}, )
    def test_get_disk_health_status(self, param_dict):
        self.assertEqual(param_dict['health'],
                         self.client.get_disk_health_status(param_dict['key']))

    @ddt.data({'key': 'dpe_drive_0', 'raw_size': '550.313'},
              {'key': 'dpe_drive_1', 'raw_size': '0'},
              {'key': 'dae_drive_0', 'raw_size': '0'},
              {'key': 'dae_drive_1', 'raw_size': NONE_STRING}, )
    def test_get_disk_raw_size(self, param_dict):
        self.assertEqual(param_dict['raw_size'],
                         self.client.get_disk_raw_size(param_dict['key']))

    @ddt.data({'key': 'dpe_drive_0', 'pool': 'Shanghai'},
              {'key': 'dpe_drive_1', 'pool': NONE_STRING},
              {'key': 'dae_drive_0', 'pool': NONE_STRING}, )
    def test_get_disk_current_pool(self, param_dict):
        self.assertEqual(param_dict['pool'],
                         self.client.get_disk_current_pool(param_dict['key']))

    @ddt.data({'key': 'dpe_drive_0', 'response_time': '35.337'},
              {'key': 'dpe_drive_1', 'response_time': '0'},
              {'key': 'dae_drive_0', 'response_time': '0'},
              {'key': 'dae_drive_1', 'response_time': NONE_STRING}, )
    def test_get_disk_response_time(self, param_dict):
        self.assertEqual(param_dict['response_time'],
                         self.client.get_disk_response_time(param_dict['key']))

    @ddt.data({'key': 'dpe_drive_0', 'queue_length': '1.212'},
              {'key': 'dpe_drive_1', 'queue_length': '0'},
              {'key': 'dae_drive_0', 'queue_length': '0'},
              {'key': 'dae_drive_1', 'queue_length': NONE_STRING}, )
    def test_get_disk_queue_length(self, param_dict):
        self.assertEqual(param_dict['queue_length'],
                         self.client.get_disk_queue_length(param_dict['key']))

    @ddt.data({'key': 'dpe_drive_0', 'total_iops': '2.2'},
              {'key': 'dpe_drive_1', 'total_iops': '0'},
              {'key': 'dae_drive_0', 'total_iops': '0'},
              {'key': 'dae_drive_1', 'total_iops': NONE_STRING}, )
    def test_get_disk_total_iops(self, param_dict):
        self.assertEqual(param_dict['total_iops'],
                         self.client.get_disk_total_iops(param_dict['key']))

    @ddt.data({'key': 'dpe_drive_0', 'read_iops': '1.417'},
              {'key': 'dpe_drive_1', 'read_iops': '0'},
              {'key': 'dae_drive_0', 'read_iops': '0'},
              {'key': 'dae_drive_1', 'read_iops': NONE_STRING}, )
    def test_get_disk_read_iops(self, param_dict):
        self.assertEqual(param_dict['read_iops'],
                         self.client.get_disk_read_iops(param_dict['key']))

    @ddt.data({'key': 'dpe_drive_0', 'write_iops': '0.783'},
              {'key': 'dpe_drive_1', 'write_iops': '0'},
              {'key': 'dae_drive_0', 'write_iops': '0'},
              {'key': 'dae_drive_1', 'write_iops': NONE_STRING}, )
    def test_get_disk_write_iops(self, param_dict):
        self.assertEqual(param_dict['write_iops'],
                         self.client.get_disk_write_iops(param_dict['key']))

    @ddt.data({'key': 'dpe_drive_0', 'total_byte_rate': '1.269'},
              {'key': 'dpe_drive_1', 'total_byte_rate': '0'},
              {'key': 'dae_drive_0', 'total_byte_rate': '0'},
              {'key': 'dae_drive_1', 'total_byte_rate': NONE_STRING}, )
    def test_get_disk_total_byte_rate(self, param_dict):
        self.assertEqual(param_dict['total_byte_rate'],
                         self.client.get_disk_total_byte_rate(
                             param_dict['key']))

    @ddt.data({'key': 'dpe_drive_0', 'read_byte_rate': '1.072'},
              {'key': 'dpe_drive_1', 'read_byte_rate': '0'},
              {'key': 'dae_drive_0', 'read_byte_rate': '0'},
              {'key': 'dae_drive_1', 'read_byte_rate': NONE_STRING}, )
    def test_get_disk_read_byte_rate(self, param_dict):
        self.assertEqual(param_dict['read_byte_rate'],
                         self.client.get_disk_read_byte_rate(
                             param_dict['key']))

    @ddt.data({'key': 'dpe_drive_0', 'write_byte_rate': '0.197'},
              {'key': 'dpe_drive_1', 'write_byte_rate': '0'},
              {'key': 'dae_drive_0', 'write_byte_rate': '0'},
              {'key': 'dae_drive_1', 'write_byte_rate': NONE_STRING}, )
    def test_get_disk_write_byte_rate(self, param_dict):
        self.assertEqual(param_dict['write_byte_rate'],
                         self.client.get_disk_write_byte_rate(
                             param_dict['key']))

    @ddt.data({'key': 'dpe_drive_0', 'utilization': '22.45'},
              {'key': 'dpe_drive_1', 'utilization': '0'},
              {'key': 'dae_drive_0', 'utilization': '0'},
              {'key': 'dae_drive_1', 'utilization': NONE_STRING}, )
    def test_get_disk_utilization(self, param_dict):
        self.assertEqual(param_dict['utilization'],
                         self.client.get_disk_utilization(param_dict['key']))

    # frontendPortTable
    def test_get_frontend_ports(self):
        items = self.client.get_frontend_ports()
        self.assertEqual(4, len(items))
        self.assertEqual({'fc_port_spa_fc1', 'fc_port_spb_fc2',
                          'iscsi_port_iscsinode_spa_eth1',
                          'iscsi_port_iscsinode_spa_eth2'}, set(items))

    @ddt.data({'key': 'fc_port_spa_fc1', 'id': 'spa_fc1'},
              {'key': 'iscsi_port_iscsinode_spa_eth1',
               'id': 'iscsinode_spa_eth1'}, )
    def test_get_frontend_port_id(self, param_dict):
        self.assertEqual(param_dict['id'],
                         self.client.get_frontend_port_id(param_dict['key']))

    @ddt.data({'key': 'fc_port_spa_fc1', 'name': 'SP A FC Port 1'},
              {'key': 'fc_port_spa_fc2', 'name': NONE_STRING},
              {'key': 'iscsi_port_iscsinode_spa_eth1',
               'name': 'iqn.1992-04.com.emc:cx.fnm00150600267.a0'},
              {'key': 'iscsi_port_iscsinode_spa_eth2', 'name': NONE_STRING}, )
    def test_get_frontend_port_name(self, param_dict):
        self.assertEqual(param_dict['name'],
                         self.client.get_frontend_port_name(param_dict['key']))

    @ddt.data({'key': 'fc_port_spa_fc1', 'address': NONE_STRING},
              {'key': 'fc_port_spa_fc2', 'address': NONE_STRING},
              {'key': 'iscsi_port_iscsinode_spa_eth1',
               'address': '10.0.0.10'},
              {'key': 'iscsi_port_iscsinode_spa_eth2',
               'address': NONE_STRING}, )
    def test_get_frontend_port_address(self, param_dict):
        self.assertEqual(param_dict['address'],
                         self.client.get_frontend_port_address(
                             param_dict['key']))

    @ddt.data({'key': 'fc_port_spa_fc1', 'port_type': 'LC'},
              {'key': 'fc_port_spa_fc2', 'port_type': NONE_STRING},
              {'key': 'iscsi_port_iscsinode_spa_eth1', 'port_type': 'RJ45'},
              {'key': 'iscsi_port_iscsinode_spa_eth2',
               'port_type': NONE_STRING}, )
    def test_get_frontend_port_type(self, param_dict):
        self.assertEqual(param_dict['port_type'],
                         self.client.get_frontend_port_type(param_dict['key']))

    @ddt.data({'key': 'fc_port_spa_fc1', 'current_speed': '_8GbPS'},
              {'key': 'fc_port_spa_fc2', 'current_speed': NONE_STRING},
              {'key': 'iscsi_port_iscsinode_spa_eth1',
               'current_speed': '_10GbPS'},
              {'key': 'iscsi_port_iscsinode_spa_eth2',
               'current_speed': NONE_STRING}, )
    def test_get_frontend_port_current_speed(self, param_dict):
        self.assertEqual(param_dict['current_speed'],
                         self.client.get_frontend_port_current_speed(
                             param_dict['key']))

    @ddt.data({'key': 'fc_port_spa_fc1',
               'support_speed': '_4GbPS, _8GbPS, _16GbPS, AUTO'},
              {'key': 'fc_port_spa_fc2', 'support_speed': NONE_STRING},
              {'key': 'iscsi_port_iscsinode_spa_eth1',
               'support_speed': '_1GbPS, _10GbPS, _100MbPS, AUTO'},
              {'key': 'iscsi_port_iscsinode_spa_eth2',
               'support_speed': NONE_STRING}, )
    def test_get_frontend_port_supported_speed(self, param_dict):
        self.assertEqual(param_dict['support_speed'],
                         self.client.get_frontend_port_supported_speed(
                             param_dict['key']))

    @ddt.data({'key': 'fc_port_spa_fc1', 'health': 'MAJOR'},
              {'key': 'fc_port_spa_fc2', 'health': NONE_STRING},
              {'key': 'iscsi_port_iscsinode_spa_eth1', 'health': 'OK BUT'},
              {'key': 'iscsi_port_iscsinode_spa_eth2',
               'health': NONE_STRING}, )
    def test_get_frontend_port_health_status(self, param_dict):
        self.assertEqual(param_dict['health'],
                         self.client.get_frontend_port_health_status(
                             param_dict['key']))

    @ddt.data({'key': 'fc_port_spa_fc1', 'total_iops': '0'},
              {'key': 'fc_port_spa_fc2', 'total_iops': '0'},
              {'key': 'iscsi_port_iscsinode_spa_eth1', 'total_iops': '0.533'},
              {'key': 'iscsi_port_iscsinode_spa_eth2',
               'total_iops': NONE_STRING}, )
    def test_get_frontend_port_total_iops(self, param_dict):
        self.assertEqual(param_dict['total_iops'],
                         self.client.get_frontend_port_total_iops(
                             param_dict['key']))

    @ddt.data({'key': 'fc_port_spa_fc1', 'read_iops': '0'},
              {'key': 'fc_port_spa_fc2', 'read_iops': '0'},
              {'key': 'iscsi_port_iscsinode_spa_eth1', 'read_iops': '0.133'},
              {'key': 'iscsi_port_iscsinode_spa_eth2',
               'read_iops': NONE_STRING}, )
    def test_get_frontend_port_read_iops(self, param_dict):
        self.assertEqual(param_dict['read_iops'],
                         self.client.get_frontend_port_read_iops(
                             param_dict['key']))

    @ddt.data({'key': 'fc_port_spa_fc1', 'write_iops': '0'},
              {'key': 'fc_port_spa_fc2', 'write_iops': '0'},
              {'key': 'iscsi_port_iscsinode_spa_eth1', 'write_iops': '0.4'},
              {'key': 'iscsi_port_iscsinode_spa_eth2',
               'write_iops': NONE_STRING}, )
    def test_get_frontend_port_write_iops(self, param_dict):
        self.assertEqual(param_dict['write_iops'],
                         self.client.get_frontend_port_write_iops(
                             param_dict['key']))

    @ddt.data({'key': 'fc_port_spa_fc1', 'total_byte_rate': '0'},
              {'key': 'fc_port_spa_fc2', 'total_byte_rate': '0'},
              {'key': 'iscsi_port_iscsinode_spa_eth1',
               'total_byte_rate': '0.003'},
              {'key': 'iscsi_port_iscsinode_spa_eth2',
               'total_byte_rate': NONE_STRING}, )
    def test_get_frontend_port_total_byte_rate(self, param_dict):
        self.assertEqual(param_dict['total_byte_rate'],
                         self.client.get_frontend_port_total_byte_rate(
                             param_dict['key']))

    @ddt.data({'key': 'fc_port_spa_fc1', 'read_byte_rate': '0'},
              {'key': 'fc_port_spa_fc2', 'read_byte_rate': '0'},
              {'key': 'iscsi_port_iscsinode_spa_eth1',
               'read_byte_rate': '0.0'},
              {'key': 'iscsi_port_iscsinode_spa_eth2',
               'read_byte_rate': NONE_STRING}, )
    def test_get_frontend_port_read_byte_rate(self, param_dict):
        self.assertEqual(param_dict['read_byte_rate'],
                         self.client.get_frontend_port_read_byte_rate(
                             param_dict['key']))

    @ddt.data({'key': 'fc_port_spa_fc1', 'write_byte_rate': '0'},
              {'key': 'fc_port_spa_fc2', 'write_byte_rate': '0'},
              {'key': 'iscsi_port_iscsinode_spa_eth1',
               'write_byte_rate': '0.002'},
              {'key': 'iscsi_port_iscsinode_spa_eth2',
               'write_byte_rate': NONE_STRING}, )
    def test_get_frontend_port_write_byte_rate(self, param_dict):
        self.assertEqual(param_dict['write_byte_rate'],
                         self.client.get_frontend_port_write_byte_rate(
                             param_dict['key']))

    # backendPortTable
    def test_get_backend_ports(self):
        items = self.client.get_backend_ports()
        self.assertEqual(2, len(items))
        self.assertEqual({'spa_sas0', 'spb_sas0'}, set(items))

    @ddt.data({'key': 'spa_sas0', 'name': 'SP A SAS Port 0'},
              {'key': 'spb_sas0', 'name': NONE_STRING}, )
    def test_get_backend_port_name(self, param_dict):
        self.assertEqual(param_dict['name'],
                         self.client.get_backend_port_name(param_dict['key']))

    @ddt.data({'key': 'spa_sas0', 'connector_type': 'MINI_SAS_HD'},
              {'key': 'spb_sas0', 'connector_type': NONE_STRING}, )
    def test_get_backend_port_type(self, param_dict):
        self.assertEqual(param_dict['connector_type'],
                         self.client.get_backend_port_type(param_dict['key']))

    @ddt.data({'key': 'spa_sas0', 'port': '0'},
              {'key': 'spb_sas0', 'port': NONE_STRING}, )
    def test_get_backend_port_port_number(self, param_dict):
        self.assertEqual(param_dict['port'],
                         self.client.get_backend_port_port_number(
                             param_dict['key']))

    @ddt.data({'key': 'spa_sas0', 'current_speed': '_12Gbps'},
              {'key': 'spb_sas0', 'current_speed': NONE_STRING}, )
    def test_get_backend_port_current_speed(self, param_dict):
        self.assertEqual(param_dict['current_speed'],
                         self.client.get_backend_port_current_speed(
                             param_dict['key']))

    @ddt.data({'key': 'spa_sas0', 'parent_io_module': 'IO Module A'},
              {'key': 'spb_sas0', 'parent_io_module': NONE_STRING}, )
    def test_get_backend_port_parent_io_module(self, param_dict):
        self.assertEqual(param_dict['parent_io_module'],
                         self.client.get_backend_port_parent_io_module(
                             param_dict['key']))

    @ddt.data({'key': 'spa_sas0', 'parent_storage_processor': 'SP A'},
              {'key': 'spb_sas0', 'parent_storage_processor': NONE_STRING}, )
    def test_get_backend_port_parent_sp(self, param_dict):
        self.assertEqual(param_dict['parent_storage_processor'],
                         self.client.get_backend_port_parent_sp(
                             param_dict['key']))

    @ddt.data({'key': 'spa_sas0', 'health': 'OK'},
              {'key': 'spb_sas0', 'health': NONE_STRING}, )
    def test_get_backend_port_health_status(self, param_dict):
        self.assertEqual(param_dict['health'],
                         self.client.get_backend_port_health_status(
                             param_dict['key']))

    @ddt.data({'key': 'spa_sas0', 'total_iops': NONE_STRING})
    def test_get_backend_port_total_iops(self, param_dict):
        self.assertEqual(param_dict['total_iops'],
                         self.client.get_backend_port_total_iops(
                             param_dict['key']))

    @ddt.data({'key': 'spa_sas0', 'read_iops': NONE_STRING})
    def test_get_backend_port_read_iops(self, param_dict):
        self.assertEqual(param_dict['read_iops'],
                         self.client.get_backend_port_read_iops(
                             param_dict['key']))

    @ddt.data({'key': 'spa_sas0', 'write_iops': NONE_STRING})
    def test_get_backend_port_write_iops(self, param_dict):
        self.assertEqual(param_dict['write_iops'],
                         self.client.get_backend_port_write_iops(
                             param_dict['key']))

    @ddt.data({'key': 'spa_sas0', 'total_byte_rate': NONE_STRING})
    def test_get_backend_port_total_byte_rate(self, param_dict):
        self.assertEqual(param_dict['total_byte_rate'],
                         self.client.get_backend_port_total_byte_rate(
                             param_dict['key']))

    @ddt.data({'key': 'spa_sas0', 'read_byte_rate': NONE_STRING})
    def test_get_backend_port_read_byte_rate(self, param_dict):
        self.assertEqual(param_dict['read_byte_rate'],
                         self.client.get_backend_port_read_byte_rate(
                             param_dict['key']))

    @ddt.data({'key': 'spa_sas0', 'write_byte_rate': NONE_STRING})
    def test_get_backend_port_write_byte_rate(self, param_dict):
        self.assertEqual(param_dict['write_byte_rate'],
                         self.client.get_backend_port_write_byte_rate(
                             param_dict['key']))

    # hostTable
    def test_get_hosts(self):
        items = self.client.get_hosts()
        self.assertEqual(5, len(items))
        self.assertEqual({'host_1', 'host_2', 'host_3', 'host_4', 'host_5'},
                         set(items))

    @ddt.data({'key': 'host_1', 'name': 'ubuntu1604'},
              {'key': 'host_2', 'name': NONE_STRING})
    def test_get_host_name(self, param_dict):
        self.assertEqual(param_dict['name'],
                         self.client.get_host_name(param_dict['key']))

    @ddt.data({'key': 'host_1',
               'ip_list': '10.207.84.27, 2620:0:170:1d34:a236:9fff:fe66:'
                          '8960, 2620:0:170:1d36:a236:9fff:fe66:8960'},
              {'key': 'host_2', 'ip_list': NONE_STRING},
              {'key': 'host_3', 'ip_list': NONE_STRING}, )
    def test_get_host_network_address(self, param_dict):
        self.assertEqual(param_dict['ip_list'],
                         self.client.get_host_network_address(
                             param_dict['key']))

    @ddt.data({'key': 'host_1',
               'initiators': 'iqn.1993-08.org.debian:01:b974ee37fea, 20:'
                             '00:00:90:FA:53:49:28:10:00:00:90:FA:53:49:2'
                             '8, 20:00:00:90:FA:53:49:29:10:00:00:90:FA:5'
                             '3:49:29'},
              {'key': 'host_2', 'initiators': NONE_STRING},
              {'key': 'host_3',
               'initiators': '20:00:00:90:FA:53:49, 20:00:00:90:FA:53:50'},
              {'key': 'host_4',
               'initiators': 'iqn.1993-08.org.debian:01:b974ee37fea'},
              {'key': 'host_5',
               'initiators': NONE_STRING}, )
    def test_get_host_initiators(self, param_dict):
        self.assertEqual(param_dict['initiators'],
                         self.client.get_host_initiators(param_dict['key']))

    @ddt.data({'key': 'host_1', 'os_type': 'Linux'}, )
    def test_get_host_os_type(self, param_dict):
        self.assertEqual(param_dict['os_type'],
                         self.client.get_host_os_type(param_dict['key']))

    @ddt.data({'key': 'host_1', 'host_luns': 'storops_dummy_lun'},
              {'key': 'host_2', 'host_luns': NONE_STRING},
              {'key': 'host_3', 'host_luns': NONE_STRING}, )
    def test_get_host_assigned_volumes(self, param_dict):
        self.assertEqual(param_dict['host_luns'],
                         self.client.get_host_assigned_volumes(
                             param_dict['key']))

    # enclosureTable
    def test_get_enclosures(self):
        items = self.client.get_enclosures()
        self.assertEqual(4, len(items))
        self.assertEqual(
            {'dae_dae_1', 'dae_dae_2', 'dpe_dpe_1', 'dpe_dpe_2'},
            set(items))

    @ddt.data({'key': 'dae_dae_1', 'id': 'dae_1'},
              {'key': 'dpe_dpe_1', 'id': 'dpe_1'}, )
    def test_get_enclosure_id(self, param_dict):
        self.assertEqual(param_dict['id'],
                         self.client.get_enclosure_id(param_dict['key']))

    @ddt.data({'key': 'dae_dae_1', 'name': 'DAE 0 1'},
              {'key': 'dpe_dpe_1', 'name': 'DPE 1'}, )
    def test_get_enclosure_name(self, param_dict):
        self.assertEqual(param_dict['name'],
                         self.client.get_enclosure_name(param_dict['key']))

    @ddt.data({'key': 'dae_dae_1', 'model': 'ANCHO LF 12G SAS DAE'},
              {'key': 'dae_dae_2', 'model': NONE_STRING},
              {'key': 'dpe_dpe_1', 'model': 'OBERON 25 DRIVE CHASSIS'},
              {'key': 'dpe_dpe_2', 'model': NONE_STRING}, )
    def test_get_enclosure_model(self, param_dict):
        self.assertEqual(param_dict['model'],
                         self.client.get_enclosure_model(param_dict['key']))

    @ddt.data({'key': 'dae_dae_1', 'emc_serial_number': 'CF22W145100058'},
              {'key': 'dae_dae_2', 'emc_serial_number': NONE_STRING},
              {'key': 'dpe_dpe_1', 'emc_serial_number': 'CF2CV145000001'},
              {'key': 'dpe_dpe_2', 'emc_serial_number': NONE_STRING}, )
    def test_get_enclosure_serial_number(self, param_dict):
        self.assertEqual(param_dict['emc_serial_number'],
                         self.client.get_enclosure_serial_number(
                             param_dict['key']))

    @ddt.data({'key': 'dae_dae_1', 'emc_part_number': '100-900-000-04'},
              {'key': 'dae_dae_2', 'emc_part_number': NONE_STRING},
              {'key': 'dpe_dpe_1', 'emc_part_number': '100-542-901-05'},
              {'key': 'dpe_dpe_2', 'emc_part_number': NONE_STRING}, )
    def test_get_enclosure_part_number(self, param_dict):
        self.assertEqual(param_dict['emc_part_number'],
                         self.client.get_enclosure_part_number(
                             param_dict['key']))

    @ddt.data({'key': 'dae_dae_1', 'health': 'OK'},
              {'key': 'dae_dae_2', 'health': NONE_STRING},
              {'key': 'dpe_dpe_1', 'health': 'CRITICAL'},
              {'key': 'dpe_dpe_2', 'health': NONE_STRING}, )
    def test_get_enclosure_health_status(self, param_dict):
        self.assertEqual(param_dict['health'],
                         self.client.get_enclosure_health_status(
                             param_dict['key']))

    @ddt.data({'key': 'dae_dae_1', 'current_power': '430'},
              {'key': 'dae_dae_2', 'current_power': '0'},
              {'key': 'dpe_dpe_1', 'current_power': '0'},
              {'key': 'dpe_dpe_2', 'current_power': NONE_STRING}, )
    def test_get_enclosure_current_power(self, param_dict):
        self.assertEqual(param_dict['current_power'],
                         self.client.get_enclosure_current_power(
                             param_dict['key']))

    @ddt.data({'key': 'dae_dae_1', 'avg_power': '428'},
              {'key': 'dae_dae_2', 'avg_power': '0'},
              {'key': 'dpe_dpe_1', 'avg_power': '0'},
              {'key': 'dpe_dpe_2', 'avg_power': NONE_STRING}, )
    def test_get_enclosure_avg_power(self, param_dict):
        self.assertEqual(param_dict['avg_power'],
                         self.client.get_enclosure_avg_power(
                             param_dict['key']))

    @ddt.data({'key': 'dae_dae_1', 'max_power': '458'},
              {'key': 'dae_dae_2', 'max_power': '0'},
              {'key': 'dpe_dpe_1', 'max_power': '0'},
              {'key': 'dpe_dpe_2', 'max_power': NONE_STRING}, )
    def test_get_enclosure_max_power(self, param_dict):
        self.assertEqual(param_dict['max_power'],
                         self.client.get_enclosure_max_power(
                             param_dict['key']))

    @ddt.data({'key': 'dae_dae_1', 'current_temperature': '26'},
              {'key': 'dae_dae_2', 'current_temperature': '0'},
              {'key': 'dpe_dpe_1', 'current_temperature': '0'},
              {'key': 'dpe_dpe_2', 'current_temperature': NONE_STRING}, )
    def test_get_enclosure_current_temperature(self, param_dict):
        self.assertEqual(param_dict['current_temperature'],
                         self.client.get_enclosure_current_temperature(
                             param_dict['key']))

    @ddt.data({'key': 'dae_dae_1', 'avg_temperature': '25'},
              {'key': 'dae_dae_2', 'avg_temperature': '0'},
              {'key': 'dpe_dpe_1', 'avg_temperature': '0'},
              {'key': 'dpe_dpe_2', 'avg_temperature': NONE_STRING}, )
    def test_get_enclosure_avg_temperature(self, param_dict):
        self.assertEqual(param_dict['avg_temperature'],
                         self.client.get_enclosure_avg_temperature(
                             param_dict['key']))

    @ddt.data({'key': 'dae_dae_1', 'max_temperature': '30'},
              {'key': 'dae_dae_2', 'max_temperature': '0'},
              {'key': 'dpe_dpe_1', 'max_temperature': '0'},
              {'key': 'dpe_dpe_2', 'max_temperature': NONE_STRING}, )
    def test_get_enclosure_max_temperature(self, param_dict):
        self.assertEqual(param_dict['max_temperature'],
                         self.client.get_enclosure_max_temperature(
                             param_dict['key']))

    # powerSupplyTable
    def test_get_power_supplies(self):
        items = self.client.get_power_supplies()
        self.assertEqual(2, len(items))
        self.assertEqual({'power_a', 'power_b'}, set(items))

    @ddt.data({'key': 'power_a', 'name': 'DPE Power Supply A0'},
              {'key': 'power_b', 'name': NONE_STRING}, )
    def test_get_power_supply_name(self, param_dict):
        self.assertEqual(param_dict['name'],
                         self.client.get_power_supply_name(param_dict['key']))

    @ddt.data({'key': 'power_a',
               'manufacturer': 'FLEXTRONICS POWER INC.'},
              {'key': 'power_b',
               'manufacturer': NONE_STRING}, )
    def test_get_power_supply_manufacturer(self, param_dict):
        self.assertEqual(param_dict['manufacturer'],
                         self.client.get_power_supply_manufacturer(
                             param_dict['key']))

    @ddt.data({'key': 'power_a',
               'model': '12V P/S WITH 12VSTBY AND FAN'},
              {'key': 'power_b', 'model': NONE_STRING}, )
    def test_get_power_supply_model(self, param_dict):
        self.assertEqual(param_dict['model'],
                         self.client.get_power_supply_model(param_dict['key']))

    @ddt.data({'key': 'power_a', 'firmware_version': '0501'},
              {'key': 'power_b',
               'firmware_version': NONE_STRING}, )
    def test_get_power_supply_firmware_version(self, param_dict):
        self.assertEqual(param_dict['firmware_version'],
                         self.client.get_power_supply_firmware_version(
                             param_dict['key']))

    @ddt.data({'key': 'power_a', 'parent_enclosure': 'DPE, DAE'},
              {'key': 'power_b',
               'parent_enclosure': NONE_STRING}, )
    def test_get_power_supply_parent_enclosure(self, param_dict):
        self.assertEqual(param_dict['parent_enclosure'],
                         self.client.get_power_supply_parent_enclosure(
                             param_dict['key']))

    @ddt.data({'key': 'power_a', 'storage_processor': 'SP A'},
              {'key': 'power_b',
               'storage_processor': NONE_STRING}, )
    def test_get_power_supply_sp(self, param_dict):
        self.assertEqual(param_dict['storage_processor'],
                         self.client.get_power_supply_sp(param_dict['key']))

    @ddt.data({'key': 'power_a', 'health': 'OK'},
              {'key': 'power_b', 'health': NONE_STRING}, )
    def test_get_power_supply_health_status(self, param_dict):
        self.assertEqual(param_dict['health'],
                         self.client.get_power_supply_health_status(
                             param_dict['key']))

    # fanTable
    def test_get_fans(self):
        items = self.client.get_fans()
        self.assertEqual(4, len(items))
        self.assertEqual({'fan_a0', 'fan_a1', 'fan_a2', 'fan_b1'}, set(items))

    @ddt.data({'key': 'fan_a0', 'name': 'DPE Cooling Module A0'},
              {'key': 'fan_a1', 'name': NONE_STRING}, )
    def test_get_fan_name(self, param_dict):
        self.assertEqual(param_dict['name'],
                         self.client.get_fan_name(param_dict['key']))

    @ddt.data({'key': 'fan_a0', 'slot_number': '0'},
              {'key': 'fan_b1', 'slot_number': 'None'}, )
    def test_get_fan_slot_number(self, param_dict):
        self.assertEqual(param_dict['slot_number'],
                         self.client.get_fan_slot_number(param_dict['key']))

    @ddt.data(
        {'key': 'fan_a0',
         'parent_enclosure': 'DPE, DAE 0 1'},
        {'key': 'fan_a1', 'parent_enclosure': 'DPE'},
        {'key': 'fan_a2', 'parent_enclosure': 'DAE 0 1'},
        {'key': 'fan_b1', 'parent_enclosure': NONE_STRING}, )
    def test_get_fan_parent_enclosure(self, param_dict):
        self.assertEqual(param_dict['parent_enclosure'],
                         self.client.get_fan_parent_enclosure(
                             param_dict['key']))

    @ddt.data({'key': 'fan_a0', 'health': 'OK'},
              {'key': 'fan_b1', 'health': NONE_STRING}, )
    def test_get_fan_health_status(self, param_dict):
        self.assertEqual(param_dict['health'],
                         self.client.get_fan_health_status(param_dict['key']))

    # BBUTable
    def test_get_bbus(self):
        items = self.client.get_bbus()
        self.assertEqual(2, len(items))
        self.assertEqual({'battery_spa', 'battery_spb'}, set(items))

    @ddt.data({'key': 'battery_spa', 'name': 'SP A Battery 0'},
              {'key': 'battery_spb', 'name': NONE_STRING}, )
    def test_get_bbu_name(self, param_dict):
        self.assertEqual(param_dict['name'],
                         self.client.get_bbu_name(param_dict['key']))

    @ddt.data({'key': 'battery_spa',
               'manufacturer': 'ACBEL POLYTECH INC.'},
              {'key': 'battery_spb', 'manufacturer': NONE_STRING}, )
    def test_get_bbu_manufacturer(self, param_dict):
        self.assertEqual(param_dict['manufacturer'],
                         self.client.get_bbu_manufacturer(param_dict['key']))

    @ddt.data({'key': 'battery_spa',
               'model': 'LITHIUM-ION, UNIVERSAL BOB'},
              {'key': 'battery_spb',
               'model': NONE_STRING}, )
    def test_get_bbu_model(self, param_dict):
        self.assertEqual(param_dict['model'],
                         self.client.get_bbu_model(param_dict['key']))

    @ddt.data({'key': 'battery_spa', 'firmware_version': '073.91'},
              {'key': 'battery_spb', 'firmware_version': NONE_STRING}, )
    def test_get_bbu_firmware_version(self, param_dict):
        self.assertEqual(param_dict['firmware_version'],
                         self.client.get_bbu_firmware_version(
                             param_dict['key']))

    @ddt.data({'key': 'battery_spa', 'parent_storage_processor': 'SP A'},
              {'key': 'battery_spb',
               'parent_storage_processor': NONE_STRING}, )
    def test_get_bbu_parent_sp(self, param_dict):
        self.assertEqual(param_dict['parent_storage_processor'],
                         self.client.get_bbu_parent_sp(param_dict['key']))

    @ddt.data({'key': 'battery_spa', 'health': 'OK'},
              {'key': 'battery_spb', 'health': NONE_STRING}, )
    def test_get_bbu_health_status(self, param_dict):
        self.assertEqual(param_dict['health'],
                         self.client.get_bbu_health_status(param_dict['key']))
