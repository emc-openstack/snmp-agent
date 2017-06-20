from datetime import datetime

class EnclosureTableInfo(object):
    def get_enclosure_name(self, name, idx):
        return  '[%s] enclosure name1' % str(datetime.now())

    def get_enclosure_model(self, name, idx):
        return  '[%s] enclosure model1' % str(datetime.now())

    def get_enclosure_serial_number(self, name, idx):
        return '[%s] enclosure serial number1' % str(datetime.now())