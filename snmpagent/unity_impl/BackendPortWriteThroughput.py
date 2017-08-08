class BackendPortWriteThroughput(object):
    def read_get(self, name, idx_name, unity_client):
        return unity_client.get_backend_port_write_iops(idx_name)


class BackendPortWriteThroughputColumn(object):
    def get_idx(self, name, idx, unity_client):
        return unity_client.get_backend_ports()
