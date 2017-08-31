class EnclosureMaxTemperature(object):
    def read_get(self, name, idx_name, unity_client):
        return unity_client.get_enclosure_max_temperature(idx_name)


class EnclosureMaxTemperatureColumn(object):
    def get_idx(self, name, idx, unity_client):
        return unity_client.get_enclosures()
