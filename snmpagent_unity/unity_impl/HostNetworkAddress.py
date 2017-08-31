class HostNetworkAddress(object):
    def read_get(self, name, idx_name, unity_client):
        return unity_client.get_host_network_address(idx_name)


class HostNetworkAddressColumn(object):
    def get_idx(self, name, idx, unity_client):
        return unity_client.get_hosts()
