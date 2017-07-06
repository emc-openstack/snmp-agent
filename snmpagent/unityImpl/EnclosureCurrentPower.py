class EnclosureCurrentPower(object):
    def read_get(self, name, idx_name, unity_client):
        return unity_client.get_enclosure_current_power(idx_name)


class EnclosureCurrentPowerColumn(object):
    def get_idx(self, name, idx, unity_client):
        return unity_client.get_enclosures()
