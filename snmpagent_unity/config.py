import itertools
from collections import OrderedDict
import os
import logging

from six.moves import configparser
from snmpagent_unity import cipher, enums, utils
from snmpagent_unity import exceptions as snmp_ex

LOG = logging.getLogger(__file__)

V2, V3 = enums.UserVersion.V2, enums.UserVersion.V3


def to_console_str(value):
    if not value:
        return '-'
    if isinstance(value, enums.CaseInsensitiveEnum):
        return str(value)
    return value


class Serializable(object):
    def __init__(self, value):
        self.value = value

    def to_config_string(self):
        return self.value


class Password(object):
    def __init__(self, password):
        if cipher.is_encrypted(password):
            self.encrypted, self.raw = password, cipher.decrypt(password)
        else:
            self.encrypted, self.raw = cipher.encrypt(password), password

    def __str__(self):
        """Used for representing value in console."""
        return '******' if self.encrypted else '-'

    def to_config_string(self):
        """Used for representing value to be stored in file."""
        return self.encrypted if self.raw else '-'


class ConfigEntry(object):
    def __init__(self, **kwargs):
        self.options = kwargs

    def __getattr__(self, item):
        try:
            return self.options[item]
        except KeyError:
            raise AttributeError('No attribute: {}'.format(item))


class AgentConfigEntry(ConfigEntry):
    def __init__(self, name, agent_ip, log_level, log_file, log_file_maxbytes,
                 log_file_count, cache_interval=None, agent_port=None,
                 model=None, mgmt_ip=None, user=None, password=None):
        super(AgentConfigEntry, self).__init__(
            name=name, agent_ip=agent_ip, log_level=log_level,
            log_file=log_file, log_file_maxbytes=log_file_maxbytes,
            log_file_count=log_file_count, cache_interval=cache_interval,
            agent_port=agent_port, model=model,
            mgmt_ip=mgmt_ip, user=user, password=Password(password))


USER_V2_HEAD = '# model security_name community'
USER_V2_SHOW_HEAD = 'SNMP Version 2 Community Access:'
USER_V2_SHOW = '''{name}
    Version:    {mode}
    Community:  {community}'''
USER_V3_HEAD = '# model security_name context security_level ' \
               'auth_protocol auth_key priv_protocol priv_key'
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
        kwargs[k] = to_console_str(v)

    return format_str.format(**kwargs)


class UserV2ConfigEntry(ConfigEntry):
    def __init__(self, name, community):
        super(UserV2ConfigEntry, self).__init__(
            name=name, mode=V2,
            community=name)

    def __str__(self):
        """Used for representing value in console."""
        return _show(USER_V2_SHOW, name=self.name, mode=self.mode,
                     community=self.community)

    def to_config_string(self):
        """Used for representing value to be stored in file."""
        return ' '.join('-' if not item else item.to_config_string()
                        for item in (
                            self.mode, Serializable(self.name),
                            Serializable(self.community)))


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
        """Used for representing value in console."""

        return _show(USER_V3_SHOW, name=self.name, mode=self.mode,
                     security_level=self.security_level,
                     auth_protocol=self.auth_protocol, auth_key=self.auth_key,
                     priv_protocol=self.priv_protocol, priv_key=self.priv_key)

    def to_config_string(self):
        """Used for representing value to be stored in file."""

        return ' '.join('-' if not item else item.to_config_string()
                        for item in (self.mode, Serializable(self.name),
                                     self.context,
                                     self.security_level,
                                     self.auth_protocol, self.auth_key,
                                     self.priv_protocol, self.priv_key))


class AgentConfigParser(object):
    def __init__(self, conf_file):
        self._conf_file = conf_file
        self._parser = configparser.ConfigParser()
        self._parser.read(conf_file)
        self._writer = configparser.ConfigParser()
        self._writer.read(conf_file)

    def parse(self):
        res = OrderedDict()
        agent_port_list = []
        for section in self._parser.sections():
            res[section] = AgentConfigEntry(
                section, **dict(self._parser.items(section)))
            agent_port = res[section].agent_port if res[
                section].agent_port else 161
            if agent_port in agent_port_list:
                raise snmp_ex.PortConflictError(
                    'SNMP Agent port conflict: {}'.format(agent_port))
            else:
                agent_port_list.append(agent_port)
        res.default_section = AgentConfigEntry(
            'DEFAULT', **dict(self._parser.defaults()))
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
        v2 = [e.to_config_string() for e in v2]
        v3 = [e.to_config_string() for e in v3]

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
        if not self._file_exists(conf_file):
            raise snmp_ex.FileNotFound(
                "Config file '{}' not found.".format(conf_file))

    def _file_exists(self, name):
        if os.path.exists(name) and os.path.isfile(name):
            return True
        return False

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

    def raise_if_error(self):
        """Try to validate the configuration before starts engine."""
        self.parser.parse()


class AgentConfig(FileConfig):
    _PARSER_CLZ = AgentConfigParser


class UserConfig(FileConfig):
    _PARSER_CLZ = UserConfigParser

    @staticmethod
    def split_v2_v3(all_entries):
        # must be sorted, since `groupby` works like Linux `uniq` command
        all_entries = sorted(all_entries.values(),
                             key=lambda v: v.mode)
        groups = dict((k, list(g)) for k, g in
                      itertools.groupby(all_entries,
                                        lambda e: e.mode))
        return (groups[V2] if V2 in groups else [],
                groups[V3] if V3 in groups else [])
