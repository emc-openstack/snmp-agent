import logging
import math
from functools import wraps, partial

import six

import storops

LOG = logging.getLogger(__name__)
NONE_STRING = 'n/a'


def to_string(func):
    @wraps(func)
    def _inner(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            if result != '':
                rst = str(result)
            else:
                # rst = snmp_ex.UnityResponseError('Result: {}'.format(result))
                rst = NONE_STRING

        # except snmp_ex.UnityException:
        #     raise

        except Exception:
            # raise snmp_ex.UnityResponseError('{}: {}'
            # .format(e.__class__.__name__, e))
            rst = NONE_STRING

        return rst

    return _inner


def to_number(func=None, length=3):
    if func is None:
        return partial(to_number, length=length)

    @wraps(func)
    def _inner(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            if isinstance(result, six.integer_types):
                rst = result
            elif isinstance(result, str) and result.lower() == 'nan':
                rst = NONE_STRING
            elif isinstance(result, float):
                if math.isnan(result):
                    rst = NONE_STRING
                else:
                    rst = round(result, length)
            else:
                # raise snmp_ex.UnityResponseError('Result: {}'.format(result))
                rst = 0

        # except snmp_ex.UnityException:
        #     raise

        except Exception:
            # raise snmp_ex.UnityResponseError(
            #     '{}: {}'.format(e.__class__.__name__, e))
            rst = 0

        return rst

    return _inner


def change_size_unit(func=None, from_unit='b', to_unit='gb'):
    if func is None:
        return partial(change_size_unit, from_unit=from_unit, to_unit=to_unit)

    unit_dict = {'tb': 2 ** 40,
                 'gb': 2 ** 30,
                 'mb': 2 ** 20,
                 'kb': 2 ** 10,
                 'b': 1}
    fac = unit_dict.get(from_unit, 1)
    den = unit_dict.get(to_unit, 2 ** 30)

    @wraps(func)
    def _inner(*args, **kwargs):
        result = func(*args, **kwargs)
        if result == 0:
            return result
        else:
            return float(result) * fac / den

    return _inner


def change_time_unit(func=None, from_unit='us', to_unit='ms'):
    if func is None:
        return partial(change_time_unit, from_unit=from_unit, to_unit=to_unit)

    unit_dict = {'s': 1000000,
                 'ms': 1000,
                 'us': 1}
    fac = unit_dict.get(from_unit, 1)
    den = unit_dict.get(to_unit, 1000)

    @wraps(func)
    def _inner(*args, **kwargs):
        result = func(*args, **kwargs)
        if result == 0:
            return result
        else:
            return float(result) * fac / den

    return _inner


class CachedUnityClientManager(object):
    def __init__(self):
        self._cache = {}

    def get_unity_client(self, name, *args, **kwargs):
        if name not in self._cache:
            unity_client = UnityClient(*args, **kwargs)
            self._cache[name] = unity_client
        else:
            unity_client = self._cache[name]
        return unity_client


class UnityClient(object):
    manager = CachedUnityClientManager()

    def __init__(self, host=None, username=None, password=None, port=443,
                 cache_interval=None):
        password = password.raw if hasattr(password, 'raw') else password
        if cache_interval is None:
            cache_interval = 30
        LOG.debug('Create UnitySystem: host: {}, username: {}, port: {}'
                  .format(host, username, port))
        self.unity_system = storops.UnitySystem(host=host, username=username,
                                                password=password, port=port,
                                                retries=0,
                                                cache_interval=cache_interval)
        LOG.debug('Enabling metric query')
        self.unity_system.enable_perf_stats()

    @classmethod
    def get_unity_client(cls, name, *args, **kwargs):
        return cls.manager.get_unity_client(name, *args, **kwargs)

    def _get_item(self, items, **filter):
        for k, v in filter.items():
            items = [item for item in items if getattr(item, k) == v]

        if len(items) >= 1:
            return items[0]

    # system
    @to_string
    def get_agent_version(self):
        return "1.0"

    @to_string
    def get_mib_version(self):
        return "1.0"

    @to_string
    def get_manufacturer(self):
        return "DellEMC"

    @to_string
    def get_model(self):
        return self.unity_system.model

    @to_string
    def get_serial_number(self):
        return self.unity_system.serial_number

    @to_string
    def get_operation_environment_version(self):
        return self.unity_system.system_version

    @to_string
    def get_mgmt_ip(self):
        return ', '.join(
            x.ip_address for x in self.unity_system.get_mgmt_interface())

    @to_string
    def get_current_power(self):
        self.unity_system.update()
        return self.unity_system.current_power

    @to_string
    def get_avg_power(self):
        self.unity_system.update()
        return self.unity_system.avg_power

    @to_number
    def get_number_of_sp(self):
        return len(self.get_sps())

    @to_number
    def get_number_of_enclosure(self):
        return len(self.get_enclosures())

    @to_number
    def get_number_of_power_supply(self):
        return len(self.get_power_supplies())

    @to_number
    def get_number_of_fan(self):
        return len(self.get_fans())

    @to_number
    def get_number_of_disk(self):
        return len(self.get_disks())

    @to_number
    def get_number_of_frontend_port(self):
        return len(self.get_frontend_ports())

    @to_number
    def get_number_of_backend_port(self):
        return len(self.get_backend_ports())

    @to_string
    @to_number
    @change_size_unit
    def get_total_capacity(self):
        return sum(
            x.size_total for x in self.unity_system.get_system_capacity())

    @to_string
    @to_number
    @change_size_unit
    def get_used_capacity(self):
        return sum(
            x.size_used for x in self.unity_system.get_system_capacity())

    @to_string
    @to_number
    @change_size_unit
    def get_free_capacity(self):
        return sum(
            x.size_free for x in self.unity_system.get_system_capacity())

    @to_string
    @to_number
    def get_total_iops(self):
        self.unity_system.update()
        return self.unity_system.total_iops

    @to_string
    @to_number
    def get_read_iops(self):
        self.unity_system.update()
        return self.unity_system.read_iops

    @to_string
    @to_number
    def get_write_iops(self):
        self.unity_system.update()
        return self.unity_system.write_iops

    @to_string
    @to_number
    @change_size_unit(to_unit='mb')
    def get_total_byte_rate(self):
        self.unity_system.update()
        return self.unity_system.total_byte_rate

    @to_string
    @to_number
    @change_size_unit(to_unit='mb')
    def get_read_byte_rate(self):
        self.unity_system.update()
        return self.unity_system.read_byte_rate

    @to_string
    @to_number
    @change_size_unit(to_unit='mb')
    def get_write_byte_rate(self):
        self.unity_system.update()
        return self.unity_system.write_byte_rate

    # storageProcessorTable
    def get_sps(self):
        return [pool.id for pool in self.unity_system.get_sp()]

    def _get_sp(self, id):
        return self._get_item(self.unity_system.get_sp(), id=id)

    @to_string
    def get_sp_name(self, id):
        sp = self._get_sp(id)
        return sp.name

    @to_string
    def get_sp_serial_number(self, id):
        sp = self._get_sp(id)
        return sp.emc_serial_number

    @to_string
    def get_sp_health_status(self, id):
        sp = self._get_sp(id)
        return sp.health.value.name

    @to_string
    @to_number
    def get_sp_utilization(self, id):
        sp = self._get_sp(id)
        return sp.utilization

    @to_string
    @to_number
    def get_sp_block_total_iops(self, id):
        sp = self._get_sp(id)
        return sp.block_total_iops

    @to_string
    @to_number
    def get_sp_block_read_iops(self, id):
        sp = self._get_sp(id)
        return sp.block_read_iops

    @to_string
    @to_number
    def get_sp_block_write_iops(self, id):
        sp = self._get_sp(id)
        return sp.block_write_iops

    @to_string
    @to_number
    @change_size_unit(to_unit='mb')
    def get_sp_total_byte_rate(self, id):
        sp = self._get_sp(id)
        return sp.total_byte_rate

    @to_string
    @to_number
    @change_size_unit(to_unit='mb')
    def get_sp_read_byte_rate(self, id):
        sp = self._get_sp(id)
        return sp.read_byte_rate

    @to_string
    @to_number
    @change_size_unit(to_unit='mb')
    def get_sp_write_byte_rate(self, id):
        sp = self._get_sp(id)
        return sp.write_byte_rate

    @to_string
    @to_number()
    def get_sp_cache_dirty_size(self, id):
        sp = self._get_sp(id)
        return sp.block_cache_dirty_size

    @to_string
    @to_number()
    def get_sp_block_cache_read_hit_ratio(self, id):
        sp = self._get_sp(id)
        return sp.block_cache_read_hit_ratio

    @to_string
    @to_number()
    def get_sp_block_cache_write_hit_ratio(self, id):
        sp = self._get_sp(id)
        return sp.block_cache_write_hit_ratio

    # poolTable
    def get_pools(self):
        return [pool.id for pool in self.unity_system.get_pool()]

    def _get_pool(self, id):
        return self._get_item(self.unity_system.get_pool(), id=id)

    @to_string
    def get_pool_name(self, id):
        pool = self._get_pool(id)
        return pool.name

    @to_string
    def get_pool_disk_types(self, id):
        pool = self._get_pool(id)
        return ', '.join(x.name for x in pool.tiers)

    @to_string
    def get_pool_raid_levels(self, id):
        pool = self._get_pool(id)
        return pool.raid_type.name

    @to_string
    def get_pool_fast_cache_status(self, id):
        pool = self._get_pool(id)
        return pool.is_fast_cache_enabled

    @to_string
    @to_number
    def get_pool_number_of_disk(self, id):
        pool = self._get_pool(id)
        return sum(x.disk_count for x in pool.tiers)

    @to_string
    @to_number
    @change_size_unit
    def get_pool_size_total(self, id):
        pool = self._get_pool(id)
        return pool.size_total

    @to_string
    @to_number
    @change_size_unit
    def get_pool_size_free(self, id):
        pool = self._get_pool(id)
        return pool.size_free

    @to_string
    @to_number
    @change_size_unit
    def get_pool_size_used(self, id):
        pool = self._get_pool(id)
        return pool.size_used

    @to_string
    @to_number
    def get_pool_size_ultilization(self, id):
        pool = self._get_pool(id)
        return float(pool.size_used) / float(pool.size_total)

    # volumeTable
    def get_luns(self):
        return [lun.id for lun in self.unity_system.get_lun()]

    def _get_lun(self, id):
        return self._get_item(self.unity_system.get_lun(), id=id)

    @to_string
    def get_lun_name(self, id):
        lun = self._get_lun(id)
        return lun.name

    @to_string
    def get_lun_raid_type(self, id):
        lun = self._get_lun(id)
        return lun.pool.raid_type.name

    @to_string
    @to_number
    @change_size_unit
    def get_lun_size_allocated(self, id):
        lun = self._get_lun(id)
        return lun.size_allocated

    @to_string
    @to_number
    @change_size_unit
    def get_lun_size_total(self, id):
        lun = self._get_lun(id)
        return lun.size_total

    @to_string
    def get_lun_health_status(self, id):
        lun = self._get_lun(id)
        return lun.health.value.name

    @to_string
    def get_lun_fast_cache_status(self, id):
        lun = self._get_lun(id)
        return lun.pool.is_fast_cache_enabled

    @to_string
    def get_lun_default_sp(self, id):
        lun = self._get_lun(id)
        return lun.default_node.name

    @to_string
    def get_lun_current_sp(self, id):
        lun = self._get_lun(id)
        return lun.current_node.name

    @to_string
    @to_number
    @change_time_unit
    def get_lun_response_time(self, id):
        lun = self._get_lun(id)
        return lun.response_time

    @to_string
    @to_number
    def get_lun_queue_length(self, id):
        lun = self._get_lun(id)
        return lun.queue_length

    @to_string
    @to_number
    def get_lun_total_iops(self, id):
        lun = self._get_lun(id)
        return lun.total_iops

    @to_string
    @to_number
    def get_lun_read_iops(self, id):
        lun = self._get_lun(id)
        return lun.read_iops

    @to_string
    @to_number
    def get_lun_write_iops(self, id):
        lun = self._get_lun(id)
        return lun.write_iops

    @to_string
    @to_number
    @change_size_unit(to_unit='mb')
    def get_lun_total_byte_rate(self, id):
        lun = self._get_lun(id)
        return lun.total_byte_rate

    @to_string
    @to_number
    @change_size_unit(to_unit='mb')
    def get_lun_read_byte_rate(self, id):
        lun = self._get_lun(id)
        return lun.read_byte_rate

    @to_string
    @to_number
    @change_size_unit(to_unit='mb')
    def get_lun_write_byte_rate(self, id):
        lun = self._get_lun(id)
        return lun.write_byte_rate

    @to_string
    @to_number
    def get_lun_fast_cache_read_hits(self, id):
        lun = self._get_lun(id)
        return lun.fast_cache_read_hits

    @to_string
    @to_number
    def get_lun_fast_cache_write_hits(self, id):
        lun = self._get_lun(id)
        return lun.fast_cache_write_hits

    @to_string
    @to_number
    def get_lun_fast_cache_read_hit_rate(self, id):
        lun = self._get_lun(id)
        return lun.fast_cache_read_hit_rate

    @to_string
    @to_number
    def get_lun_fast_cache_write_hit_rate(self, id):
        lun = self._get_lun(id)
        return lun.fast_cache_write_hit_rate

    @to_string
    @to_number
    def get_lun_utilization(self, id):
        lun = self._get_lun(id)
        return lun.utilization

    @to_string
    def get_lun_host_access(self, id):
        lun = self._get_lun(id)
        host_list = [x.host.name for x in lun.host_access]
        if host_list:
            return ', '.join(host_list)
        else:
            return NONE_STRING

    # diskTable
    def get_disks(self):
        return [disk.id for disk in self.unity_system.get_disk()]

    def _get_disk(self, id):
        return self._get_item(self.unity_system.get_disk(), id=id)

    @to_string
    def get_disk_name(self, id):
        disk = self._get_disk(id)
        return disk.name

    @to_string
    def get_disk_model(self, id):
        disk = self._get_disk(id)
        return disk.model

    @to_string
    def get_disk_serial_number(self, id):
        disk = self._get_disk(id)
        return disk.emc_serial_number

    @to_string
    def get_disk_version(self, id):
        disk = self._get_disk(id)
        return disk.version

    @to_string
    def get_disk_type(self, id):
        disk = self._get_disk(id)
        return disk.disk_technology.name

    @to_string
    def get_disk_slot_number(self, id):
        disk = self._get_disk(id)
        return disk.slot_number

    @to_string
    def get_disk_health_status(self, id):
        disk = self._get_disk(id)
        return disk.health.value.name

    @to_string
    @to_number
    @change_size_unit
    def get_disk_raw_size(self, id):
        disk = self._get_disk(id)
        return disk.raw_size

    @to_string
    def get_disk_current_pool(self, id):
        disk = self._get_disk(id)
        return disk.pool.name

    @to_string
    @to_number
    @change_time_unit
    def get_disk_response_time(self, id):
        disk = self._get_disk(id)
        return disk.response_time

    @to_string
    @to_number
    def get_disk_queue_length(self, id):
        disk = self._get_disk(id)
        return disk.queue_length

    @to_string
    @to_number
    def get_disk_total_iops(self, id):
        disk = self._get_disk(id)
        return disk.total_iops

    @to_string
    @to_number
    def get_disk_read_iops(self, id):
        disk = self._get_disk(id)
        return disk.read_iops

    @to_string
    @to_number
    def get_disk_write_iops(self, id):
        disk = self._get_disk(id)
        return disk.write_iops

    @to_string
    @to_number
    @change_size_unit(to_unit='mb')
    def get_disk_total_byte_rate(self, id):
        disk = self._get_disk(id)
        return disk.total_byte_rate

    @to_string
    @to_number
    @change_size_unit(to_unit='mb')
    def get_disk_read_byte_rate(self, id):
        disk = self._get_disk(id)
        return disk.read_byte_rate

    @to_string
    @to_number
    @change_size_unit(to_unit='mb')
    def get_disk_write_byte_rate(self, id):
        disk = self._get_disk(id)
        return disk.write_byte_rate

    @to_string
    @to_number
    def get_disk_utilization(self, id):
        disk = self._get_disk(id)
        return disk.utilization

    # frontendPortTable
    FC_PORT_TYPE = 'fc_port_'
    ISCSI_PORT_TYPE = 'iscsi_port_'

    def get_frontend_ports(self):
        fc_ports = [self.FC_PORT_TYPE + port.id for port in
                    self.unity_system.get_fc_port()]
        iscsi_ports = [self.ISCSI_PORT_TYPE + port.id for port in
                       self.unity_system.get_iscsi_node()]
        return fc_ports + iscsi_ports

    def _get_frontend_port(self, id):
        if id.startswith(self.FC_PORT_TYPE):
            id = id.replace(self.FC_PORT_TYPE, '', 1)
            return self._get_item(self.unity_system.get_fc_port(),
                                  id=id), self.FC_PORT_TYPE
        if id.startswith(self.ISCSI_PORT_TYPE):
            id = id.replace(self.ISCSI_PORT_TYPE, '', 1)
            return self._get_item(self.unity_system.get_iscsi_node(),
                                  id=id), self.ISCSI_PORT_TYPE

    @to_string
    def get_frontend_port_id(self, id):
        port, _ = self._get_frontend_port(id)
        return port.id

    @to_string
    def get_frontend_port_name(self, id):
        port, _ = self._get_frontend_port(id)
        return port.name

    @to_string
    def get_frontend_port_address(self, id):
        port, type = self._get_frontend_port(id)
        if type == self.FC_PORT_TYPE:
            return NONE_STRING
        if type == self.ISCSI_PORT_TYPE:
            ip_list = [portal.ip_address for portal in
                       self.unity_system.get_iscsi_portal() if
                       portal.iscsi_node.id == port.id]

        if ip_list:
            return ', '.join(ip_list)
        else:
            return NONE_STRING

    @to_string
    def get_frontend_port_type(self, id):
        port, type = self._get_frontend_port(id)
        if type == self.FC_PORT_TYPE:
            return port.connector_type.name
        if type == self.ISCSI_PORT_TYPE:
            return port.ethernet_port.connector_type.name

    @to_string
    def get_frontend_port_current_speed(self, id):
        port, type = self._get_frontend_port(id)
        if type == self.FC_PORT_TYPE:
            return port.current_speed.name
        if type == self.ISCSI_PORT_TYPE:
            return port.ethernet_port.speed.name

    @to_string
    def get_frontend_port_supported_speed(self, id):
        port, type = self._get_frontend_port(id)
        if type == self.FC_PORT_TYPE:
            return ', '.join(x.name for x in port.available_speeds)
        if type == self.ISCSI_PORT_TYPE:
            return ', '.join(
                x.name for x in port.ethernet_port.supported_speeds)

    @to_string
    def get_frontend_port_health_status(self, id):
        port, type = self._get_frontend_port(id)
        if type == self.FC_PORT_TYPE:
            return port.health.value.name
        if type == self.ISCSI_PORT_TYPE:
            return port.ethernet_port.health.value.name

    @to_string
    @to_number
    def get_frontend_port_total_iops(self, id):
        port, _ = self._get_frontend_port(id)
        return port.total_iops

    @to_string
    @to_number
    def get_frontend_port_read_iops(self, id):
        port, _ = self._get_frontend_port(id)
        return port.read_iops

    @to_string
    @to_number
    def get_frontend_port_write_iops(self, id):
        port, _ = self._get_frontend_port(id)
        return port.write_iops

    @to_string
    @to_number
    @change_size_unit(to_unit='mb')
    def get_frontend_port_total_byte_rate(self, id):
        port, _ = self._get_frontend_port(id)
        return port.total_byte_rate

    @to_string
    @to_number
    @change_size_unit(to_unit='mb')
    def get_frontend_port_read_byte_rate(self, id):
        port, _ = self._get_frontend_port(id)
        return port.read_byte_rate

    @to_string
    @to_number
    @change_size_unit(to_unit='mb')
    def get_frontend_port_write_byte_rate(self, id):
        port, _ = self._get_frontend_port(id)
        return port.write_byte_rate

    # backendPortTable
    def get_backend_ports(self):
        return [port.id for port in self.unity_system.get_sas_port()]

    def _get_backend_port(self, id):
        return self._get_item(self.unity_system.get_sas_port(), id=id)

    @to_string
    def get_backend_port_name(self, id):
        port = self._get_backend_port(id)
        return port.name

    @to_string
    def get_backend_port_type(self, id):
        port = self._get_backend_port(id)
        return port.connector_type.name

    @to_string
    def get_backend_port_port_number(self, id):
        port = self._get_backend_port(id)
        return port.port

    @to_string
    def get_backend_port_current_speed(self, id):
        port = self._get_backend_port(id)
        return port.current_speed.name

    @to_string
    def get_backend_port_parent_io_module(self, id):
        port = self._get_backend_port(id)
        return port.parent_io_module.name

    @to_string
    def get_backend_port_parent_sp(self, id):
        port = self._get_backend_port(id)
        return port.parent_storage_processor.name

    @to_string
    def get_backend_port_health_status(self, id):
        port = self._get_backend_port(id)
        return port.health.value.name

    @to_string
    def get_backend_port_total_iops(self, id):
        return NONE_STRING

    @to_string
    def get_backend_port_read_iops(self, id):
        return NONE_STRING

    @to_string
    def get_backend_port_write_iops(self, id):
        return NONE_STRING

    @to_string
    def get_backend_port_total_byte_rate(self, id):
        return NONE_STRING

    @to_string
    def get_backend_port_read_byte_rate(self, id):
        return NONE_STRING

    @to_string
    def get_backend_port_write_byte_rate(self, id):
        return NONE_STRING

    # hostTable
    def get_hosts(self):
        return [host.id for host in self.unity_system.get_host()]

    def _get_host(self, id):
        return self._get_item(self.unity_system.get_host(), id=id)

    @to_string
    def get_host_name(self, id):
        host = self._get_host(id)
        return host.name

    @to_string
    def get_host_network_address(self, id):
        host = self._get_host(id)
        if host.ip_list:
            return ', '.join(host.ip_list)
        else:
            return NONE_STRING

    @to_string
    def get_host_initiators(self, id):
        host = self._get_host(id)
        initiators = []
        if hasattr(host,
                   'iscsi_host_initiators') and host.iscsi_host_initiators:
            initiators.extend(
                x.initiator_id for x in host.iscsi_host_initiators)
        if hasattr(host, 'fc_host_initiators') and host.fc_host_initiators:
            initiators.extend(x.initiator_id for x in host.fc_host_initiators)

        if initiators:
            return ', '.join(initiators)
        else:
            return NONE_STRING

    @to_string
    def get_host_os_type(self, id):
        host = self._get_host(id)
        return host.os_type

    @to_string
    def get_host_assigned_volumes(self, id):
        host = self._get_host(id)
        if host.host_luns:
            return ', '.join(x.lun.name for x in host.host_luns)
        else:
            return NONE_STRING

    # enclosureTable
    DAE_TYPE = 'dae_'
    DPE_TYPE = 'dpe_'

    def get_enclosures(self):
        daes = [self.DAE_TYPE + dae.id for dae in
                self.unity_system.get_dae()]
        dpes = [self.DPE_TYPE + dpe.id for dpe in
                self.unity_system.get_dpe()]
        return daes + dpes

    def _get_enclosure(self, id):
        if id.startswith(self.DAE_TYPE):
            id = id.replace(self.DAE_TYPE, '', 1)
            return self._get_item(self.unity_system.get_dae(), id=id)
        if id.startswith(self.DPE_TYPE):
            id = id.replace(self.DPE_TYPE, '', 1)
            return self._get_item(self.unity_system.get_dpe(), id=id)

    @to_string
    def get_enclosure_id(self, id):
        enclosure = self._get_enclosure(id)
        return enclosure.id

    @to_string
    def get_enclosure_name(self, id):
        enclosure = self._get_enclosure(id)
        return enclosure.name

    @to_string
    def get_enclosure_model(self, id):
        enclosure = self._get_enclosure(id)
        return enclosure.model

    @to_string
    def get_enclosure_serial_number(self, id):
        enclosure = self._get_enclosure(id)
        return enclosure.emc_serial_number

    @to_string
    def get_enclosure_part_number(self, id):
        enclosure = self._get_enclosure(id)
        return enclosure.emc_part_number

    @to_string
    def get_enclosure_health_status(self, id):
        enclosure = self._get_enclosure(id)
        return enclosure.health.value.name

    @to_string
    @to_number
    def get_enclosure_current_power(self, id):
        enclosure = self._get_enclosure(id)
        return enclosure.current_power

    @to_string
    @to_number
    def get_enclosure_avg_power(self, id):
        enclosure = self._get_enclosure(id)
        return enclosure.avg_power

    @to_string
    @to_number
    def get_enclosure_max_power(self, id):
        enclosure = self._get_enclosure(id)
        return enclosure.max_power

    @to_string
    @to_number
    def get_enclosure_current_temperature(self, id):
        enclosure = self._get_enclosure(id)
        return enclosure.current_temperature

    @to_string
    @to_number
    def get_enclosure_avg_temperature(self, id):
        enclosure = self._get_enclosure(id)
        return enclosure.avg_temperature

    @to_string
    @to_number
    def get_enclosure_max_temperature(self, id):
        enclosure = self._get_enclosure(id)
        return enclosure.max_temperature

    # powerSupplyTable
    def get_power_supplies(self):
        return [power_supply.id for power_supply in
                self.unity_system.get_power_supply()]

    def _get_power_supply(self, id):
        return self._get_item(self.unity_system.get_power_supply(), id=id)

    @to_string
    def get_power_supply_name(self, id):
        power_supply = self._get_power_supply(id)
        return power_supply.name

    @to_string
    def get_power_supply_manufacturer(self, id):
        power_supply = self._get_power_supply(id)
        return power_supply.manufacturer

    @to_string
    def get_power_supply_model(self, id):
        power_supply = self._get_power_supply(id)
        return power_supply.model

    @to_string
    def get_power_supply_firmware_version(self, id):
        power_supply = self._get_power_supply(id)
        return power_supply.firmware_version

    @to_string
    def get_power_supply_parent_enclosure(self, id):
        power_supply = self._get_power_supply(id)
        parents = []
        if hasattr(power_supply, 'parent_dpe') and power_supply.parent_dpe:
            parents.append(power_supply.parent_dpe)
        if hasattr(power_supply, 'parent_dae') and power_supply.parent_dae:
            parents.append(power_supply.parent_dae)

        if parents:
            return ', '.join(x.name for x in parents)
        else:
            return NONE_STRING

    @to_string
    def get_power_supply_sp(self, id):
        power_supply = self._get_power_supply(id)
        return power_supply.storage_processor.name

    @to_string
    def get_power_supply_health_status(self, id):
        power_supply = self._get_power_supply(id)
        return power_supply.health.value.name

    # fanTable
    def get_fans(self):
        return [fan.id for fan in self.unity_system.get_fan()]

    def _get_fan(self, id):
        return self._get_item(self.unity_system.get_fan(), id=id)

    @to_string
    def get_fan_name(self, id):
        fan = self._get_fan(id)
        return fan.name

    @to_string
    def get_fan_slot_number(self, id):
        fan = self._get_fan(id)
        return fan.slot_number

    @to_string
    def get_fan_parent_enclosure(self, id):
        fan = self._get_fan(id)
        parents = []
        if hasattr(fan, 'parent_dpe') and fan.parent_dpe:
            parents.append(fan.parent_dpe)
        if hasattr(fan, 'parent_dae') and fan.parent_dae:
            parents.append(fan.parent_dae)

        if parents:
            return ', '.join(x.name for x in parents)
        else:
            return NONE_STRING

    @to_string
    def get_fan_health_status(self, id):
        fan = self._get_fan(id)
        return fan.health.value.name

    # BBUTable
    def get_bbus(self):
        return [bbu.id for bbu in self.unity_system.get_battery()]

    def _get_bbu(self, id):
        return self._get_item(self.unity_system.get_battery(), id=id)

    @to_string
    def get_bbu_name(self, id):
        bbu = self._get_bbu(id)
        return bbu.name

    @to_string
    def get_bbu_manufacturer(self, id):
        bbu = self._get_bbu(id)
        return bbu.manufacturer

    @to_string
    def get_bbu_model(self, id):
        bbu = self._get_bbu(id)
        return bbu.model

    @to_string
    def get_bbu_firmware_version(self, id):
        bbu = self._get_bbu(id)
        return bbu.firmware_version

    @to_string
    def get_bbu_parent_sp(self, id):
        bbu = self._get_bbu(id)
        return bbu.parent_storage_processor.name

    @to_string
    def get_bbu_health_status(self, id):
        bbu = self._get_bbu(id)
        return bbu.health.value.name
