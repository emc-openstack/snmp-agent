import os

from six.moves.configparser import ConfigParser


class ConfigSection(object):
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)


class SNMPAgentConfig(object):
    def __init__(self, config_file):
        self.config_file = config_file
        self.sections = {}
        self._parse_config_file()

    def _parse_config_file(self):
        config = ConfigParser()
        config.read(self.config_file)
        for section in config.sections():
            kw = dict(config.items(section))
            self.sections[section] = ConfigSection(**kw)

    def get_sections_by_type(self, section_type):
        sections = []
        for name, section in self.sections.items():
            if 'type' in section.__dict__ and section.type == section_type:
                sections.append(section)
        return sections


if __name__ == '__main__':
    config_file = os.path.abspath('../etc/snmpagent.conf')
    snmp_config = SNMPAgentConfig(config_file)
    for name, section in snmp_config.sections.items():
        if 'type' in section.__dict__ and section.type == 'unity':
            print(name)
            for k, v in section.__dict__.items():
                print(k + ': ' + v)

    for name, section in snmp_config.sections.items():
        if 'type' in section.__dict__ and section.type == 'auth':
            print(name)
            for k, v in section.__dict__.items():
                print(k + ': ' + v)
