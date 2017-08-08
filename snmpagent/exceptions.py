class SNMPAgentException(Exception):
    pass


class PortConflictError(SNMPAgentException):
    pass


class UserConfigError(SNMPAgentException):
    pass


class UserExistingError(SNMPAgentException):
    pass


class NotSupportedPlatformError(SNMPAgentException):
    pass
