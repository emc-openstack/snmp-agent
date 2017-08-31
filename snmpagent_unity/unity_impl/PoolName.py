class PoolName(object):
    def read_get(self, name, idx_name, unity_client):
        return unity_client.get_pool_name(idx_name)


class PoolNameColumn(object):
    def get_idx(self, name, idx, unity_client):
        return unity_client.get_pools()
