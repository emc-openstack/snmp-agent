class EnclosureAveragePower(object):
    def read_get(self, name, idx_name, unity_client):
        return unity_client.get_enclosure_avg_power(idx_name)


class EnclosureAveragePowerColumn(object):
    def get_idx(self, name, idx, unity_client):
        return unity_client.get_enclosures()
