class Manufacturer(object):
    def read_get(self, name, idx, unity_client):
        return unity_client.get_manufacturer()