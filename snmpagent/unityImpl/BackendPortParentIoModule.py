class BackendPortParentIoModule(object):
    def read_get(self, name, idx_name, unity_client):
        return unity_client.get_backend_port_parent_io_module(idx_name)


class BackendPortParentIoModuleColumn(object):
    def get_idx(self, name, idx, unity_client):
        return unity_client.get_backend_ports()
