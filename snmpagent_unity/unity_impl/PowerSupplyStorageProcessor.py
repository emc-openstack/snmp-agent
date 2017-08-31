class PowerSupplyStorageProcessor(object):
    def read_get(self, name, idx_name, unity_client):
        return unity_client.get_power_supply_sp(idx_name)


class PowerSupplyStorageProcessorColumn(object):
    def get_idx(self, name, idx, unity_client):
        return unity_client.get_power_supplies()
