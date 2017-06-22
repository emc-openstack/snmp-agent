import os
import re

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

    @classmethod
    def _is_encrypted(cls, string):
        return True

    @classmethod
    def _encrypt_string(cls, match, key='pass'):
        # TODO: implement encrypt algorithm
        encrypt = lambda x: 'pass_' + x + '_word'
        return match.groups()[0] + encrypt(match.groups()[1]) + match.groups()[2]

    @classmethod
    def encrypt_config(cls, config_file):
        pattern = re.compile('(password\s*=\s*)(\S*)(.*)')
        with open(config_file, 'r') as f:
            string = f.read()
            if not cls._is_encrypted(string):
                string = re.sub(pattern, cls._encrypt_string, string)
                print(string)

                # TODO: backup config file?
                # with open(config_file, 'w') as f:
                #     f.write(string)

    @classmethod
    def _decrypt_string(cls, match, key='pass'):
        # TODO: implement decrypt algorithm
        encrypt = lambda x: 'word_' + x + '_pass'
        return match.groups()[0] + encrypt(match.groups()[1]) + match.groups()[2]

    @classmethod
    def decrypt_config(cls, config_file):
        pattern = re.compile('(password\s*=\s*)(\S*)(.*)')
        with open(config_file, 'r') as f:
            string = f.read()
            if cls._is_encrypted(string):
                string = re.sub(pattern, cls._decrypt_string, string)
                print(string)

                # TODO: backup config file?
                # with open(config_file, 'w') as f:
                #     f.write(string)


class UserInfo(object):
    def __init__(self, model, security_name, context=None, security_level=None, auth_proto=None, auth_key=None,
                 priv_proto=None, priv_key=None, community=None):
        self.model = model
        self.security_name = security_name
        self.context = context
        self.security_level = security_level
        self.auth_proto = auth_proto
        self.auth_key = auth_key
        self.priv_proto = priv_proto
        self.priv_key = priv_key
        self.community = community


class AuthConfig(object):
    def __init__(self, config_file):
        self.config_file = config_file
        self.users = []
        self._parse_config_file()

    def _parse_config_file(self):
        with open(self.config_file, 'r') as f:
            for line in f.readlines():
                # TODO: need to consider space/tab at BOL
                if re.match('snmp', line, re.I):
                    self.users.append(self._parse_user_info(line))

    def _parse_user_info(self, line):
        check_info = lambda x: x if x != '-' else None
        user_info = [check_info(x) for x in re.split(r'\s+', line)]
        model = user_info[0].lower()
        if model == 'snmpv3' and len(user_info) >= 8:
            return UserInfo(model, *user_info[1:8])
        elif model == 'snmpv2c' and len(user_info) >= 3:
            return UserInfo(model, user_info[1], community=user_info[2])
        else:
            # TODO: raise exception
            pass


if __name__ == '__main__':
    # config_file = os.path.abspath('../../etc/snmpagent.conf')
    # snmp_config = SNMPAgentConfig(config_file)
    # for name, section in snmp_config.sections.items():
    #     if 'type' in section.__dict__ and section.type == 'unity':
    #         print(name)
    #         for k, v in section.__dict__.items():
    #             print(k + ': ' + v)
    #
    # auth_config_file = os.path.abspath('../../etc/access.conf')
    # auth_config = AuthConfig(auth_config_file)
    # for user in auth_config.users:
    #     for k, v in user.__dict__.items():
    #         print("%s: %s" % (k, v))

    # SNMPAgentConfig.encrypt_config(os.path.abspath('../../etc/snmpagent.conf'))
    SNMPAgentConfig.decrypt_config(os.path.abspath('../../etc/snmpagent.conf'))

