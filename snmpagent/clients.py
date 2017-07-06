from storops import UnitySystem


class CachedUnityClientManager(object):
    def __init__(self):
        self._cache = {}

    def get_unity_client(self, name, *args):
        if name not in self._cache:
            unity_client = UnityClient(*args)
            self._cache[name] = unity_client
        else:
            unity_client = self._cache[name]
        return unity_client


class UnityClient(object):
    manager = CachedUnityClientManager()

    def __init__(self, host=None, username=None, password=None, port=443):
        self.unity_system = UnitySystem(host=host, username=username, password=password, port=port)
        self.unity_system.enable_perf_stats()

    @classmethod
    def get_unity_client(cls, name, *args):
        return cls.manager.get_unity_client(name, *args)

    # system
    def get_agent_version(self):
        return "1.0"

    def get_mib_version(self):
        return "1.0"

    def get_manufacturer(self):
        return "DellEMC"

    def get_model(self):
        return self.unity_system.model

    def get_serial_number(self):
        return self.unity_system.serial_number

    def get_operation_environment_version(self):
        return self.unity_system.system_version

    def get_management_ip(self):
        pass

    def get_current_power(self):
        self.unity_system.update()
        return str(self.unity_system.current_power)

    def get_avg_power(self):
        self.unity_system.update()
        return str(self.unity_system.avg_power)

    def get_number_of_sp(self):
        return len(self.unity_system.get_sp())

    def get_number_of_enclosure(self):
        return len(self.get_enclosures())

    def get_number_of_power_supply(self):
        return len(self.unity_system.get_power_supply())

    def get_number_of_fan(self):
        return len(self.unity_system.get_fan())

    def get_number_of_disk(self):
        return len(self.unity_system.get_disk())

    def get_number_of_frontend_port(self):
        return len(self.get_frontend_ports())

    def get_number_of_backend_port(self):
        return len(self.unity_system.get_sas_port())

    # storageProcessorTable
    def get_sps(self):
        return [pool.name for pool in self.unity_system.get_sp()]

    def get_sp_serial_number(self, name):
        sp = self.unity_system.get_sp(name=name)
        return sp.emc_serial_number

    def get_sp_health_status(self, name):
        sp = self.unity_system.get_sp(name=name)
        return sp.health.value.name

    def get_sp_utilization(self, name):
        sp = self.unity_system.get_sp(name=name)
        return str(sp.utilization)

    def get_sp_block_read_iops(self, name):
        sp = self.unity_system.get_sp(name=name)
        return str(sp.block_read_iops)

    def get_sp_block_write_iops(self, name):
        sp = self.unity_system.get_sp(name=name)
        return str(sp.block_write_iops)

    def get_sp_block_cache_read_hit_ratio(self, name):
        sp = self.unity_system.get_sp(name=name)
        return str(sp.block_cache_read_hit_ratio)

    def get_sp_block_cache_write_hit_ratio(self, name):
        sp = self.unity_system.get_sp(name=name)
        return str(sp.block_cache_write_hit_ratio)

    # poolTable
    def get_pools(self):
        return [pool.name for pool in self.unity_system.get_pool()]

    def get_pool_disk_types(self, name):
        pool = self.unity_system.get_pool(name=name)
        if pool.tiers:
            return ', '.join(x.name for x in pool.tiers)
        else:
            return

    def get_pool_raid_levels(self, name):
        pool = self.unity_system.get_pool(name=name)
        return pool.raid_type.name

    def get_pool_fast_cache_status(self, name):
        pool = self.unity_system.get_pool(name=name)
        return str(pool.is_fast_cache_enabled)

    def get_pool_number_of_disk(self, name):
        pool = self.unity_system.get_pool(name=name)
        if pool.tiers:
            # return str(sum(x.disk_count for x in pool.tiers))
            return sum(x.disk_count for x in pool.tiers)
        else:
            return

    def get_pool_size_total(self, name):
        pool = self.unity_system.get_pool(name=name)
        return str(pool.size_total)

    def get_pool_size_free(self, name):
        pool = self.unity_system.get_pool(name=name)
        return str(pool.size_free)

    def get_pool_size_used(self, name):
        pool = self.unity_system.get_pool(name=name)
        return str(pool.size_used)

    def get_pool_size_ultilization(self, name):
        pool = self.unity_system.get_pool(name=name)
        return str(pool.size_used / pool.size_total)

    # volumeTable
    def get_luns(self):
        # self.luns = self.unity_system.get_lun()
        # return [lun.id for lun in self.luns]
        return [lun.id for lun in self.unity_system.get_lun()]

        # def get_lun_id(self, idx):
        # luns = self.unity_system.get_lun()
        # luns = self.luns
        # return luns[idx-1].id

    def get_lun_name(self, id):
        # luns = self.unity_system.get_lun()
        # luns = self.luns
        # return luns[idx-1].name
        lun = self.unity_system.get_lun(_id=id)
        return lun.name

    def get_lun_raid_type(self, id):
        # luns = self.unity_system.get_lun()
        # luns = self.luns
        # return luns[idx-1].pool.raid_type.name
        lun = self.unity_system.get_lun(_id=id)
        if lun.pool:
            return lun.pool.raid_type.name
        else:
            return

    def get_lun_size_allocated(self, id):
        lun = self.unity_system.get_lun(_id=id)
        return str(lun.size_allocated)

    def get_lun_size_total(self, id):
        lun = self.unity_system.get_lun(_id=id)
        return str(lun.size_total)

    def get_lun_health_status(self, id):
        lun = self.unity_system.get_lun(_id=id)
        return lun.health.value.name

    def get_lun_fast_cache_status(self, id):
        lun = self.unity_system.get_lun(_id=id)
        return str(lun.pool.is_fast_cache_enabled)

    def get_lun_default_sp(self, id):
        lun = self.unity_system.get_lun(_id=id)
        return lun.default_node.name

    def get_lun_current_sp(self, id):
        lun = self.unity_system.get_lun(_id=id)
        return lun.current_node.name

    def get_lun_read_iops(self, id):
        lun = self.unity_system.get_lun(_id=id)
        return str(lun.read_iops)

    def get_lun_write_iops(self, id):
        lun = self.unity_system.get_lun(_id=id)
        return str(lun.write_iops)

    def get_lun_utilization(self, id):
        lun = self.unity_system.get_lun(_id=id)
        return str(lun.utilization)

    def get_lun_host_access(self, id):
        lun = self.unity_system.get_lun(_id=id)
        if lun.host_access:
            return ', '.join(x.host.name for x in lun.host_access)
        else:
            return

    # diskTable
    def get_disks(self):
        return [disk.name for disk in self.unity_system.get_disk()]

    def get_disk_model(self, name):
        disk = self.unity_system.get_disk(name=name)
        return disk.model

    def get_disk_serial_number(self, name):
        disk = self.unity_system.get_disk(name=name)
        return disk.emc_serial_number

    def get_disk_version(self, name):
        disk = self.unity_system.get_disk(name=name)
        return disk.version

    def get_disk_type(self, name):
        disk = self.unity_system.get_disk(name=name)
        if disk.disk_technology:
            return disk.disk_technology.name
        else:
            return

    def get_disk_slot_number(self, name):
        disk = self.unity_system.get_disk(name=name)
        return str(disk.slot_number)

    def get_disk_health_status(self, name):
        disk = self.unity_system.get_disk(name=name)
        return disk.health.value.name

    def get_disk_raw_size(self, name):
        disk = self.unity_system.get_disk(name=name)
        return str(disk.raw_size)

    def get_disk_current_pool(self, name):
        disk = self.unity_system.get_disk(name=name)
        if disk.pool:
            return disk.pool.name
        else:
            return

    def get_disk_read_iops(self, name):
        disk = self.unity_system.get_disk(name=name)
        return str(disk.read_iops)

    def get_disk_write_iops(self, name):
        disk = self.unity_system.get_disk(name=name)
        return str(disk.write_iops)

    def get_disk_utilization(self, name):
        disk = self.unity_system.get_disk(name=name)
        return str(disk.utilization)

    # frontendPortTable
    def get_frontend_ports(self):
        fc_ports = ['fc_port_' + port.id for port in self.unity_system.get_fc_port()]
        eth_ports = ['eth_port_' + port.id for port in self.unity_system.get_ethernet_port()]
        return fc_ports + eth_ports

    def _get_frontend_port(self, id):
        if id.startswith('fc_port_'):
            id = id.lstrip('fc_port_')
            return self.unity_system.get_fc_port(_id=id)
        if id.startswith('eth_port_'):
            id = id.lstrip('eth_port_')
            return self.unity_system.get_ethernet_port(_id=id)

    def get_frontend_port_id(self, id):
        port = self._get_frontend_port(id)
        return port.id

    def get_frontend_port_name(self, id):
        port = self._get_frontend_port(id)
        return port.name

    def get_frontend_port_address(self, id):
        port = self._get_frontend_port(id)
        if hasattr(port, 'mac_address'):
            return port.mac_address

    def get_frontend_port_type(self, id):
        port = self._get_frontend_port(id)
        return port.connector_type.name

    def get_frontend_port_current_speed(self, id):
        port = self._get_frontend_port(id)
        if hasattr(port, 'speed'):
            if port.speed:
                return port.speed.name

    def get_frontend_port_supported_speed(self, id):
        port = self._get_frontend_port(id)
        if hasattr(port, 'supported_speeds'):
            return ', '.join(x.name for x in port.supported_speeds)

    def get_frontend_port_health_status(self, id):
        port = self._get_frontend_port(id)
        return port.health.value.name

    # backendPortTable
    def get_backend_ports(self):
        return [port.id for port in self.unity_system.get_sas_port()]

    def get_backend_port_name(self, id):
        port = self.unity_system.get_sas_port(_id=id)
        return port.name

    def get_backend_port_type(self, id):
        port = self.unity_system.get_sas_port(_id=id)
        return port.connector_type.name

    def get_backend_port_port_number(self, id):
        port = self.unity_system.get_sas_port(_id=id)
        return str(port.port)

    def get_backend_port_current_speed(self, id):
        port = self.unity_system.get_sas_port(_id=id)
        if port.current_speed:
            return port.current_speed.name
        else:
            return

    def get_backend_port_parent_io_module(self, id):
        port = self.unity_system.get_sas_port(_id=id)
        if port.parent_io_module:
            return port.parent_io_module.name
        else:
            return

    def get_backend_port_parent_sp(self, id):
        port = self.unity_system.get_sas_port(_id=id)
        if port.parent_storage_processor:
            return port.parent_storage_processor.name
        else:
            return

    def get_backend_port_health_status(self, id):
        port = self.unity_system.get_sas_port(_id=id)
        return port.health.value.name

    # hostTable
    def get_hosts(self):
        return [host.name for host in self.unity_system.get_host()]

    def get_host_network_address(self, name):
        host = self.unity_system.get_host(name=name)
        return ', '.join(host.ip_list)

    def get_host_initiators(self, name):
        host = self.unity_system.get_host(name=name)
        initiators = []
        if host.iscsi_host_initiators:
            initiators.extend(x.initiator_id for x in host.iscsi_host_initiators)
        if host.fc_host_initiators:
            initiators.extend(x.initiator_id for x in host.fc_host_initiators)
        return ', '.join(initiators)

    def get_host_os_type(self, name):
        host = self.unity_system.get_host(name=name)
        return host.os_type

    def get_host_assigned_volumes(self, name):
        host = self.unity_system.get_host(name=name)
        if host.host_luns:
            return ', '.join(x.lun.name for x in host.host_luns)
        else:
            return

    # enclosureTable
    def get_enclosures(self):
        daes = ['dae_' + dae.name for dae in self.unity_system.get_dae()]
        dpes = ['dpe_' + dpe.name for dpe in self.unity_system.get_dpe()]
        return daes + dpes

    def _get_enclosure(self, name):
        if name.startswith('dae_'):
            name = name.lstrip('dae_')
            return self.unity_system.get_dae(name=name)
        if name.startswith('dpe_'):
            name = name.lstrip('dpe_')
            return self.unity_system.get_dpe(name=name)

    def get_enclosure_name(self, name):
        enclosure = self._get_enclosure(name)
        return enclosure.name

    def get_enclosure_model(self, name):
        enclosure = self._get_enclosure(name)
        return enclosure.model

    def get_enclosure_serial_number(self, name):
        enclosure = self._get_enclosure(name)
        return enclosure.emc_serial_number

    def get_enclosure_part_number(self, name):
        enclosure = self._get_enclosure(name)
        return enclosure.emc_part_number

    def get_enclosure_health_status(self, name):
        enclosure = self._get_enclosure(name)
        return enclosure.health.value.name

    def get_enclosure_current_power(self, name):
        enclosure = self._get_enclosure(name)
        return str(enclosure.current_power)

    def get_enclosure_avg_power(self, name):
        enclosure = self._get_enclosure(name)
        return str(enclosure.avg_power)

    def get_enclosure_max_power(self, name):
        enclosure = self._get_enclosure(name)
        return str(enclosure.max_power)

    def get_enclosure_current_temperature(self, name):
        enclosure = self._get_enclosure(name)
        return str(enclosure.current_temperature)

    def get_enclosure_avg_temperature(self, name):
        enclosure = self._get_enclosure(name)
        return str(enclosure.avg_temperature)

    def get_enclosure_max_temperature(self, name):
        enclosure = self._get_enclosure(name)
        return str(enclosure.max_temperature)

    # powerSupplyTable
    def get_power_supplies(self):
        return [power_supply.name for power_supply in self.unity_system.get_power_supply()]

    def get_power_supply_manufacturer(self, name):
        power_supply = self.unity_system.get_power_supply(name=name)
        return power_supply.manufacturer

    def get_power_supply_model(self, name):
        power_supply = self.unity_system.get_power_supply(name=name)
        return power_supply.model

    def get_power_supply_firmware_version(self, name):
        power_supply = self.unity_system.get_power_supply(name=name)
        return power_supply.firmware_version

    def get_power_supply_parent_enclosure(self, name):
        power_supply = self.unity_system.get_power_supply(name=name)
        parents = []
        if power_supply.parent_dpe:
            parents.append(power_supply.parent_dpe)
        if power_supply.parent_dae:
            parents.append(power_supply.parent_dae)
        return ', '.join(x.name for x in parents)

    def get_power_supply_sp(self, name):
        power_supply = self.unity_system.get_power_supply(name=name)
        return power_supply.storage_processor.name

    def get_power_supply_health_status(self, name):
        power_supply = self.unity_system.get_power_supply(name=name)
        return power_supply.health.value.name

    # fanTable
    def get_fans(self):
        return [fan.name for fan in self.unity_system.get_fan()]

    def get_fan_slot_number(self, name):
        fan = self.unity_system.get_fan(name=name)
        return str(fan.slot_number)

    def get_fan_parent_enclosure(self, name):
        fan = self.unity_system.get_fan(name=name)
        parents = []
        if fan.parent_dpe:
            parents.append(fan.parent_dpe)
        if fan.parent_dae:
            parents.append(fan.parent_dae)
        return ', '.join(x.name for x in parents)

    def get_fan_health_status(self, name):
        fan = self.unity_system.get_fan(name=name)
        return fan.health.value.name

    # BBUTable
    def get_bbus(self):
        return [bbu.name for bbu in self.unity_system.get_battery()]

    def get_bbu_manufacturer(self, name):
        bbu = self.unity_system.get_battery(name=name)
        return bbu.manufacturer

    def get_bbu_model(self, name):
        bbu = self.unity_system.get_battery(name=name)
        return bbu.model

    def get_bbu_firmware_version(self, name):
        bbu = self.unity_system.get_battery(name=name)
        return bbu.firmware_version

    def get_bbu_parent_sp(self, name):
        bbu = self.unity_system.get_battery(name=name)
        return bbu.parent_storage_processor.name

    def get_bbu_health_status(self, name):
        bbu = self.unity_system.get_battery(name=name)
        return bbu.health.value.name
