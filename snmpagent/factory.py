class ScalarInstanceFactory(object):
    @staticmethod
    def build(name, class_impl, method_get_value, base_class):
        def __init__(self, *args, **kwargs):
            self.class_impl = class_impl
            self.method_get_value = method_get_value
            base_class.__init__(self, *args, **kwargs)

        def __get_value__(self, name, idx):
            return self.getSyntax().clone(
                self.class_impl.__getattribute__(self.method_get_value)(
                    name, idx)
            )

        newclass = type(name + "ScalarInstance", (base_class,),
                        {"__init__": __init__,
                         "getValue": __get_value__})
        return newclass