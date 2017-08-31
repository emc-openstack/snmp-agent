class PowerSupplyModel(object):
    def read_get(self, name, idx_name, unity_client):
        return unity_client.get_power_supply_model(idx_name)


class PowerSupplyModelColumn(object):
    def get_idx(self, name, idx, unity_client):
        return unity_client.get_power_supplies()
