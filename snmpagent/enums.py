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


class UserVersion(CaseInsensitiveEnum):
    V2 = 'SNMPv2c'
    V3 = 'SNMPv3'


class Community(CaseInsensitiveEnum):
    PUBLIC = 'Public'
    PRIVATE = 'Private'


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
