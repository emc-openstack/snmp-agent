class VolumeUtilization(object):
    def read_get(self, name, idx_name, unity_client):
        return unity_client.get_lun_utilization(idx_name)


class VolumeUtilizationColumn(object):
    def get_idx(self, name, idx, unity_client):
        return unity_client.get_luns()
