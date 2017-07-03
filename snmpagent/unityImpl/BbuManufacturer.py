class BbuManufacturer(object):
    def read_get(self, name, idx_name, unity_client):
        return unity_client.get_bbu_manufacturer(idx_name)


class BbuManufacturerColumn(object):
    def get_idx(self, name, idx, unity_client):
        return unity_client.get_bbus()
