class DiskModel(object):
    def read_get(self, name, idx_name, unity_client):
        return unity_client.get_disk_model(idx_name)


class DiskModelColumn(object):
    def get_idx(self, name, idx, unity_client):
        return unity_client.get_disks()
