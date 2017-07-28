class PoolDiskTypes(object):
    def read_get(self, name, idx_name, unity_client):
        return unity_client.get_pool_disk_types(idx_name)


class PoolDiskTypesColumn(object):
    def get_idx(self, name, idx, unity_client):
        return unity_client.get_pools()
