class VolumeAllocatedSize(object):
    def read_get(self, name, idx_name, unity_client):
        return unity_client.get_lun_size_allocated(idx_name)


class VolumeAllocatedSizeColumn(object):
    def get_idx(self, name, idx, unity_client):
        return unity_client.get_luns()
