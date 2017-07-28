class DiskResponseTime(object):
    def read_get(self, name, idx_name, unity_client):
        return unity_client.get_disk_response_time(idx_name)


class DiskResponseTimeColumn(object):
    def get_idx(self, name, idx, unity_client):
        return unity_client.get_disks()
