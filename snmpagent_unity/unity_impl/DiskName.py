class DiskName(object):
    def read_get(self, name, idx_name, unity_client):
        return unity_client.get_disk_name(idx_name)


class DiskNameColumn(object):
    def get_idx(self, name, idx, unity_client):
        return unity_client.get_disks()
