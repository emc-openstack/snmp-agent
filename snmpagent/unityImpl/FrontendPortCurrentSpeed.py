class FrontendPortCurrentSpeed(object):
    def read_get(self, name, idx_name, unity_client):
        return unity_client.get_frontend_port_current_speed(idx_name)


class FrontendPortCurrentSpeedColumn(object):
    def get_idx(self, name, idx, unity_client):
        return unity_client.get_frontend_ports()
