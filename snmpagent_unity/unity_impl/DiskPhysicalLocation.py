class DiskPhysicalLocation(object):
    def read_get(self, name, idx_name, unity_client):
        return unity_client.get_disk_slot_number(idx_name)


class DiskPhysicalLocationColumn(object):
    def get_idx(self, name, idx, unity_client):
        return unity_client.get_disks()
