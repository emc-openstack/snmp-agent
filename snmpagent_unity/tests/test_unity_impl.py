import unittest

import ddt
from snmpagent_unity.tests import patches
from snmpagent_unity.unity_impl import AgentVersion, AveragePower, \
    BackendPortCurrentSpeed, BackendPortId, BackendPortName, \
    BackendPortParentIoModule, BackendPortParentStorageProcessor, \
    BackendPortPortNumber, BackendPortStatus, BackendPortType, \
    BbuFirmwareVersion, BbuHealthStatus, BbuId, \
    BbuManufacturer, BbuModel, BbuName, BbuParentStorageProcessor, \
    CurrentPower, DiskCurrentPool, DiskFirmwareVersion, DiskId, DiskModel, \
    DiskName, DiskPhysicalLocation, DiskQueueLength, DiskRawCapacity, \
    DiskReadBandwidth, DiskReadThroughput, DiskResponseTime, \
    DiskSerialNumber, DiskStatus, DiskTotalBandwidth, DiskTotalThroughput, \
    DiskType, DiskUtilization, DiskWriteBandwidth, DiskWriteThroughput, \
    EnclosureAveragePower, EnclosureAverageTemperature, \
    EnclosureCurrentPower, EnclosureCurrentTemperature, EnclosureId, \
    EnclosureHealthStatus, EnclosureMaxPower, EnclosureMaxTemperature, \
    EnclosureModel, EnclosureName, EnclosurePartNumber, \
    EnclosureSerialNumber, FanHealthStatus, FanId, FanName, \
    FanParentEnclosure, FanSlotNumber, FreeCapacity, \
    FrontendPortAddress, FrontendPortCurrentSpeed, FrontendPortId, \
    FrontendPortName, FrontendPortReadBandwidth, FrontendPortReadThroughput, \
    FrontendPortStatus, FrontendPortSupportedSpeed, \
    FrontendPortTotalBandwidth, FrontendPortTotalThroughput, \
    FrontendPortType, FrontendPortWriteBandwidth, \
    FrontendPortWriteThroughput, HostAssignedStorageVolumes, HostId, \
    HostInitiators, HostName, HostNetworkAddress, HostOperationSystemVersion, \
    ManagementIP, Manufacturer, MibVersion, Model, NumberOfBackendPort, \
    NumberOfEnclosure, NumberOfFan, NumberOfFrontendPort, \
    NumberOfPhysicalDisk, NumberOfPowerSupply, NumberOfStorageProcessor, \
    OperationEnvironmentVersion, PoolCapacityUtilization, PoolDiskTypes, \
    PoolFastCacheStatus, PoolId, PoolName, PoolNumberOfPhysicalDisk, \
    PoolRaidLevels, PoolRemainingCapacity, PoolTotalCapacity, \
    PoolUsedCapacity, PowerSupplyFirmwareVersion, \
    PowerSupplyHealthStatus, PowerSupplyId, PowerSupplyManufacturer, \
    PowerSupplyModel, PowerSupplyName, PowerSupplyParentEnclosure, \
    PowerSupplyStorageProcessor, ReadBandwidth, ReadThroughput, \
    SerialNumber, StorageProcessorCacheDirtySize, \
    StorageProcessorCpuUtilization, StorageProcessorId, \
    StorageProcessorName, StorageProcessorOperationalState, \
    StorageProcessorReadBandwidth, StorageProcessorReadCacheState, \
    StorageProcessorReadThroughput, StorageProcessorSerialNumber, \
    StorageProcessorTotalBandwidth, StorageProcessorTotalThroughput, \
    StorageProcessorWriteBandwidth, StorageProcessorWriteCacheState, \
    StorageProcessorWriteThroughput, StorageProcessorFastCacheReadHitIOs, \
    StorageProcessorFastCacheReadHitRate, \
    StorageProcessorFastCacheWriteHitIOs, \
    StorageProcessorFastCacheWriteHitRate, TotalBandwidth, TotalCapacity, \
    TotalThroughput, UsedCapacity, VolumeAllocatedSize, \
    VolumeCurrentStorageProcessor, VolumeDefaultStorageProcessor, \
    VolumeFastCacheState, VolumeHostInfo, VolumeId, VolumeName, \
    VolumeOperationalState, VolumeQueueLength, VolumeRaidLevels, \
    VolumeReadBandwidth, VolumeReadThroughput, VolumeResponseTime, \
    VolumeSize, VolumeTotalBandwidth, VolumeTotalThroughput, \
    VolumeUtilization, VolumeWriteBandwidth, VolumeWriteThroughput, \
    WriteBandwidth, WriteThroughput


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
        unity_client.get_operation_environment_version.return_value = \
            self.test_string
        obj = OperationEnvironmentVersion. \
            OperationEnvironmentVersion()
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
        unity_client.get_number_of_power_supply.return_value = \
            self.test_number
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
        unity_client.get_number_of_frontend_port.return_value = \
            self.test_number
        obj = NumberOfFrontendPort.NumberOfFrontendPort()
        self.assertEqual(self.test_number,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_number_of_frontend_port.assert_called_once()

    @patches.unity_client
    def test_number_of_backend_port(self, unity_client):
        unity_client.get_number_of_backend_port.return_value = \
            self.test_number
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
    def test_sp_id(self, unity_client):
        obj = StorageProcessorId.StorageProcessorId()
        self.assertEqual(self.idx,
                         obj.read_get(self.name, self.idx, unity_client))

    @patches.unity_client
    def test_sp_id_column(self, unity_client):
        unity_client.get_sps.return_value = self.test_list
        obj = StorageProcessorId.StorageProcessorIdColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_sps.assert_called_once()

    @patches.unity_client
    def test_sp_name(self, unity_client):
        unity_client.get_sp_name.return_value = self.test_string
        obj = StorageProcessorName.StorageProcessorName()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_sp_name.assert_called_once_with(self.idx)

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
        obj = StorageProcessorSerialNumber. \
            StorageProcessorSerialNumber()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_sp_serial_number.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_sp_serial_number_column(self, unity_client):
        unity_client.get_sps.return_value = self.test_list
        obj = StorageProcessorSerialNumber. \
            StorageProcessorSerialNumberColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_sps.assert_called_once()

    @patches.unity_client
    def test_sp_op_state(self, unity_client):
        unity_client.get_sp_health_status.return_value = self.test_string
        obj = StorageProcessorOperationalState. \
            StorageProcessorOperationalState()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_sp_health_status.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_sp_op_state_column(self, unity_client):
        unity_client.get_sps.return_value = self.test_list
        obj = StorageProcessorOperationalState. \
            StorageProcessorOperationalStateColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_sps.assert_called_once()

    @patches.unity_client
    def test_sp_cpu_utilization(self, unity_client):
        unity_client.get_sp_utilization.return_value = self.test_string
        obj = StorageProcessorCpuUtilization. \
            StorageProcessorCpuUtilization()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_sp_utilization.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_sp_cpu_utilization_column(self, unity_client):
        unity_client.get_sps.return_value = self.test_list
        obj = StorageProcessorCpuUtilization. \
            StorageProcessorCpuUtilizationColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_sps.assert_called_once()

    @patches.unity_client
    def test_sp_total_iops(self, unity_client):
        unity_client.get_sp_block_total_iops.return_value = self.test_string
        obj = StorageProcessorTotalThroughput. \
            StorageProcessorTotalThroughput()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_sp_block_total_iops.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_sp_total_iops_column(self, unity_client):
        unity_client.get_sps.return_value = self.test_list
        obj = StorageProcessorTotalThroughput. \
            StorageProcessorTotalThroughputColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_sps.assert_called_once()

    @patches.unity_client
    def test_sp_read_iops(self, unity_client):
        unity_client.get_sp_block_read_iops.return_value = self.test_string
        obj = StorageProcessorReadThroughput. \
            StorageProcessorReadThroughput()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_sp_block_read_iops.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_sp_read_iops_column(self, unity_client):
        unity_client.get_sps.return_value = self.test_list
        obj = StorageProcessorReadThroughput. \
            StorageProcessorReadThroughputColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_sps.assert_called_once()

    @patches.unity_client
    def test_sp_write_iops(self, unity_client):
        unity_client.get_sp_block_write_iops.return_value = self.test_string
        obj = StorageProcessorWriteThroughput. \
            StorageProcessorWriteThroughput()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_sp_block_write_iops.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_sp_write_iops_column(self, unity_client):
        unity_client.get_sps.return_value = self.test_list
        obj = StorageProcessorWriteThroughput. \
            StorageProcessorWriteThroughputColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_sps.assert_called_once()

    @patches.unity_client
    def test_sp_total_byte_rate(self, unity_client):
        unity_client.get_sp_total_byte_rate.return_value = self.test_string
        obj = StorageProcessorTotalBandwidth. \
            StorageProcessorTotalBandwidth()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_sp_total_byte_rate.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_sp_total_byte_rate_column(self, unity_client):
        unity_client.get_sps.return_value = self.test_list
        obj = StorageProcessorTotalBandwidth. \
            StorageProcessorTotalBandwidthColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_sps.assert_called_once()

    @patches.unity_client
    def test_sp_read_byte_rate(self, unity_client):
        unity_client.get_sp_read_byte_rate.return_value = self.test_string
        obj = StorageProcessorReadBandwidth. \
            StorageProcessorReadBandwidth()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_sp_read_byte_rate.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_sp_read_byte_rate_column(self, unity_client):
        unity_client.get_sps.return_value = self.test_list
        obj = StorageProcessorReadBandwidth. \
            StorageProcessorReadBandwidthColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_sps.assert_called_once()

    @patches.unity_client
    def test_sp_write_byte_rate(self, unity_client):
        unity_client.get_sp_write_byte_rate.return_value = self.test_string
        obj = StorageProcessorWriteBandwidth. \
            StorageProcessorWriteBandwidth()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_sp_write_byte_rate.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_sp_write_byte_rate_column(self, unity_client):
        unity_client.get_sps.return_value = self.test_list
        obj = StorageProcessorWriteBandwidth. \
            StorageProcessorWriteBandwidthColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_sps.assert_called_once()

    @patches.unity_client
    def test_sp_cache_dirty_size(self, unity_client):
        unity_client.get_sp_cache_dirty_size.return_value = self.test_string
        obj = StorageProcessorCacheDirtySize. \
            StorageProcessorCacheDirtySize()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_sp_cache_dirty_size.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_sp_cache_dirty_size_column(self, unity_client):
        unity_client.get_sps.return_value = self.test_list
        obj = StorageProcessorCacheDirtySize. \
            StorageProcessorCacheDirtySizeColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_sps.assert_called_once()

    @patches.unity_client
    def test_sp_cache_read_hit_ratio(self, unity_client):
        unity_client.get_sp_block_cache_read_hit_ratio.return_value = \
            self.test_string
        obj = StorageProcessorReadCacheState. \
            StorageProcessorReadCacheState()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_sp_block_cache_read_hit_ratio.assert_called_once_with(
            self.idx)

    @patches.unity_client
    def test_sp_cache_read_hit_ratio_column(self, unity_client):
        unity_client.get_sps.return_value = self.test_list
        obj = StorageProcessorReadCacheState. \
            StorageProcessorReadCacheStateColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_sps.assert_called_once()

    @patches.unity_client
    def test_sp_cache_write_hit_ratio(self, unity_client):
        unity_client.get_sp_block_cache_write_hit_ratio.return_value = \
            self.test_string
        obj = StorageProcessorWriteCacheState. \
            StorageProcessorWriteCacheState()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_sp_block_cache_write_hit_ratio. \
            assert_called_once_with(self.idx)

    @patches.unity_client
    def test_sp_cache_write_hit_ratio_column(self, unity_client):
        unity_client.get_sps.return_value = self.test_list
        obj = StorageProcessorWriteCacheState. \
            StorageProcessorWriteCacheStateColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_sps.assert_called_once()

    @patches.unity_client
    def test_sp_fast_cache_read_hit_iops(self, unity_client):
        unity_client.get_sp_fast_cache_read_hits.return_value = \
            self.test_string
        obj = StorageProcessorFastCacheReadHitIOs.\
            StorageProcessorFastCacheReadHitIOs()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_sp_fast_cache_read_hits.assert_called_once_with(
            self.idx)

    @patches.unity_client
    def test_sp_fast_cache_read_hit_iops_column(self, unity_client):
        unity_client.get_sps.return_value = self.test_list
        obj = StorageProcessorFastCacheReadHitIOs. \
            StorageProcessorFastCacheReadHitIOsColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_sps.assert_called_once()

    @patches.unity_client
    def test_sp_fast_cache_write_hit_iops(self, unity_client):
        unity_client.get_sp_fast_cache_write_hits.return_value = \
            self.test_string
        obj = StorageProcessorFastCacheWriteHitIOs. \
            StorageProcessorFastCacheWriteHitIOs()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_sp_fast_cache_write_hits.assert_called_once_with(
            self.idx)

    @patches.unity_client
    def test_sp_fast_cache_write_hit_iops_column(self, unity_client):
        unity_client.get_sps.return_value = self.test_list
        obj = StorageProcessorFastCacheWriteHitIOs. \
            StorageProcessorFastCacheWriteHitIOsColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_sps.assert_called_once()

    @patches.unity_client
    def test_sp_fast_cache_read_hit_rate(self, unity_client):
        unity_client.get_sp_fast_cache_read_hit_rate.return_value = \
            self.test_string
        obj = StorageProcessorFastCacheReadHitRate. \
            StorageProcessorFastCacheReadHitRate()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_sp_fast_cache_read_hit_rate.assert_called_once_with(
            self.idx)

    @patches.unity_client
    def test_sp_fast_cache_read_hit_rate_column(self, unity_client):
        unity_client.get_sps.return_value = self.test_list
        obj = StorageProcessorFastCacheReadHitRate. \
            StorageProcessorFastCacheReadHitRateColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_sps.assert_called_once()

    @patches.unity_client
    def test_sp_fast_cache_write_hit_rate(self, unity_client):
        unity_client.get_sp_fast_cache_write_hit_rate.return_value = \
            self.test_string
        obj = StorageProcessorFastCacheWriteHitRate. \
            StorageProcessorFastCacheWriteHitRate()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_sp_fast_cache_write_hit_rate.assert_called_once_with(
            self.idx)

    @patches.unity_client
    def test_sp_fast_cache_write_hit_rate_column(self, unity_client):
        unity_client.get_sps.return_value = self.test_list
        obj = StorageProcessorFastCacheWriteHitRate. \
            StorageProcessorFastCacheWriteHitRateColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_sps.assert_called_once()

    # poolTable
    @patches.unity_client
    def test_pool_id(self, unity_client):
        obj = PoolId.PoolId()
        self.assertEqual(self.idx,
                         obj.read_get(self.name, self.idx, unity_client))

    @patches.unity_client
    def test_pool_id_column(self, unity_client):
        unity_client.get_pools.return_value = self.test_list
        obj = PoolId.PoolIdColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_pools.assert_called_once()

    @patches.unity_client
    def test_pool_name(self, unity_client):
        unity_client.get_pool_name.return_value = self.test_string
        obj = PoolName.PoolName()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_pool_name.assert_called_once_with(self.idx)

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
        unity_client.get_pool_fast_cache_status.return_value = \
            self.test_string
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
        obj = PoolNumberOfPhysicalDisk. \
            PoolNumberOfPhysicalDiskColumn()
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
        unity_client.get_pool_size_ultilization.return_value = \
            self.test_string
        obj = PoolCapacityUtilization.PoolCapacityUtilization()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_pool_size_ultilization.assert_called_once_with(
            self.idx)

    @patches.unity_client
    def test_pool_size_ultilization_column(self, unity_client):
        unity_client.get_pools.return_value = self.test_list
        obj = PoolCapacityUtilization. \
            PoolCapacityUtilizationColumn()
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
        obj = VolumeDefaultStorageProcessor. \
            VolumeDefaultStorageProcessor()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_lun_default_sp.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_lun_default_sp_column(self, unity_client):
        unity_client.get_luns.return_value = self.test_list
        obj = VolumeDefaultStorageProcessor. \
            VolumeDefaultStorageProcessorColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_luns.assert_called_once()

    @patches.unity_client
    def test_lun_current_sp(self, unity_client):
        unity_client.get_lun_current_sp.return_value = self.test_string
        obj = VolumeCurrentStorageProcessor. \
            VolumeCurrentStorageProcessor()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_lun_current_sp.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_lun_current_sp_column(self, unity_client):
        unity_client.get_luns.return_value = self.test_list
        obj = VolumeCurrentStorageProcessor. \
            VolumeCurrentStorageProcessorColumn()
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
    def test_lun_utilization(self, unity_client):
        unity_client.get_lun_utilization.return_value = self.test_string
        obj = VolumeUtilization.VolumeUtilization()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_lun_utilization.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_lun_utilization_column(self, unity_client):
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
    def test_lun_host_access_column(self, unity_client):
        unity_client.get_luns.return_value = self.test_list
        obj = VolumeHostInfo.VolumeHostInfoColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_luns.assert_called_once()

    # diskTable
    @patches.unity_client
    def test_disk_id(self, unity_client):
        obj = DiskId.DiskId()
        self.assertEqual(self.idx,
                         obj.read_get(self.name, self.idx, unity_client))

    @patches.unity_client
    def test_disk_id_column(self, unity_client):
        unity_client.get_disks.return_value = self.test_list
        obj = DiskId.DiskIdColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_disks.assert_called_once()

    @patches.unity_client
    def test_disk_name(self, unity_client):
        unity_client.get_disk_name.return_value = self.test_string
        obj = DiskName.DiskName()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_disk_name.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_disk_name_column(self, unity_client):
        unity_client.get_disks.return_value = self.test_list
        obj = DiskName.DiskNameColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_disks.assert_called_once()

    @patches.unity_client
    def test_disk_model(self, unity_client):
        unity_client.get_disk_model.return_value = self.test_string
        obj = DiskModel.DiskModel()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_disk_model.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_disk_model_column(self, unity_client):
        unity_client.get_disks.return_value = self.test_list
        obj = DiskModel.DiskModelColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_disks.assert_called_once()

    @patches.unity_client
    def test_disk_serial_number(self, unity_client):
        unity_client.get_disk_serial_number.return_value = self.test_string
        obj = DiskSerialNumber.DiskSerialNumber()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_disk_serial_number.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_disk_serial_number_column(self, unity_client):
        unity_client.get_disks.return_value = self.test_list
        obj = DiskSerialNumber.DiskSerialNumberColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_disks.assert_called_once()

    @patches.unity_client
    def test_disk_version(self, unity_client):
        unity_client.get_disk_version.return_value = self.test_string
        obj = DiskFirmwareVersion.DiskFirmwareVersion()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_disk_version.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_disk_version_column(self, unity_client):
        unity_client.get_disks.return_value = self.test_list
        obj = DiskFirmwareVersion.DiskFirmwareVersionColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_disks.assert_called_once()

    @patches.unity_client
    def test_disk_type(self, unity_client):
        unity_client.get_disk_type.return_value = self.test_string
        obj = DiskType.DiskType()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_disk_type.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_disk_type_column(self, unity_client):
        unity_client.get_disks.return_value = self.test_list
        obj = DiskType.DiskTypeColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_disks.assert_called_once()

    @patches.unity_client
    def test_disk_slot_number(self, unity_client):
        unity_client.get_disk_slot_number.return_value = self.test_string
        obj = DiskPhysicalLocation.DiskPhysicalLocation()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_disk_slot_number.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_disk_slot_number_column(self, unity_client):
        unity_client.get_disks.return_value = self.test_list
        obj = DiskPhysicalLocation.DiskPhysicalLocationColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_disks.assert_called_once()

    @patches.unity_client
    def test_disk_status(self, unity_client):
        unity_client.get_disk_health_status.return_value = self.test_string
        obj = DiskStatus.DiskStatus()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_disk_health_status.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_disk_status_column(self, unity_client):
        unity_client.get_disks.return_value = self.test_list
        obj = DiskStatus.DiskStatusColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_disks.assert_called_once()

    @patches.unity_client
    def test_disk_raw_size(self, unity_client):
        unity_client.get_disk_raw_size.return_value = self.test_string
        obj = DiskRawCapacity.DiskRawCapacity()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_disk_raw_size.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_disk_raw_size_column(self, unity_client):
        unity_client.get_disks.return_value = self.test_list
        obj = DiskRawCapacity.DiskRawCapacityColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_disks.assert_called_once()

    @patches.unity_client
    def test_disk_current_pool(self, unity_client):
        unity_client.get_disk_current_pool.return_value = self.test_string
        obj = DiskCurrentPool.DiskCurrentPool()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_disk_current_pool.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_disk_current_pool_column(self, unity_client):
        unity_client.get_disks.return_value = self.test_list
        obj = DiskCurrentPool.DiskCurrentPoolColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_disks.assert_called_once()

    @patches.unity_client
    def test_disk_response_time(self, unity_client):
        unity_client.get_disk_response_time.return_value = self.test_string
        obj = DiskResponseTime.DiskResponseTime()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_disk_response_time.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_disk_response_time_column(self, unity_client):
        unity_client.get_disks.return_value = self.test_list
        obj = DiskResponseTime.DiskResponseTimeColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_disks.assert_called_once()

    @patches.unity_client
    def test_disk_queue_length(self, unity_client):
        unity_client.get_disk_queue_length.return_value = self.test_string
        obj = DiskQueueLength.DiskQueueLength()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_disk_queue_length.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_disk_queue_length_column(self, unity_client):
        unity_client.get_disks.return_value = self.test_list
        obj = DiskQueueLength.DiskQueueLengthColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_disks.assert_called_once()

    @patches.unity_client
    def test_disk_total_iops(self, unity_client):
        unity_client.get_disk_total_iops.return_value = self.test_string
        obj = DiskTotalThroughput.DiskTotalThroughput()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_disk_total_iops.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_disk_total_iops_column(self, unity_client):
        unity_client.get_disks.return_value = self.test_list
        obj = DiskTotalThroughput.DiskTotalThroughputColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_disks.assert_called_once()

    @patches.unity_client
    def test_disk_read_iops(self, unity_client):
        unity_client.get_disk_read_iops.return_value = self.test_string
        obj = DiskReadThroughput.DiskReadThroughput()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_disk_read_iops.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_disk_read_iops_column(self, unity_client):
        unity_client.get_disks.return_value = self.test_list
        obj = DiskReadThroughput.DiskReadThroughputColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_disks.assert_called_once()

    @patches.unity_client
    def test_disk_write_iops(self, unity_client):
        unity_client.get_disk_write_iops.return_value = self.test_string
        obj = DiskWriteThroughput.DiskWriteThroughput()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_disk_write_iops.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_disk_write_iops_column(self, unity_client):
        unity_client.get_disks.return_value = self.test_list
        obj = DiskWriteThroughput.DiskWriteThroughputColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_disks.assert_called_once()

    @patches.unity_client
    def test_disk_total_byte_rate(self, unity_client):
        unity_client.get_disk_total_byte_rate.return_value = self.test_string
        obj = DiskTotalBandwidth.DiskTotalBandwidth()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_disk_total_byte_rate.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_disk_total_byte_rate_column(self, unity_client):
        unity_client.get_disks.return_value = self.test_list
        obj = DiskTotalBandwidth.DiskTotalBandwidthColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_disks.assert_called_once()

    @patches.unity_client
    def test_disk_read_byte_rate(self, unity_client):
        unity_client.get_disk_read_byte_rate.return_value = self.test_string
        obj = DiskReadBandwidth.DiskReadBandwidth()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_disk_read_byte_rate.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_disk_read_byte_rate_column(self, unity_client):
        unity_client.get_disks.return_value = self.test_list
        obj = DiskReadBandwidth.DiskReadBandwidthColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_disks.assert_called_once()

    @patches.unity_client
    def test_disk_write_byte_rate(self, unity_client):
        unity_client.get_disk_write_byte_rate.return_value = self.test_string
        obj = DiskWriteBandwidth.DiskWriteBandwidth()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_disk_write_byte_rate.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_disk_write_byte_rate_column(self, unity_client):
        unity_client.get_disks.return_value = self.test_list
        obj = DiskWriteBandwidth.DiskWriteBandwidthColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_disks.assert_called_once()

    @patches.unity_client
    def test_disk_utilization(self, unity_client):
        unity_client.get_disk_utilization.return_value = self.test_string
        obj = DiskUtilization.DiskUtilization()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_disk_utilization.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_disk_utilization_column(self, unity_client):
        unity_client.get_disks.return_value = self.test_list
        obj = DiskUtilization.DiskUtilizationColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_disks.assert_called_once()

    # frontendPortTable
    @patches.unity_client
    def test_frontend_port_id(self, unity_client):
        unity_client.get_frontend_port_id.return_value = self.test_string
        obj = FrontendPortId.FrontendPortId()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_frontend_port_id.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_frontend_port_id_column(self, unity_client):
        unity_client.get_frontend_ports.return_value = self.test_list
        obj = FrontendPortId.FrontendPortIdColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_frontend_ports.assert_called_once()

    @patches.unity_client
    def test_frontend_port_name(self, unity_client):
        unity_client.get_frontend_port_name.return_value = self.test_string
        obj = FrontendPortName.FrontendPortName()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_frontend_port_name.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_frontend_port_name_column(self, unity_client):
        unity_client.get_frontend_ports.return_value = self.test_list
        obj = FrontendPortName.FrontendPortNameColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_frontend_ports.assert_called_once()

    @patches.unity_client
    def test_frontend_port_address(self, unity_client):
        unity_client.get_frontend_port_address.return_value = self.test_string
        obj = FrontendPortAddress.FrontendPortAddress()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_frontend_port_address.assert_called_once_with(
            self.idx)

    @patches.unity_client
    def test_frontend_port_address_column(self, unity_client):
        unity_client.get_frontend_ports.return_value = self.test_list
        obj = FrontendPortAddress.FrontendPortAddressColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_frontend_ports.assert_called_once()

    @patches.unity_client
    def test_frontend_port_type(self, unity_client):
        unity_client.get_frontend_port_type.return_value = self.test_string
        obj = FrontendPortType.FrontendPortType()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_frontend_port_type.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_frontend_port_type_column(self, unity_client):
        unity_client.get_frontend_ports.return_value = self.test_list
        obj = FrontendPortType.FrontendPortTypeColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_frontend_ports.assert_called_once()

    @patches.unity_client
    def test_frontend_port_current_speed(self, unity_client):
        unity_client.get_frontend_port_current_speed.return_value = \
            self.test_string
        obj = FrontendPortCurrentSpeed.FrontendPortCurrentSpeed()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_frontend_port_current_speed.assert_called_once_with(
            self.idx)

    @patches.unity_client
    def test_frontend_port_current_speed_column(self, unity_client):
        unity_client.get_frontend_ports.return_value = self.test_list
        obj = FrontendPortCurrentSpeed. \
            FrontendPortCurrentSpeedColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_frontend_ports.assert_called_once()

    @patches.unity_client
    def test_frontend_port_support_speed(self, unity_client):
        unity_client.get_frontend_port_supported_speed.return_value = \
            self.test_string
        obj = FrontendPortSupportedSpeed. \
            FrontendPortSupportedSpeed()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_frontend_port_supported_speed.assert_called_once_with(
            self.idx)

    @patches.unity_client
    def test_frontend_port_support_speed_column(self, unity_client):
        unity_client.get_frontend_ports.return_value = self.test_list
        obj = FrontendPortSupportedSpeed. \
            FrontendPortSupportedSpeedColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_frontend_ports.assert_called_once()

    @patches.unity_client
    def test_frontend_port_status(self, unity_client):
        unity_client.get_frontend_port_health_status.return_value = \
            self.test_string
        obj = FrontendPortStatus.FrontendPortStatus()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_frontend_port_health_status.assert_called_once_with(
            self.idx)

    @patches.unity_client
    def test_frontend_port_status_column(self, unity_client):
        unity_client.get_frontend_ports.return_value = self.test_list
        obj = FrontendPortStatus.FrontendPortStatusColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_frontend_ports.assert_called_once()

    @patches.unity_client
    def test_frontend_port_total_iops(self, unity_client):
        unity_client.get_frontend_port_total_iops.return_value = \
            self.test_string
        obj = FrontendPortTotalThroughput. \
            FrontendPortTotalThroughput()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_frontend_port_total_iops.assert_called_once_with(
            self.idx)

    @patches.unity_client
    def test_frontend_port_total_iops_column(self, unity_client):
        unity_client.get_frontend_ports.return_value = self.test_list
        obj = FrontendPortTotalThroughput. \
            FrontendPortTotalThroughputColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_frontend_ports.assert_called_once()

    @patches.unity_client
    def test_frontend_port_read_iops(self, unity_client):
        unity_client.get_frontend_port_read_iops.return_value = \
            self.test_string
        obj = FrontendPortReadThroughput. \
            FrontendPortReadThroughput()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_frontend_port_read_iops.assert_called_once_with(
            self.idx)

    @patches.unity_client
    def test_frontend_port_read_iops_column(self, unity_client):
        unity_client.get_frontend_ports.return_value = self.test_list
        obj = FrontendPortReadThroughput. \
            FrontendPortReadThroughputColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_frontend_ports.assert_called_once()

    @patches.unity_client
    def test_frontend_port_write_iops(self, unity_client):
        unity_client.get_frontend_port_write_iops.return_value = \
            self.test_string
        obj = FrontendPortWriteThroughput. \
            FrontendPortWriteThroughput()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_frontend_port_write_iops.assert_called_once_with(
            self.idx)

    @patches.unity_client
    def test_frontend_port_write_iops_column(self, unity_client):
        unity_client.get_frontend_ports.return_value = self.test_list
        obj = FrontendPortWriteThroughput. \
            FrontendPortWriteThroughputColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_frontend_ports.assert_called_once()

    @patches.unity_client
    def test_frontend_port_total_byte_rate(self, unity_client):
        unity_client.get_frontend_port_total_byte_rate.return_value = \
            self.test_string
        obj = FrontendPortTotalBandwidth. \
            FrontendPortTotalBandwidth()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_frontend_port_total_byte_rate.assert_called_once_with(
            self.idx)

    @patches.unity_client
    def test_frontend_port_total_byte_rate_column(self, unity_client):
        unity_client.get_frontend_ports.return_value = self.test_list
        obj = FrontendPortTotalBandwidth. \
            FrontendPortTotalBandwidthColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_frontend_ports.assert_called_once()

    @patches.unity_client
    def test_frontend_port_read_byte_rate(self, unity_client):
        unity_client.get_frontend_port_read_byte_rate.return_value = \
            self.test_string
        obj = FrontendPortReadBandwidth. \
            FrontendPortReadBandwidth()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_frontend_port_read_byte_rate.assert_called_once_with(
            self.idx)

    @patches.unity_client
    def test_frontend_port_read_byte_rate_column(self, unity_client):
        unity_client.get_frontend_ports.return_value = self.test_list
        obj = FrontendPortReadBandwidth. \
            FrontendPortReadBandwidthColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_frontend_ports.assert_called_once()

    @patches.unity_client
    def test_frontend_port_write_byte_rate(self, unity_client):
        unity_client.get_frontend_port_write_byte_rate.return_value = \
            self.test_string
        obj = FrontendPortWriteBandwidth. \
            FrontendPortWriteBandwidth()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_frontend_port_write_byte_rate.assert_called_once_with(
            self.idx)

    @patches.unity_client
    def test_frontend_port_write_byte_rate_column(self, unity_client):
        unity_client.get_frontend_ports.return_value = self.test_list
        obj = FrontendPortWriteBandwidth. \
            FrontendPortWriteBandwidthColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_frontend_ports.assert_called_once()

    # backendPortTable
    @patches.unity_client
    def test_backend_port_id(self, unity_client):
        obj = BackendPortId.BackendPortId()
        self.assertEqual(self.idx,
                         obj.read_get(self.name, self.idx, unity_client))

    @patches.unity_client
    def test_backend_port_id_column(self, unity_client):
        unity_client.get_backend_ports.return_value = self.test_list
        obj = BackendPortId.BackendPortIdColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_backend_ports.assert_called_once()

    @patches.unity_client
    def test_backend_port_name(self, unity_client):
        unity_client.get_backend_port_name.return_value = self.test_string
        obj = BackendPortName.BackendPortName()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_backend_port_name.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_backend_port_name_column(self, unity_client):
        unity_client.get_backend_ports.return_value = self.test_list
        obj = BackendPortName.BackendPortNameColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_backend_ports.assert_called_once()

    @patches.unity_client
    def test_backend_port_type(self, unity_client):
        unity_client.get_backend_port_type.return_value = self.test_string
        obj = BackendPortType.BackendPortType()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_backend_port_type.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_backend_port_type_column(self, unity_client):
        unity_client.get_backend_ports.return_value = self.test_list
        obj = BackendPortType.BackendPortTypeColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_backend_ports.assert_called_once()

    @patches.unity_client
    def test_backend_port_port_number(self, unity_client):
        unity_client.get_backend_port_port_number.return_value = \
            self.test_string
        obj = BackendPortPortNumber.BackendPortPortNumber()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_backend_port_port_number.assert_called_once_with(
            self.idx)

    @patches.unity_client
    def test_backend_port_port_number_column(self, unity_client):
        unity_client.get_backend_ports.return_value = self.test_list
        obj = BackendPortPortNumber.BackendPortPortNumberColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_backend_ports.assert_called_once()

    @patches.unity_client
    def test_backend_port_current_speed(self, unity_client):
        unity_client.get_backend_port_current_speed.return_value = \
            self.test_string
        obj = BackendPortCurrentSpeed.BackendPortCurrentSpeed()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_backend_port_current_speed.assert_called_once_with(
            self.idx)

    @patches.unity_client
    def test_backend_port_current_speed_column(self, unity_client):
        unity_client.get_backend_ports.return_value = self.test_list
        obj = BackendPortCurrentSpeed. \
            BackendPortCurrentSpeedColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_backend_ports.assert_called_once()

    @patches.unity_client
    def test_backend_port_parent_io_module(self, unity_client):
        unity_client.get_backend_port_parent_io_module.return_value = \
            self.test_string
        obj = BackendPortParentIoModule.BackendPortParentIoModule()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_backend_port_parent_io_module.assert_called_once_with(
            self.idx)

    @patches.unity_client
    def test_backend_port_parent_io_module_column(self, unity_client):
        unity_client.get_backend_ports.return_value = self.test_list
        obj = BackendPortParentIoModule. \
            BackendPortParentIoModuleColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_backend_ports.assert_called_once()

    @patches.unity_client
    def test_backend_port_parent_sp(self, unity_client):
        unity_client.get_backend_port_parent_sp.return_value = self.test_string
        obj = BackendPortParentStorageProcessor. \
            BackendPortParentStorageProcessor()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_backend_port_parent_sp.assert_called_once_with(
            self.idx)

    @patches.unity_client
    def test_backend_port_parent_sp_column(self, unity_client):
        unity_client.get_backend_ports.return_value = self.test_list
        obj = BackendPortParentStorageProcessor. \
            BackendPortParentStorageProcessorColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_backend_ports.assert_called_once()

    @patches.unity_client
    def test_backend_port_status(self, unity_client):
        unity_client.get_backend_port_health_status.return_value = \
            self.test_string
        obj = BackendPortStatus.BackendPortStatus()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_backend_port_health_status.assert_called_once_with(
            self.idx)

    @patches.unity_client
    def test_backend_port_status_column(self, unity_client):
        unity_client.get_backend_ports.return_value = self.test_list
        obj = BackendPortStatus.BackendPortStatusColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_backend_ports.assert_called_once()

    # hostTable
    @patches.unity_client
    def test_host_id(self, unity_client):
        obj = HostId.HostId()
        self.assertEqual(self.idx,
                         obj.read_get(self.name, self.idx, unity_client))

    @patches.unity_client
    def test_host_id_column(self, unity_client):
        unity_client.get_hosts.return_value = self.test_list
        obj = HostId.HostIdColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_hosts.assert_called_once()

    @patches.unity_client
    def test_host_name(self, unity_client):
        unity_client.get_host_name.return_value = self.test_string
        obj = HostName.HostName()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_host_name.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_host_name_column(self, unity_client):
        unity_client.get_hosts.return_value = self.test_list
        obj = HostName.HostNameColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_hosts.assert_called_once()

    @patches.unity_client
    def test_host_network_address(self, unity_client):
        unity_client.get_host_network_address.return_value = self.test_string
        obj = HostNetworkAddress.HostNetworkAddress()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_host_network_address.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_host_network_address_column(self, unity_client):
        unity_client.get_hosts.return_value = self.test_list
        obj = HostNetworkAddress.HostNetworkAddressColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_hosts.assert_called_once()

    @patches.unity_client
    def test_host_initiators(self, unity_client):
        unity_client.get_host_initiators.return_value = self.test_string
        obj = HostInitiators.HostInitiators()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_host_initiators.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_host_initiators_column(self, unity_client):
        unity_client.get_hosts.return_value = self.test_list
        obj = HostInitiators.HostInitiatorsColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_hosts.assert_called_once()

    @patches.unity_client
    def test_host_os_version(self, unity_client):
        unity_client.get_host_os_type.return_value = self.test_string
        obj = HostOperationSystemVersion. \
            HostOperationSystemVersion()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_host_os_type.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_host_os_version_column(self, unity_client):
        unity_client.get_hosts.return_value = self.test_list
        obj = HostOperationSystemVersion. \
            HostOperationSystemVersionColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_hosts.assert_called_once()

    @patches.unity_client
    def test_host_assigned_volumes(self, unity_client):
        unity_client.get_host_assigned_volumes.return_value = self.test_string
        obj = HostAssignedStorageVolumes. \
            HostAssignedStorageVolumes()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_host_assigned_volumes.assert_called_once_with(
            self.idx)

    @patches.unity_client
    def test_host_assigned_volumes_column(self, unity_client):
        unity_client.get_hosts.return_value = self.test_list
        obj = HostAssignedStorageVolumes. \
            HostAssignedStorageVolumesColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_hosts.assert_called_once()

    # enclosureTable
    @patches.unity_client
    def test_enclosure_id(self, unity_client):
        unity_client.get_enclosure_id.return_value = self.test_string
        obj = EnclosureId.EnclosureId()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_enclosure_id.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_enclosure_id_column(self, unity_client):
        unity_client.get_enclosures.return_value = self.test_list
        obj = EnclosureId.EnclosureIdColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_enclosures.assert_called_once()

    @patches.unity_client
    def test_enclosure_name(self, unity_client):
        unity_client.get_enclosure_name.return_value = self.test_string
        obj = EnclosureName.EnclosureName()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_enclosure_name.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_enclosure_name_column(self, unity_client):
        unity_client.get_enclosures.return_value = self.test_list
        obj = EnclosureName.EnclosureNameColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_enclosures.assert_called_once()

    @patches.unity_client
    def test_enclosure_model(self, unity_client):
        unity_client.get_enclosure_model.return_value = self.test_string
        obj = EnclosureModel.EnclosureModel()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_enclosure_model.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_enclosure_model_column(self, unity_client):
        unity_client.get_enclosures.return_value = self.test_list
        obj = EnclosureModel.EnclosureModelColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_enclosures.assert_called_once()

    @patches.unity_client
    def test_enclosure_serial_number(self, unity_client):
        unity_client.get_enclosure_serial_number.return_value = \
            self.test_string
        obj = EnclosureSerialNumber.EnclosureSerialNumber()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_enclosure_serial_number.assert_called_once_with(
            self.idx)

    @patches.unity_client
    def test_enclosure_serial_number_column(self, unity_client):
        unity_client.get_enclosures.return_value = self.test_list
        obj = EnclosureSerialNumber.EnclosureSerialNumberColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_enclosures.assert_called_once()

    @patches.unity_client
    def test_enclosure_part_number(self, unity_client):
        unity_client.get_enclosure_part_number.return_value = self.test_string
        obj = EnclosurePartNumber.EnclosurePartNumber()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_enclosure_part_number.assert_called_once_with(
            self.idx)

    @patches.unity_client
    def test_enclosure_part_number_column(self, unity_client):
        unity_client.get_enclosures.return_value = self.test_list
        obj = EnclosurePartNumber.EnclosurePartNumberColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_enclosures.assert_called_once()

    @patches.unity_client
    def test_enclosure_health_status(self, unity_client):
        unity_client.get_enclosure_health_status.return_value = \
            self.test_string
        obj = EnclosureHealthStatus.EnclosureHealthStatus()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_enclosure_health_status.assert_called_once_with(
            self.idx)

    @patches.unity_client
    def test_enclosure_health_status_column(self, unity_client):
        unity_client.get_enclosures.return_value = self.test_list
        obj = EnclosureHealthStatus.EnclosureHealthStatusColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_enclosures.assert_called_once()

    @patches.unity_client
    def test_enclosure_current_power(self, unity_client):
        unity_client.get_enclosure_current_power.return_value = \
            self.test_string
        obj = EnclosureCurrentPower.EnclosureCurrentPower()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_enclosure_current_power.assert_called_once_with(
            self.idx)

    @patches.unity_client
    def test_enclosure_current_power_column(self, unity_client):
        unity_client.get_enclosures.return_value = self.test_list
        obj = EnclosureCurrentPower.EnclosureCurrentPowerColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_enclosures.assert_called_once()

    @patches.unity_client
    def test_enclosure_avg_power(self, unity_client):
        unity_client.get_enclosure_avg_power.return_value = self.test_string
        obj = EnclosureAveragePower.EnclosureAveragePower()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_enclosure_avg_power.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_enclosure_avg_power_column(self, unity_client):
        unity_client.get_enclosures.return_value = self.test_list
        obj = EnclosureAveragePower.EnclosureAveragePowerColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_enclosures.assert_called_once()

    @patches.unity_client
    def test_enclosure_max_power(self, unity_client):
        unity_client.get_enclosure_max_power.return_value = self.test_string
        obj = EnclosureMaxPower.EnclosureMaxPower()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_enclosure_max_power.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_enclosure_max_power_column(self, unity_client):
        unity_client.get_enclosures.return_value = self.test_list
        obj = EnclosureMaxPower.EnclosureMaxPowerColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_enclosures.assert_called_once()

    @patches.unity_client
    def test_enclosure_current_temperature(self, unity_client):
        unity_client.get_enclosure_current_temperature.return_value = \
            self.test_string
        obj = EnclosureCurrentTemperature. \
            EnclosureCurrentTemperature()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_enclosure_current_temperature.assert_called_once_with(
            self.idx)

    @patches.unity_client
    def test_enclosure_current_temperature_column(self, unity_client):
        unity_client.get_enclosures.return_value = self.test_list
        obj = EnclosureCurrentTemperature. \
            EnclosureCurrentTemperatureColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_enclosures.assert_called_once()

    @patches.unity_client
    def test_enclosure_avg_temperature(self, unity_client):
        unity_client.get_enclosure_avg_temperature.return_value = \
            self.test_string
        obj = EnclosureAverageTemperature. \
            EnclosureAverageTemperature()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_enclosure_avg_temperature.assert_called_once_with(
            self.idx)

    @patches.unity_client
    def test_enclosure_avg_temperature_column(self, unity_client):
        unity_client.get_enclosures.return_value = self.test_list
        obj = EnclosureAverageTemperature. \
            EnclosureAverageTemperatureColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_enclosures.assert_called_once()

    @patches.unity_client
    def test_enclosure_max_temperature(self, unity_client):
        unity_client.get_enclosure_max_temperature.return_value = \
            self.test_string
        obj = EnclosureMaxTemperature.EnclosureMaxTemperature()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_enclosure_max_temperature.assert_called_once_with(
            self.idx)

    @patches.unity_client
    def test_enclosure_max_temperature_column(self, unity_client):
        unity_client.get_enclosures.return_value = self.test_list
        obj = EnclosureMaxTemperature. \
            EnclosureMaxTemperatureColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_enclosures.assert_called_once()

    # powerSupplyTable
    @patches.unity_client
    def test_power_supply_id(self, unity_client):
        obj = PowerSupplyId.PowerSupplyId()
        self.assertEqual(self.idx,
                         obj.read_get(self.name, self.idx, unity_client))

    @patches.unity_client
    def test_power_supply_id_column(self, unity_client):
        unity_client.get_power_supplies.return_value = self.test_list
        obj = PowerSupplyId.PowerSupplyIdColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_power_supplies.assert_called_once()

    @patches.unity_client
    def test_power_supply_name(self, unity_client):
        unity_client.get_power_supply_name.return_value = self.test_string
        obj = PowerSupplyName.PowerSupplyName()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_power_supply_name.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_power_supply_name_column(self, unity_client):
        unity_client.get_power_supplies.return_value = self.test_list
        obj = PowerSupplyName.PowerSupplyNameColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_power_supplies.assert_called_once()

    @patches.unity_client
    def test_power_supply_manufacturer(self, unity_client):
        unity_client.get_power_supply_manufacturer.return_value = \
            self.test_string
        obj = PowerSupplyManufacturer.PowerSupplyManufacturer()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_power_supply_manufacturer.assert_called_once_with(
            self.idx)

    @patches.unity_client
    def test_power_supply_manufacturer_column(self, unity_client):
        unity_client.get_power_supplies.return_value = self.test_list
        obj = PowerSupplyManufacturer. \
            PowerSupplyManufacturerColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_power_supplies.assert_called_once()

    @patches.unity_client
    def test_power_supply_model(self, unity_client):
        unity_client.get_power_supply_model.return_value = self.test_string
        obj = PowerSupplyModel.PowerSupplyModel()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_power_supply_model.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_power_supply_model_column(self, unity_client):
        unity_client.get_power_supplies.return_value = self.test_list
        obj = PowerSupplyModel.PowerSupplyModelColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_power_supplies.assert_called_once()

    @patches.unity_client
    def test_power_supply_firmware_version(self, unity_client):
        unity_client.get_power_supply_firmware_version.return_value = \
            self.test_string
        obj = PowerSupplyFirmwareVersion. \
            PowerSupplyFirmwareVersion()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_power_supply_firmware_version.assert_called_once_with(
            self.idx)

    @patches.unity_client
    def test_power_supply_firmware_version_column(self, unity_client):
        unity_client.get_power_supplies.return_value = self.test_list
        obj = PowerSupplyFirmwareVersion. \
            PowerSupplyFirmwareVersionColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_power_supplies.assert_called_once()

    @patches.unity_client
    def test_power_supply_parent_enclosure(self, unity_client):
        unity_client.get_power_supply_parent_enclosure.return_value = \
            self.test_string
        obj = PowerSupplyParentEnclosure. \
            PowerSupplyParentEnclosure()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_power_supply_parent_enclosure.assert_called_once_with(
            self.idx)

    @patches.unity_client
    def test_power_supply_parent_enclosure_column(self, unity_client):
        unity_client.get_power_supplies.return_value = self.test_list
        obj = PowerSupplyParentEnclosure. \
            PowerSupplyParentEnclosureColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_power_supplies.assert_called_once()

    @patches.unity_client
    def test_power_supply_sp(self, unity_client):
        unity_client.get_power_supply_sp.return_value = self.test_string
        obj = PowerSupplyStorageProcessor. \
            PowerSupplyStorageProcessor()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_power_supply_sp.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_power_supply_sp_column(self, unity_client):
        unity_client.get_power_supplies.return_value = self.test_list
        obj = PowerSupplyStorageProcessor. \
            PowerSupplyStorageProcessorColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_power_supplies.assert_called_once()

    @patches.unity_client
    def test_power_supply_status(self, unity_client):
        unity_client.get_power_supply_health_status.return_value = \
            self.test_string
        obj = PowerSupplyHealthStatus.PowerSupplyHealthStatus()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_power_supply_health_status.assert_called_once_with(
            self.idx)

    @patches.unity_client
    def test_power_supply_status_column(self, unity_client):
        unity_client.get_power_supplies.return_value = self.test_list
        obj = PowerSupplyHealthStatus. \
            PowerSupplyHealthStatusColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_power_supplies.assert_called_once()

    # fanTable
    @patches.unity_client
    def test_fan_id(self, unity_client):
        obj = FanId.FanId()
        self.assertEqual(self.idx,
                         obj.read_get(self.name, self.idx, unity_client))

    @patches.unity_client
    def test_fan_id_column(self, unity_client):
        unity_client.get_fans.return_value = self.test_list
        obj = FanId.FanIdColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_fans.assert_called_once()

    @patches.unity_client
    def test_fan_name(self, unity_client):
        unity_client.get_fan_name.return_value = self.test_string
        obj = FanName.FanName()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_fan_name.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_fan_name_column(self, unity_client):
        unity_client.get_fans.return_value = self.test_list
        obj = FanName.FanNameColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_fans.assert_called_once()

    @patches.unity_client
    def test_fan_slot_number(self, unity_client):
        unity_client.get_fan_slot_number.return_value = self.test_string
        obj = FanSlotNumber.FanSlotNumber()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_fan_slot_number.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_fan_slot_number_column(self, unity_client):
        unity_client.get_fans.return_value = self.test_list
        obj = FanSlotNumber.FanSlotNumberColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_fans.assert_called_once()

    @patches.unity_client
    def test_fan_parent_enclosure(self, unity_client):
        unity_client.get_fan_parent_enclosure.return_value = self.test_string
        obj = FanParentEnclosure.FanParentEnclosure()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_fan_parent_enclosure.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_fan_parent_enclosure_column(self, unity_client):
        unity_client.get_fans.return_value = self.test_list
        obj = FanParentEnclosure.FanParentEnclosureColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_fans.assert_called_once()

    @patches.unity_client
    def test_fan_status(self, unity_client):
        unity_client.get_fan_health_status.return_value = self.test_string
        obj = FanHealthStatus.FanHealthStatus()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_fan_health_status.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_fan_status_column(self, unity_client):
        unity_client.get_fans.return_value = self.test_list
        obj = FanHealthStatus.FanHealthStatusColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_fans.assert_called_once()

    # BBUTable
    @patches.unity_client
    def test_bbu_id(self, unity_client):
        obj = BbuId.BbuId()
        self.assertEqual(self.idx,
                         obj.read_get(self.name, self.idx, unity_client))

    @patches.unity_client
    def test_bbu_id_column(self, unity_client):
        unity_client.get_bbus.return_value = self.test_list
        obj = BbuId.BbuIdColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_bbus.assert_called_once()

    @patches.unity_client
    def test_bbu_name(self, unity_client):
        unity_client.get_bbu_name.return_value = self.test_string
        obj = BbuName.BbuName()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_bbu_name.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_bbu_name_column(self, unity_client):
        unity_client.get_bbus.return_value = self.test_list
        obj = BbuName.BbuNameColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_bbus.assert_called_once()

    @patches.unity_client
    def test_bbu_manufacturer(self, unity_client):
        unity_client.get_bbu_manufacturer.return_value = self.test_string
        obj = BbuManufacturer.BbuManufacturer()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_bbu_manufacturer.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_bbu_manufacturer_column(self, unity_client):
        unity_client.get_bbus.return_value = self.test_list
        obj = BbuManufacturer.BbuManufacturerColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_bbus.assert_called_once()

    @patches.unity_client
    def test_bbu_model(self, unity_client):
        unity_client.get_bbu_model.return_value = self.test_string
        obj = BbuModel.BbuModel()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_bbu_model.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_bbu_model_column(self, unity_client):
        unity_client.get_bbus.return_value = self.test_list
        obj = BbuModel.BbuModelColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_bbus.assert_called_once()

    @patches.unity_client
    def test_bbu_firmware_version(self, unity_client):
        unity_client.get_bbu_firmware_version.return_value = self.test_string
        obj = BbuFirmwareVersion.BbuFirmwareVersion()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_bbu_firmware_version.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_bbu_firmware_version_column(self, unity_client):
        unity_client.get_bbus.return_value = self.test_list
        obj = BbuFirmwareVersion.BbuFirmwareVersionColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_bbus.assert_called_once()

    @patches.unity_client
    def test_bbu_parent_sp(self, unity_client):
        unity_client.get_bbu_parent_sp.return_value = self.test_string
        obj = BbuParentStorageProcessor. \
            BbuParentStorageProcessor()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_bbu_parent_sp.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_bbu_parent_sp_column(self, unity_client):
        unity_client.get_bbus.return_value = self.test_list
        obj = BbuParentStorageProcessor. \
            BbuParentStorageProcessorColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_bbus.assert_called_once()

    @patches.unity_client
    def test_bbu_status(self, unity_client):
        unity_client.get_bbu_health_status.return_value = self.test_string
        obj = BbuHealthStatus.BbuHealthStatus()
        self.assertEqual(self.test_string,
                         obj.read_get(self.name, self.idx, unity_client))
        unity_client.get_bbu_health_status.assert_called_once_with(self.idx)

    @patches.unity_client
    def test_bbu_status_column(self, unity_client):
        unity_client.get_bbus.return_value = self.test_list
        obj = BbuHealthStatus.BbuHealthStatusColumn()
        self.assertEqual(self.test_list,
                         obj.get_idx(self.name, self.idx, unity_client))
        unity_client.get_bbus.assert_called_once()
