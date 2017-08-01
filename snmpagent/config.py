import itertools
from collections import OrderedDict

from six.moves import configparser

from snmpagent import cipher, enums, utils
from snmpagent import exceptions as snmp_ex

V2, V3 = enums.UserVersion.V2, enums.UserVersion.V3


def dash_if_empty(value):
    if value is None or not str(value):
        return '-'
    return str(value)


class Password(object):
    def __init__(self, password):
        if cipher.is_encrypted(password):
            self.encrypted, self.raw = password, cipher.decrypt(password)
        else:
            self.encrypted, self.raw = cipher.encrypt(password), password

    def __str__(self):
        return dash_if_empty(self.encrypted)


class ConfigEntry(object):
    def __init__(self, **kwargs):
        self.options = kwargs

    def __getattr__(self, item):
        try:
            return self.options[item]
        except KeyError:
            raise AttributeError('No attribute: {}'.format(item))


class AgentConfigEntry(ConfigEntry):
    def __init__(self, name, agent_ip, agent_port, model, mgmt_ip, user,
                 password):
        super(AgentConfigEntry, self).__init__(
            name=name, agent_ip=agent_ip, agent_port=agent_port, model=model,
            mgmt_ip=mgmt_ip, user=user, password=Password(password))


USER_V2_HEAD = '# model security_name community'
USER_V2_SHOW_HEAD = 'SNMP Version 2 Community Access:'
USER_V2_SHOW = '''{name}
    Version:    {mode}
    Community:  {community}'''
USER_V3_HEAD = '''# model security_name context security_level
auth_protocol auth_key priv_protocol priv_key'''
USER_V3_SHOW_HEAD = 'SNMP Version 3 Users:'
USER_V3_SHOW = '''{name}
    Version:            {mode}
    Security Level:     {security_level}
    Auth Protocol:      {auth_protocol}
    Auth Key:           {auth_key}
    Privacy Protocol:   {priv_protocol}
    Privacy Key:        {priv_key}'''


def _show(format_str, **kwargs):
    for k, v in kwargs.items():
        kwargs[k] = dash_if_empty(v)
    return format_str.format(**kwargs)


class UserV2ConfigEntry(ConfigEntry):
    def __init__(self, name, community):
        super(UserV2ConfigEntry, self).__init__(
            name=name, mode=V2,
            community=utils.enum(enums.Community, community))

    def __str__(self):
        return ' '.join(dash_if_empty(item)
                        for item in (self.mode, self.name, self.community))

    def show(self):
        return _show(USER_V2_SHOW, name=self.name, mode=self.mode,
                     community=self.community)


class UserV3ConfigEntry(ConfigEntry):
    def __init__(self, name, context, security_level, auth_protocol,
                 auth_key, priv_protocol, priv_key):
        super(UserV3ConfigEntry, self).__init__(
            name=name, mode=V3, context=context,
            security_level=utils.enum(enums.SecurityLevel,
                                      security_level),
            auth_protocol=utils.enum(enums.AuthProtocol, auth_protocol),
            auth_key=Password(auth_key),
            priv_protocol=utils.enum(enums.PrivProtocol, priv_protocol),
            priv_key=Password(priv_key))

    def __str__(self):
        return ' '.join(dash_if_empty(item)
                        for item in (self.mode, self.name,
                                     self.context, self.security_level,
                                     self.auth_protocol, self.auth_key,
                                     self.priv_protocol, self.priv_key))

    def show(self):
        return _show(USER_V3_SHOW, name=self.name, mode=self.mode,
                     security_level=self.security_level,
                     auth_protocol=self.auth_protocol, auth_key=self.auth_key,
                     priv_protocol=self.priv_protocol, priv_key=self.priv_key)


class AgentConfigParser(object):
    def __init__(self, conf_file):
        self._conf_file = conf_file
        self._parser = configparser.ConfigParser()
        self._parser.read(conf_file)
        self._writer = configparser.ConfigParser()
        self._writer.read(conf_file)

    def parse(self):
        res = OrderedDict()
        for section in self._parser.sections():
            res[section] = AgentConfigEntry(
                section, **dict(self._parser.items(section)))
        return res

    def save(self, conf_dict, encrypt=True):
        for section, entry in conf_dict.items():
            for option, value in entry.options.items():
                if isinstance(value, Password):
                    self._writer.set(section, option,
                                     value.encrypted if encrypt else value.raw)
        with open(self._conf_file, 'w') as f:
            self._writer.write(f)


class UserConfigParser(object):
    def __init__(self, conf_file):
        self._conf_file = conf_file
        with open(conf_file, 'r') as f:
            self._raw_conf = [line.strip() for line in f.readlines()
                              if not line.lstrip().startswith('#') and
                              len(line.strip())]

    def parse(self):
        def _parse_user(line):
            mode, detail = line.split(None, 1)
            args = [each.strip('-') for each in detail.split()]
            name = args[0]
            mode = utils.enum(enums.UserVersion, mode)
            if mode == V3:
                return name, UserV3ConfigEntry(*args)
            elif mode == V2:
                return name, UserV2ConfigEntry(*args)
            else:
                raise snmp_ex.UserConfigError(
                    'Not supported user mode: {}'.format(mode))

        return OrderedDict(map(_parse_user, self._raw_conf))

    def save(self, conf_dict, encrypt=True):
        v2, v3 = UserConfig.split_v2_v3(conf_dict)
        with open(self._conf_file, 'w') as f:
            f.writelines(str(line) + '\n'
                         for line in ([USER_V2_HEAD] + v2 +
                                      ['\n', USER_V3_HEAD] + v3))


class FileConfig(object):
    _PARSER_CLZ = None

    def __init__(self, conf_file):
        self._conf_file = conf_file
        self._entries = None
        self._parser = None

    @property
    def parser(self):
        if self._parser is None:
            self._parser = self._PARSER_CLZ(self._conf_file)
        return self._parser

    @property
    def entries(self):
        if self._entries is None:
            self._entries = self.parser.parse()
        return self._entries

    def save(self, encrypt=True):
        self.parser.save(self.entries, encrypt)


class AgentConfig(FileConfig):
    _PARSER_CLZ = AgentConfigParser


class UserConfig(FileConfig):
    _PARSER_CLZ = UserConfigParser

    @staticmethod
    def split_v2_v3(all_entries):
        groups = dict((k, list(g)) for k, g in
                      itertools.groupby(all_entries.values(),
                                        lambda e: e.mode))
        return groups[V2], groups[V3]
