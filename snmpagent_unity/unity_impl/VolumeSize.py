class VolumeSize(object):
    def read_get(self, name, idx_name, unity_client):
        return unity_client.get_lun_size_total(idx_name)


class VolumeSizeColumn(object):
    def get_idx(self, name, idx, unity_client):
        return unity_client.get_luns()
