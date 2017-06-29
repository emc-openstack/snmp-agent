class VolumeCurrentstorageProcessor(object):
    def read_get(self, name, idx_name, unity_client):
        return unity_client.get_lun_current_sp(idx_name)


class VolumeCurrentstorageProcessorColumn(object):
    def get_idx(self, name, idx, unity_client):
        return unity_client.get_luns()
