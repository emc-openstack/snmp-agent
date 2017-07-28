class BackendPortParentStorageProcessor(object):
    def read_get(self, name, idx_name, unity_client):
        return unity_client.get_backend_port_parent_sp(idx_name)


class BackendPortParentStorageProcessorColumn(object):
    def get_idx(self, name, idx, unity_client):
        return unity_client.get_backend_ports()
