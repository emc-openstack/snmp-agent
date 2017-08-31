class PowerSupplyHealthStatus(object):
    def read_get(self, name, idx_name, unity_client):
        return unity_client.get_power_supply_health_status(idx_name)


class PowerSupplyHealthStatusColumn(object):
    def get_idx(self, name, idx, unity_client):
        return unity_client.get_power_supplies()
