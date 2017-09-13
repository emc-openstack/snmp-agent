class EnclosureId(object):
    def read_get(self, name, idx_name, unity_client):
        return unity_client.get_enclosure_id(idx_name)


class EnclosureIdColumn(object):
    def get_idx(self, name, idx, unity_client):
        return unity_client.get_enclosures()
