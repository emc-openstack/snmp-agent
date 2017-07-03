class PowerSupplyFirmwareVersion(object):
    def read_get(self, name, idx_name, unity_client):
        return unity_client.get_power_supply_firmware_version(idx_name)


class PowerSupplyFirmwareVersionColumn(object):
    def get_idx(self, name, idx, unity_client):
        return unity_client.get_power_supplies()
