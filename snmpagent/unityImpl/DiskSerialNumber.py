class DiskSerialNumber(object):
    def read_get(self, name, idx_name, unity_client):
        return unity_client.get_disk_serial_number(idx_name)


class DiskSerialNumberColumn(object):
    def get_idx(self, name, idx, unity_client):
        return unity_client.get_disks()
