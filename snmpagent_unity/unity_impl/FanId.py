class FanId(object):
    def read_get(self, name, idx_name, unity_client):
        return idx_name


class FanIdColumn(object):
    def get_idx(self, name, idx, unity_client):
        return unity_client.get_fans()
