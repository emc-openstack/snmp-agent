class PoolId(object):
    def read_get(self, name, idx_name, unity_client):
        return idx_name


class PoolIdColumn(object):
    def get_idx(self, name, idx, unity_client):
        return unity_client.get_pools()
