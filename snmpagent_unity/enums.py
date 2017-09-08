import enum


class CaseInsensitiveEnum(enum.Enum):
    @property
    def description(self):
        return self.value[1]

    @property
    def index(self):
        return self.value[0]

    def to_config_string(self):
        return self.index

    @classmethod
    def from_str(cls, value):
        try:
            return [m for m in cls if m.index.lower() == value.lower()][0]
        except IndexError:
            return None

    def __str__(self):
        return self.description

    def __lt__(self, other):
        # An equivalent for cmp(self.value, other.value)
        # https://docs.python.org/3.0/whatsnew/3.0.html#ordering-comparisons
        return (self.index > other.index) - (
            self.index < other.index)


class UserVersion(CaseInsensitiveEnum):
    V2 = ('SNMPv2c', 'SNMP Version 2c')
    V3 = ('SNMPv3', 'SNMP Version 3')


class Community(CaseInsensitiveEnum):
    PUBLIC = ('public', 'Public')
    PRIVATE = ('private', 'Private')


class AuthProtocol(CaseInsensitiveEnum):
    MD5 = ('MD5', 'MD5')
    SHA = ('SHA', 'SHA')


class PrivProtocol(CaseInsensitiveEnum):
    AES = ('AES', 'AES')
    DES = ('DES', 'DES')


class SecurityLevel(CaseInsensitiveEnum):
    NO_AUTH_NO_PRIV = ('noAuthNoPriv', 'No Authentication')
    AUTH_NO_PRIV = ('authNoPriv', 'Authentication')
    AUTH_PRIV = ('authPriv', "Authentication and Privacy")
