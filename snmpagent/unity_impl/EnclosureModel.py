class EnclosureModel(object):
    def read_get(self, name, idx_name, unity_client):
        return unity_client.get_enclosure_model(idx_name)


class EnclosureModelColumn(object):
    def get_idx(self, name, idx, unity_client):
        return unity_client.get_enclosures()
