class BbuFirmwareVersion(object):
    def read_get(self, name, idx_name, unity_client):
        return unity_client.get_bbu_firmware_version(idx_name)


class BbuFirmwareVersionColumn(object):
    def get_idx(self, name, idx, unity_client):
        return unity_client.get_bbus()
