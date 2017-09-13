class BbuModel(object):
    def read_get(self, name, idx_name, unity_client):
        return unity_client.get_bbu_model(idx_name)


class BbuModelColumn(object):
    def get_idx(self, name, idx, unity_client):
        return unity_client.get_bbus()
