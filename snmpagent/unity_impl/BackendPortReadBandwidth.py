class BackendPortReadBandwidth(object):
    def read_get(self, name, idx_name, unity_client):
        return unity_client.get_backend_port_read_byte_rate(idx_name)


class BackendPortReadBandwidthColumn(object):
    def get_idx(self, name, idx, unity_client):
        return unity_client.get_backend_ports()
