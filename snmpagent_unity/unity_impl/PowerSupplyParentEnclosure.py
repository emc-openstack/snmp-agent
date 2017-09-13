class PowerSupplyParentEnclosure(object):
    def read_get(self, name, idx_name, unity_client):
        return unity_client.get_power_supply_parent_enclosure(idx_name)


class PowerSupplyParentEnclosureColumn(object):
    def get_idx(self, name, idx, unity_client):
        return unity_client.get_power_supplies()
