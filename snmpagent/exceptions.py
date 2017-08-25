class SNMPAgentException(Exception):
    pass


class UnityException(SNMPAgentException):
    pass


class UnityConnectionError(UnityException):
    pass


class UnityResponseError(UnityException):
    pass


class PortConflictError(SNMPAgentException):
    pass


class UserException(SNMPAgentException):
    pass


class UserConfigError(UserException):
    pass


class FileNotFound(UserException):
    pass


class UserExistingError(UserException):
    pass


class UserNotExistsError(UserException):
    pass


class UserInvalidPasswordError(UserException):
    pass


class UserInvalidProtocolError(UserException):
    pass


class NotSupportedPlatformError(SNMPAgentException):
    pass
