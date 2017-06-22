class ScalarInstanceFactory(object):
    @staticmethod
    def build(name, base_class, impl_class):
        def __init__(self, *args, **kwargs):
            self.impl_class = impl_class
            base_class.__init__(self, *args, **kwargs)

        def __get_value__(self, name, idx):
            return self.getSyntax().clone(
                self.impl_class().get_value(name, idx)
            )

        newclass = type(name + "ScalarInstance", (base_class,),
                        {"__init__": __init__,
                         "getValue": __get_value__})
        return newclass


class TableColumnInstanceFactory(object):
    @staticmethod
    def build(name, base_class, proto_inst, entry):
        def __init__(self, *args, **kwargs):
            self.entry = entry
            self.maxAccess = 'readcreate'
            base_class.__init__(self, *args, **kwargs)

        def __read_getnext__(self, name, val, idx, acInfo, oName=None):
            if self.name == name:
                # TODO: need to get row_list first
                row_list = ['a', 'b', 'c']
                for row in row_list:
                    row_instance_id = self.entry.getInstIdFromIndices(row)
                    # TODO: destory subtree first?
                    self.createTest(name + row_instance_id, val, idx, acInfo)
                    self.createCommit(name + row_instance_id, val, idx, acInfo)
            next_node = self.getNextNode(name, idx)
            return next_node.readGet(next_node.name, val, idx, acInfo)

        newclass = type(name + "ColumnInstance", (base_class,),
                        {"__init__": __init__,
                         "protoInstance": proto_inst,
                         "readGetNext": __read_getnext__})
        return newclass
