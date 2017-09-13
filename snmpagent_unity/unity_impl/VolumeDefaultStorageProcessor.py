class VolumeDefaultStorageProcessor(object):
    def read_get(self, name, idx_name, unity_client):
        return unity_client.get_lun_default_sp(idx_name)


class VolumeDefaultStorageProcessorColumn(object):
    def get_idx(self, name, idx, unity_client):
        return unity_client.get_luns()
