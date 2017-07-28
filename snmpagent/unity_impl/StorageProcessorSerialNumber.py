class StorageProcessorSerialNumber(object):
    def read_get(self, name, idx_name, unity_client):
        return unity_client.get_sp_serial_number(idx_name)


class StorageProcessorSerialNumberColumn(object):
    def get_idx(self, name, idx, unity_client):
        return unity_client.get_sps()
