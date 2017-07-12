class DiskQueueLength(object):
    def read_get(self, name, idx_name, unity_client):
        return unity_client.get_disk_queue_length(idx_name)


class DiskQueueLengthColumn(object):
    def get_idx(self, name, idx, unity_client):
        return unity_client.get_disks()
