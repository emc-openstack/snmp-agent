class PoolNumberOfPhysicalDisk(object):
    def read_get(self, name, idx_name, unity_client):
        return unity_client.get_pool_number_of_disk(idx_name)


class PoolNumberOfPhysicalDiskColumn(object):
    def get_idx(self, name, idx, unity_client):
        return unity_client.get_pools()
