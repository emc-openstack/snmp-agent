import enum


class CaseInsensitiveEnum(enum.Enum):
    @classmethod
    def from_str(cls, value):
        try:
            return [m for m in cls if m.value.lower() == value.lower()][0]
        except IndexError:
            return None

    def __str__(self):
        return self.value

    def __lt__(self, other):
        # An equivalent for cmp(self.value, other.value)
        # https://docs.python.org/3.0/whatsnew/3.0.html#ordering-comparisons
        return (self.value > other.value) - (self.value < other.value)


class UserVersion(CaseInsensitiveEnum):
    V2 = 'SNMPv2c'
    V3 = 'SNMPv3'


class Community(CaseInsensitiveEnum):
    PUBLIC = 'public'
    PRIVATE = 'private'


class AuthProtocol(CaseInsensitiveEnum):
    MD5 = 'MD5'
    SHA = 'SHA'


class PrivProtocol(CaseInsensitiveEnum):
    AES = 'AES'
    DES = 'DES'


class SecurityLevel(CaseInsensitiveEnum):
    NO_AUTH_NO_PRIV = 'noAuthNoPriv'
    AUTH_NO_PRIV = 'authNoPriv'
    AUTH_PRIV = 'authPriv'
