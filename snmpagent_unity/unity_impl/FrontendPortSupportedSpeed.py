class FrontendPortSupportedSpeed(object):
    def read_get(self, name, idx_name, unity_client):
        return unity_client.get_frontend_port_supported_speed(idx_name)


class FrontendPortSupportedSpeedColumn(object):
    def get_idx(self, name, idx, unity_client):
        return unity_client.get_frontend_ports()
