import unittest

import ddt
from snmpagent.tests import patches
from snmpagent.unity_impl import *


@ddt.ddt
class TestUnityClient(unittest.TestCase):
    def setUp(self):
        self.name = 'oid'
        self.idx = 0
        self.test_string = 'test string'
        self.test_number = 100
        self.test_list = ['a', 'b', 'c']

    # system
    @patches.unity_client
    def test_agent_version(self, unity_client):
        unity_client.get_agent_version.return_value = self.test_string
        obj = AgentVersion.AgentVersion()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_agent_version.assert_called_once()

    @patches.unity_client
    def test_mib_version(self, unity_client):
        unity_client.get_mib_version.return_value = self.test_string
        obj = MibVersion.MibVersion()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_mib_version.assert_called_once()

    @patches.unity_client
    def test_manufacturer(self, unity_client):
        unity_client.get_manufacturer.return_value = self.test_string
        obj = Manufacturer.Manufacturer()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_manufacturer.assert_called_once()

    @patches.unity_client
    def test_model(self, unity_client):
        unity_client.get_model.return_value = self.test_string
        obj = Model.Model()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_model.assert_called_once()

    @patches.unity_client
    def test_serial_number(self, unity_client):
        unity_client.get_serial_number.return_value = self.test_string
        obj = SerialNumber.SerialNumber()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_serial_number.assert_called_once()

    @patches.unity_client
    def test_operation_environment_version(self, unity_client):
        unity_client.get_operation_environment_version.return_value = self.test_string
        obj = OperationEnvironmentVersion.OperationEnvironmentVersion()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_operation_environment_version.assert_called_once()

    @patches.unity_client
    def test_mgmt_ip(self, unity_client):
        unity_client.get_mgmt_ip.return_value = self.test_string
        obj = ManagementIP.ManagementIP()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_mgmt_ip.assert_called_once()

    @patches.unity_client
    def test_current_power(self, unity_client):
        unity_client.get_current_power.return_value = self.test_string
        obj = CurrentPower.CurrentPower()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_current_power.assert_called_once()

    @patches.unity_client
    def test_avg_power(self, unity_client):
        unity_client.get_avg_power.return_value = self.test_string
        obj = AveragePower.AveragePower()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_avg_power.assert_called_once()

    @patches.unity_client
    def test_number_of_sp(self, unity_client):
        unity_client.get_number_of_sp.return_value = self.test_number
        obj = NumberOfStorageProcessor.NumberOfStorageProcessor()
        self.assertEqual(self.test_number,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_number_of_sp.assert_called_once()

    @patches.unity_client
    def test_number_of_enclosure(self, unity_client):
        unity_client.get_number_of_enclosure.return_value = self.test_number
        obj = NumberOfEnclosure.NumberOfEnclosure()
        self.assertEqual(self.test_number,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_number_of_enclosure.assert_called_once()

    @patches.unity_client
    def test_number_of_power_supply(self, unity_client):
        unity_client.get_number_of_power_supply.return_value = self.test_number
        obj = NumberOfPowerSupply.NumberOfPowerSupply()
        self.assertEqual(self.test_number,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_number_of_power_supply.assert_called_once()

    @patches.unity_client
    def test_number_of_fan(self, unity_client):
        unity_client.get_number_of_fan.return_value = self.test_number
        obj = NumberOfFan.NumberOfFan()
        self.assertEqual(self.test_number,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_number_of_fan.assert_called_once()

    @patches.unity_client
    def test_number_of_disk(self, unity_client):
        unity_client.get_number_of_disk.return_value = self.test_number
        obj = NumberOfPhysicalDisk.NumberOfPhysicalDisk()
        self.assertEqual(self.test_number,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_number_of_disk.assert_called_once()

    @patches.unity_client
    def test_number_of_frontend_port(self, unity_client):
        unity_client.get_number_of_frontend_port.return_value = self.test_number
        obj = NumberOfFrontendPort.NumberOfFrontendPort()
        self.assertEqual(self.test_number,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_number_of_frontend_port.assert_called_once()

    @patches.unity_client
    def test_number_of_backend_port(self, unity_client):
        unity_client.get_number_of_backend_port.return_value = self.test_number
        obj = NumberOfBackendPort.NumberOfBackendPort()
        self.assertEqual(self.test_number,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_number_of_backend_port.assert_called_once()

    @patches.unity_client
    def test_total_capacity(self, unity_client):
        unity_client.get_total_capacity.return_value = self.test_string
        obj = TotalCapacity.TotalCapacity()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_total_capacity.assert_called_once()

    @patches.unity_client
    def test_used_capacity(self, unity_client):
        unity_client.get_used_capacity.return_value = self.test_string
        obj = UsedCapacity.UsedCapacity()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_used_capacity.assert_called_once()

    @patches.unity_client
    def test_free_capacity(self, unity_client):
        unity_client.get_free_capacity.return_value = self.test_string
        obj = FreeCapacity.FreeCapacity()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_free_capacity.assert_called_once()

    @patches.unity_client
    def test_total_iops(self, unity_client):
        unity_client.get_total_iops.return_value = self.test_string
        obj = TotalThroughput.TotalThroughput()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_total_iops.assert_called_once()

    @patches.unity_client
    def test_read_iops(self, unity_client):
        unity_client.get_read_iops.return_value = self.test_string
        obj = ReadThroughput.ReadThroughput()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_read_iops.assert_called_once()

    @patches.unity_client
    def test_write_iops(self, unity_client):
        unity_client.get_write_iops.return_value = self.test_string
        obj = WriteThroughput.WriteThroughput()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_write_iops.assert_called_once()

    @patches.unity_client
    def test_total_byte_rate(self, unity_client):
        unity_client.get_total_byte_rate.return_value = self.test_string
        obj = TotalBandwidth.TotalBandwidth()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_total_byte_rate.assert_called_once()

    @patches.unity_client
    def test_read_byte_rate(self, unity_client):
        unity_client.get_read_byte_rate.return_value = self.test_string
        obj = ReadBandwidth.ReadBandwidth()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_read_byte_rate.assert_called_once()

    @patches.unity_client
    def test_write_byte_rate(self, unity_client):
        unity_client.get_write_byte_rate.return_value = self.test_string
        obj = WriteBandwidth.WriteBandwidth()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_write_byte_rate.assert_called_once()

    # storageProcessorTable
    @patches.unity_client
    def test_sp_name(self, unity_client):
        obj = StorageProcessorName.StorageProcessorName()
        self.assertEqual(self.idx,
                         obj.read_get(self.name, self.idx, unity_client))

    @patches.unity_client
    def test_sp_name_column(self, unity_client):
        unity_client.get_sps.return_value = self.test_list
        obj = StorageProcessorName.StorageProcessorNameColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_sps.assert_called_once()

    @patches.unity_client
    def test_sp_serial_number(self, unity_client):
        unity_client.get_sp_serial_number.return_value = self.test_string
        obj = StorageProcessorSerialNumber.StorageProcessorSerialNumber()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_sp_serial_number.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_sp_serial_number_column(self, unity_client):
        unity_client.get_sps.return_value = self.test_list
        obj = StorageProcessorSerialNumber.StorageProcessorSerialNumberColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_sps.assert_called_once()

    @patches.unity_client
    def test_sp_op_state(self, unity_client):
        unity_client.get_sp_health_status.return_value = self.test_string
        obj = StorageProcessorOperationalState.StorageProcessorOperationalState()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_sp_health_status.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_sp_op_state_column(self, unity_client):
        unity_client.get_sps.return_value = self.test_list
        obj = StorageProcessorOperationalState.StorageProcessorOperationalStateColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_sps.assert_called_once()

    @patches.unity_client
    def test_sp_cpu_utilization(self, unity_client):
        unity_client.get_sp_utilization.return_value = self.test_string
        obj = StorageProcessorCpuUtilization.StorageProcessorCpuUtilization()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_sp_utilization.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_sp_cpu_utilization_column(self, unity_client):
        unity_client.get_sps.return_value = self.test_list
        obj = StorageProcessorCpuUtilization.StorageProcessorCpuUtilizationColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_sps.assert_called_once()

    @patches.unity_client
    def test_sp_total_iops(self, unity_client):
        unity_client.get_sp_block_total_iops.return_value = self.test_string
        obj = StorageProcessorTotalThroughput.StorageProcessorTotalThroughput()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_sp_block_total_iops.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_sp_total_iops_column(self, unity_client):
        unity_client.get_sps.return_value = self.test_list
        obj = StorageProcessorTotalThroughput.StorageProcessorTotalThroughputColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_sps.assert_called_once()

    @patches.unity_client
    def test_sp_read_iops(self, unity_client):
        unity_client.get_sp_block_read_iops.return_value = self.test_string
        obj = StorageProcessorReadThroughput.StorageProcessorReadThroughput()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_sp_block_read_iops.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_sp_read_iops_column(self, unity_client):
        unity_client.get_sps.return_value = self.test_list
        obj = StorageProcessorReadThroughput.StorageProcessorReadThroughputColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_sps.assert_called_once()

    @patches.unity_client
    def test_sp_write_iops(self, unity_client):
        unity_client.get_sp_block_write_iops.return_value = self.test_string
        obj = StorageProcessorWriteThroughput.StorageProcessorWriteThroughput()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_sp_block_write_iops.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_sp_write_iops_column(self, unity_client):
        unity_client.get_sps.return_value = self.test_list
        obj = StorageProcessorWriteThroughput.StorageProcessorWriteThroughputColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_sps.assert_called_once()

    @patches.unity_client
    def test_sp_total_byte_rate(self, unity_client):
        unity_client.get_sp_total_byte_rate.return_value = self.test_string
        obj = StorageProcessorTotalBandwidth.StorageProcessorTotalBandwidth()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_sp_total_byte_rate.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_sp_total_byte_rate_column(self, unity_client):
        unity_client.get_sps.return_value = self.test_list
        obj = StorageProcessorTotalBandwidth.StorageProcessorTotalBandwidthColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_sps.assert_called_once()

    @patches.unity_client
    def test_sp_read_byte_rate(self, unity_client):
        unity_client.get_sp_read_byte_rate.return_value = self.test_string
        obj = StorageProcessorReadBandwidth.StorageProcessorReadBandwidth()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_sp_read_byte_rate.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_sp_read_byte_rate_column(self, unity_client):
        unity_client.get_sps.return_value = self.test_list
        obj = StorageProcessorReadBandwidth.StorageProcessorReadBandwidthColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_sps.assert_called_once()

    @patches.unity_client
    def test_sp_write_byte_rate(self, unity_client):
        unity_client.get_sp_write_byte_rate.return_value = self.test_string
        obj = StorageProcessorWriteBandwidth.StorageProcessorWriteBandwidth()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_sp_write_byte_rate.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_sp_write_byte_rate_column(self, unity_client):
        unity_client.get_sps.return_value = self.test_list
        obj = StorageProcessorWriteBandwidth.StorageProcessorWriteBandwidthColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_sps.assert_called_once()

    @patches.unity_client
    def test_sp_cache_dirty_size(self, unity_client):
        unity_client.get_sp_cache_dirty_size.return_value = self.test_string
        obj = StorageProcessorCacheDirtySize.StorageProcessorCacheDirtySize()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_sp_cache_dirty_size.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_sp_cache_dirty_size_column(self, unity_client):
        unity_client.get_sps.return_value = self.test_list
        obj = StorageProcessorCacheDirtySize.StorageProcessorCacheDirtySizeColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_sps.assert_called_once()

    @patches.unity_client
    def test_sp_cache_read_hit_ratio(self, unity_client):
        unity_client.get_sp_block_cache_read_hit_ratio.return_value = self.test_string
        obj = StorageProcessorReadCacheState.StorageProcessorReadCacheState()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_sp_block_cache_read_hit_ratio.assert_called_once_with(
            self.idx)

    @patches.unity_client
    def test_sp_cache_read_hit_ratio_column(self, unity_client):
        unity_client.get_sps.return_value = self.test_list
        obj = StorageProcessorReadCacheState.StorageProcessorReadCacheStateColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_sps.assert_called_once()

    @patches.unity_client
    def test_sp_cache_write_hit_ratio(self, unity_client):
        unity_client.get_sp_block_cache_write_hit_ratio.return_value = self.test_string
        obj = StorageProcessorWriteCacheState.StorageProcessorWriteCacheState()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_sp_block_cache_write_hit_ratio.assert_called_once_with(
            self.idx)

    @patches.unity_client
    def test_sp_cache_write_hit_ratio_column(self, unity_client):
        unity_client.get_sps.return_value = self.test_list
        obj = StorageProcessorWriteCacheState.StorageProcessorWriteCacheStateColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_sps.assert_called_once()

    # poolTable
    @patches.unity_client
    def test_pool_name(self, unity_client):
        obj = PoolName.PoolName()
        self.assertEqual(self.idx,
                         obj.read_get(self.name, self.idx, unity_client))

    @patches.unity_client
    def test_pool_name_column(self, unity_client):
        unity_client.get_pools.return_value = self.test_list
        obj = PoolName.PoolNameColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_pools.assert_called_once()

    @patches.unity_client
    def test_pool_disk_types(self, unity_client):
        unity_client.get_pool_disk_types.return_value = self.test_string
        obj = PoolDiskTypes.PoolDiskTypes()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_pool_disk_types.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_pool_disk_types_column(self, unity_client):
        unity_client.get_pools.return_value = self.test_list
        obj = PoolDiskTypes.PoolDiskTypesColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_pools.assert_called_once()

    @patches.unity_client
    def test_pool_raid_levels(self, unity_client):
        unity_client.get_pool_raid_levels.return_value = self.test_string
        obj = PoolRaidLevels.PoolRaidLevels()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_pool_raid_levels.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_pool_raid_levels_column(self, unity_client):
        unity_client.get_pools.return_value = self.test_list
        obj = PoolRaidLevels.PoolRaidLevelsColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_pools.assert_called_once()

    @patches.unity_client
    def test_pool_fast_cache_status(self, unity_client):
        unity_client.get_pool_fast_cache_status.return_value = self.test_string
        obj = PoolFastCacheStatus.PoolFastCacheStatus()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_pool_fast_cache_status.assert_called_once_with(
            self.idx)

    @patches.unity_client
    def test_pool_fast_cache_status_column(self, unity_client):
        unity_client.get_pools.return_value = self.test_list
        obj = PoolFastCacheStatus.PoolFastCacheStatusColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_pools.assert_called_once()

    @patches.unity_client
    def test_pool_number_of_disk(self, unity_client):
        unity_client.get_pool_number_of_disk.return_value = self.test_number
        obj = PoolNumberOfPhysicalDisk.PoolNumberOfPhysicalDisk()
        self.assertEqual(self.test_number,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_pool_number_of_disk.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_pool_number_of_disk_column(self, unity_client):
        unity_client.get_pools.return_value = self.test_list
        obj = PoolNumberOfPhysicalDisk.PoolNumberOfPhysicalDiskColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_pools.assert_called_once()

    @patches.unity_client
    def test_pool_size_total(self, unity_client):
        unity_client.get_pool_size_total.return_value = self.test_string
        obj = PoolTotalCapacity.PoolTotalCapacity()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_pool_size_total.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_pool_size_total_column(self, unity_client):
        unity_client.get_pools.return_value = self.test_list
        obj = PoolTotalCapacity.PoolTotalCapacityColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_pools.assert_called_once()

    @patches.unity_client
    def test_pool_size_free(self, unity_client):
        unity_client.get_pool_size_free.return_value = self.test_string
        obj = PoolRemainingCapacity.PoolRemainingCapacity()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_pool_size_free.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_pool_size_free_column(self, unity_client):
        unity_client.get_pools.return_value = self.test_list
        obj = PoolRemainingCapacity.PoolRemainingCapacityColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_pools.assert_called_once()

    @patches.unity_client
    def test_pool_size_used(self, unity_client):
        unity_client.get_pool_size_used.return_value = self.test_string
        obj = PoolUsedCapacity.PoolUsedCapacity()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_pool_size_used.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_pool_size_used_column(self, unity_client):
        unity_client.get_pools.return_value = self.test_list
        obj = PoolUsedCapacity.PoolUsedCapacityColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_pools.assert_called_once()

    @patches.unity_client
    def test_pool_size_ultilization(self, unity_client):
        unity_client.get_pool_size_ultilization.return_value = self.test_string
        obj = PoolCapacityUtilization.PoolCapacityUtilization()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_pool_size_ultilization.assert_called_once_with(
            self.idx)

    @patches.unity_client
    def test_pool_size_ultilization_column(self, unity_client):
        unity_client.get_pools.return_value = self.test_list
        obj = PoolCapacityUtilization.PoolCapacityUtilizationColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_pools.assert_called_once()

    # volumeTable
    @patches.unity_client
    def test_lun_id(self, unity_client):
        obj = VolumeId.VolumeId()
        self.assertEqual(self.idx,
                         obj.read_get(self.name, self.idx, unity_client))

    @patches.unity_client
    def test_lun_id_column(self, unity_client):
        unity_client.get_luns.return_value = self.test_list
        obj = VolumeId.VolumeIdColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_luns.assert_called_once()

    @patches.unity_client
    def test_lun_name(self, unity_client):
        unity_client.get_lun_name.return_value = self.test_string
        obj = VolumeName.VolumeName()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_lun_name.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_lun_name_column(self, unity_client):
        unity_client.get_luns.return_value = self.test_list
        obj = VolumeName.VolumeNameColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_luns.assert_called_once()

    @patches.unity_client
    def test_lun_raid_type(self, unity_client):
        unity_client.get_lun_raid_type.return_value = self.test_string
        obj = VolumeRaidLevels.VolumeRaidLevels()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_lun_raid_type.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_lun_raid_type_column(self, unity_client):
        unity_client.get_luns.return_value = self.test_list
        obj = VolumeRaidLevels.VolumeRaidLevelsColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_luns.assert_called_once()

    @patches.unity_client
    def test_lun_size_allocated(self, unity_client):
        unity_client.get_lun_size_allocated.return_value = self.test_string
        obj = VolumeAllocatedSize.VolumeAllocatedSize()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_lun_size_allocated.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_lun_size_allocated_column(self, unity_client):
        unity_client.get_luns.return_value = self.test_list
        obj = VolumeAllocatedSize.VolumeAllocatedSizeColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_luns.assert_called_once()

    @patches.unity_client
    def test_lun_size_total(self, unity_client):
        unity_client.get_lun_size_total.return_value = self.test_string
        obj = VolumeSize.VolumeSize()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_lun_size_total.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_lun_size_total_column(self, unity_client):
        unity_client.get_luns.return_value = self.test_list
        obj = VolumeSize.VolumeSizeColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_luns.assert_called_once()

    @patches.unity_client
    def test_lun_health_status(self, unity_client):
        unity_client.get_lun_health_status.return_value = self.test_string
        obj = VolumeOperationalState.VolumeOperationalState()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_lun_health_status.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_lun_health_status_column(self, unity_client):
        unity_client.get_luns.return_value = self.test_list
        obj = VolumeOperationalState.VolumeOperationalStateColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_luns.assert_called_once()

    @patches.unity_client
    def test_lun_fast_cache_status(self, unity_client):
        unity_client.get_lun_fast_cache_status.return_value = self.test_string
        obj = VolumeFastCacheState.VolumeFastCacheState()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_lun_fast_cache_status.assert_called_once_with(
            self.idx)

    @patches.unity_client
    def test_lun_fast_cache_status_column(self, unity_client):
        unity_client.get_luns.return_value = self.test_list
        obj = VolumeFastCacheState.VolumeFastCacheStateColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_luns.assert_called_once()

    @patches.unity_client
    def test_lun_default_sp(self, unity_client):
        unity_client.get_lun_default_sp.return_value = self.test_string
        obj = VolumeDefaultStorageProcessor.VolumeDefaultStorageProcessor()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_lun_default_sp.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_lun_default_sp_column(self, unity_client):
        unity_client.get_luns.return_value = self.test_list
        obj = VolumeDefaultStorageProcessor.VolumeDefaultStorageProcessorColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_luns.assert_called_once()

    @patches.unity_client
    def test_lun_current_sp(self, unity_client):
        unity_client.get_lun_current_sp.return_value = self.test_string
        obj = VolumeCurrentStorageProcessor.VolumeCurrentStorageProcessor()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_lun_current_sp.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_lun_current_sp_column(self, unity_client):
        unity_client.get_luns.return_value = self.test_list
        obj = VolumeCurrentStorageProcessor.VolumeCurrentStorageProcessorColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_luns.assert_called_once()

    @patches.unity_client
    def test_lun_response_time(self, unity_client):
        unity_client.get_lun_response_time.return_value = self.test_string
        obj = VolumeResponseTime.VolumeResponseTime()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_lun_response_time.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_lun_response_time_column(self, unity_client):
        unity_client.get_luns.return_value = self.test_list
        obj = VolumeResponseTime.VolumeResponseTimeColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_luns.assert_called_once()

    @patches.unity_client
    def test_lun_queue_length(self, unity_client):
        unity_client.get_lun_queue_length.return_value = self.test_string
        obj = VolumeQueueLength.VolumeQueueLength()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_lun_queue_length.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_lun_queue_length_column(self, unity_client):
        unity_client.get_luns.return_value = self.test_list
        obj = VolumeQueueLength.VolumeQueueLengthColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_luns.assert_called_once()

    @patches.unity_client
    def test_lun_total_iops(self, unity_client):
        unity_client.get_lun_total_iops.return_value = self.test_string
        obj = VolumeTotalThroughput.VolumeTotalThroughput()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_lun_total_iops.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_lun_total_iops_column(self, unity_client):
        unity_client.get_luns.return_value = self.test_list
        obj = VolumeTotalThroughput.VolumeTotalThroughputColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_luns.assert_called_once()

    @patches.unity_client
    def test_lun_read_iops(self, unity_client):
        unity_client.get_lun_read_iops.return_value = self.test_string
        obj = VolumeReadThroughput.VolumeReadThroughput()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_lun_read_iops.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_lun_read_iops_column(self, unity_client):
        unity_client.get_luns.return_value = self.test_list
        obj = VolumeReadThroughput.VolumeReadThroughputColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_luns.assert_called_once()

    @patches.unity_client
    def test_lun_write_iops(self, unity_client):
        unity_client.get_lun_write_iops.return_value = self.test_string
        obj = VolumeWriteThroughput.VolumeWriteThroughput()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_lun_write_iops.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_lun_write_iops_column(self, unity_client):
        unity_client.get_luns.return_value = self.test_list
        obj = VolumeWriteThroughput.VolumeWriteThroughputColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_luns.assert_called_once()

    @patches.unity_client
    def test_lun_fast_cache_read_hit_iops(self, unity_client):
        unity_client.get_lun_fast_cache_read_hits.return_value = self.test_string
        obj = VolumeFastCacheReadHitIOs.VolumeFastCacheReadHitIOs()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_lun_fast_cache_read_hits.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_lun_fast_cache_read_hit_iops_column(self, unity_client):
        unity_client.get_luns.return_value = self.test_list
        obj = VolumeFastCacheReadHitIOs.VolumeFastCacheReadHitIOsColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_luns.assert_called_once()

    @patches.unity_client
    def test_lun_fast_cache_write_hit_iops(self, unity_client):
        unity_client.get_lun_fast_cache_write_hits.return_value = self.test_string
        obj = VolumeFastCacheWriteHitIOs.VolumeFastCacheWriteHitIOs()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_lun_fast_cache_write_hits.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_lun_fast_cache_write_hit_iops_column(self, unity_client):
        unity_client.get_luns.return_value = self.test_list
        obj = VolumeFastCacheWriteHitIOs.VolumeFastCacheWriteHitIOsColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_luns.assert_called_once()

    @patches.unity_client
    def test_lun_total_byte_rate(self, unity_client):
        unity_client.get_lun_total_byte_rate.return_value = self.test_string
        obj = VolumeTotalBandwidth.VolumeTotalBandwidth()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_lun_total_byte_rate.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_lun_total_byte_rate_column(self, unity_client):
        unity_client.get_luns.return_value = self.test_list
        obj = VolumeTotalBandwidth.VolumeTotalBandwidthColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_luns.assert_called_once()

    @patches.unity_client
    def test_lun_read_byte_rate(self, unity_client):
        unity_client.get_lun_read_byte_rate.return_value = self.test_string
        obj = VolumeReadBandwidth.VolumeReadBandwidth()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_lun_read_byte_rate.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_lun_read_byte_rate_column(self, unity_client):
        unity_client.get_luns.return_value = self.test_list
        obj = VolumeReadBandwidth.VolumeReadBandwidthColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_luns.assert_called_once()

    @patches.unity_client
    def test_lun_write_byte_rate(self, unity_client):
        unity_client.get_lun_write_byte_rate.return_value = self.test_string
        obj = VolumeWriteBandwidth.VolumeWriteBandwidth()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_lun_write_byte_rate.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_lun_write_byte_rate_column(self, unity_client):
        unity_client.get_luns.return_value = self.test_list
        obj = VolumeWriteBandwidth.VolumeWriteBandwidthColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_luns.assert_called_once()

    @patches.unity_client
    def test_lun_fast_cache_read_hit_rate(self, unity_client):
        unity_client.get_lun_fast_cache_read_hit_rate.return_value = self.test_string
        obj = VolumeFastCacheReadHitRate.VolumeFastCacheReadHitRate()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_lun_fast_cache_read_hit_rate.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_lun_fast_cache_read_hit_rate_column(self, unity_client):
        unity_client.get_luns.return_value = self.test_list
        obj = VolumeFastCacheReadHitRate.VolumeFastCacheReadHitRateColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_luns.assert_called_once()

    @patches.unity_client
    def test_lun_fast_cache_write_hit_rate(self, unity_client):
        unity_client.get_lun_fast_cache_write_hit_rate.return_value = self.test_string
        obj = VolumeFastCacheWriteHitRate.VolumeFastCacheWriteHitRate()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_lun_fast_cache_write_hit_rate.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_lun_fast_cache_write_hit_rate_column(self, unity_client):
        unity_client.get_luns.return_value = self.test_list
        obj = VolumeFastCacheWriteHitRate.VolumeFastCacheWriteHitRateColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_luns.assert_called_once()

    @patches.unity_client
    def test_lun_utilization(self, unity_client):
        unity_client.get_lun_utilization.return_value = self.test_string
        obj = VolumeUtilization.VolumeUtilization()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_lun_utilization.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_lun_utilization(self, unity_client):
        unity_client.get_luns.return_value = self.test_list
        obj = VolumeUtilization.VolumeUtilizationColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_luns.assert_called_once()

    @patches.unity_client
    def test_lun_host_access(self, unity_client):
        unity_client.get_lun_host_access.return_value = self.test_string
        obj = VolumeHostInfo.VolumeHostInfo()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_lun_host_access.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_lun_host_access(self, unity_client):
        unity_client.get_luns.return_value = self.test_list
        obj = VolumeHostInfo.VolumeHostInfoColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_luns.assert_called_once()
