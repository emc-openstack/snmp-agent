class EnclosureSerialNumber(object):
    def read_get(self, name, idx_name, unity_client):
        return unity_client.get_enclosure_serial_number(idx_name)


class EnclosureSerialNumberColumn(object):
    def get_idx(self, name, idx, unity_client):
        return unity_client.get_enclosures()
