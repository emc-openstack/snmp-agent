class EnclosureMaxPower(object):
    def read_get(self, name, idx_name, unity_client):
        return unity_client.get_enclosure_max_power(idx_name)


class EnclosureMaxPowerColumn(object):
    def get_idx(self, name, idx, unity_client):
        return unity_client.get_enclosures()
