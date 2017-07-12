class VolumeResponseTime(object):
    def read_get(self, name, idx_name, unity_client):
        return unity_client.get_lun_response_time(idx_name)


class VolumeResponseTimeColumn(object):
    def get_idx(self, name, idx, unity_client):
        return unity_client.get_luns()
