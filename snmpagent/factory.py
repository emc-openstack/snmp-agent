class ScalarInstanceFactory(object):
    @staticmethod
    def build(name, base_class, impl_class, get_value):
        def __init__(self, *args, **kwargs):
            self.impl_class = impl_class
            self.method_get_value = get_value
            base_class.__init__(self, *args, **kwargs)

        def __get_value__(self, name, idx):
            return self.getSyntax().clone(
                self.impl_class().__getattribute__(self.method_get_value)(
                    name, idx)
            )

        newclass = type(name + "ScalarInstance", (base_class,),
                        {"__init__": __init__,
                         "getValue": __get_value__})
        return newclass