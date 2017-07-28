class SNMPAgentException(Exception):
    pass


class UserConfigError(SNMPAgentException):
    pass


class UserExistingError(SNMPAgentException):
    pass


class NotSupportedPlatformError(SNMPAgentException):
    pass
