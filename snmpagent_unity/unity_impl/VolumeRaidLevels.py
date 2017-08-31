class VolumeRaidLevels(object):
    def read_get(self, name, idx_name, unity_client):
        return unity_client.get_lun_raid_type(idx_name)


class VolumeRaidLevelsColumn(object):
    def get_idx(self, name, idx, unity_client):
        return unity_client.get_luns()
