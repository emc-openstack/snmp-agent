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


class UserConfigError(SNMPAgentException):
    pass


class UserExistingError(SNMPAgentException):
    pass


class UserNotExistsError(SNMPAgentException):
    pass


class NotSupportedPlatformError(SNMPAgentException):
    pass
