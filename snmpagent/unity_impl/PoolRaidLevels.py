class PoolRaidLevels(object):
    def read_get(self, name, idx_name, unity_client):
        return unity_client.get_pool_raid_levels(idx_name)


class PoolRaidLevelsColumn(object):
    def get_idx(self, name, idx, unity_client):
        return unity_client.get_pools()
