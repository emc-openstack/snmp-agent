class PoolRemainingCapacity(object):
    def read_get(self, name, idx_name, unity_client):
        return unity_client.get_pool_size_free(idx_name)


class PoolRemainingCapacityColumn(object):
    def get_idx(self, name, idx, unity_client):
        return unity_client.get_pools()
