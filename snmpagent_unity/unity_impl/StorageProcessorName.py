class StorageProcessorName(object):
    def read_get(self, name, idx_name, unity_client):
        return unity_client.get_sp_name(idx_name)


class StorageProcessorNameColumn(object):
    def get_idx(self, name, idx, unity_client):
        return unity_client.get_sps()
