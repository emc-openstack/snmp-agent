class PoolCapacityUtilization(object):
    def read_get(self, name, idx_name, unity_client):
        return unity_client.get_pool_size_ultilization(idx_name)


class PoolCapacityUtilizationColumn(object):
    def get_idx(self, name, idx, unity_client):
        return unity_client.get_pools()
