def enum(enum_clz, value):
    if isinstance(value, enum_clz):
        return value
    return enum_clz.from_str(value) if value else None
