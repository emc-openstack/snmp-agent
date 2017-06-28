class StorageProcessorOperationalState(object):
    def read_get(self, name, idx_name, unity_client):
        return unity_client.get_sp_health_status(idx_name)


class StorageProcessorOperationalStateColumn(object):
    def get_idx(self, name, idx, unity_client):
        return unity_client.get_sps()
