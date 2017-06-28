class HostOperationSystemVersion(object):
    def read_get(self, name, idx_name, unity_client):
        return unity_client.get_host_os_type(idx_name)


class HostOperationSystemVersionColumn(object):
    def get_idx(self, name, idx, unity_client):
        return unity_client.get_hosts()
