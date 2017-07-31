from clients import UnityClient


def create_unity_client(engine):
    storage_context = engine.storage_context
    client_name = storage_context.spa + '_' + storage_context.port
    try:
        engine.unity_client = UnityClient.get_unity_client(client_name,
                                                           storage_context.spa,
                                                           storage_context.user,
                                                           storage_context.password)
    except:
        print('Failed to connect unity: %s' % storage_context.spa)
        engine.unity_client = None
    return engine


class ScalarInstanceFactory(object):
    @staticmethod
    def build(name, base_class, impl_class):
        def __init__(self, *args, **kwargs):
            self.impl_class = impl_class
            base_class.__init__(self, *args, **kwargs)

        def __read_get__(self, name, val, idx, acInfo):
            engine = acInfo[1]

            if engine.unity_client == None:
                engine = create_unity_client(engine)

            if engine.unity_client == None:
                # return name, self.getSyntax().clone('Failed to connect unity.')
                return name, self.getSyntax().clone()

            idx_len = self.instId[0]
            idx_name = ''.join([chr(x) for x in self.instId[1: idx_len + 1]])

            try:
                return name, self.getSyntax().clone(
                    self.impl_class().read_get(name, idx_name,
                                               engine.unity_client)
                )
            except:
                # TODO: logging ...
                return name, self.getSyntax().clone()
                # raise

        newclass = type(name + "ScalarInstance", (base_class,),
                        {"__init__": __init__,
                         "readGet": __read_get__
                         })
        return newclass


class TableColumnInstanceFactory(object):
    @staticmethod
    def build(name, base_class, proto_inst, entry, impl_class):
        def __init__(self, *args, **kwargs):
            self.entry = entry
            self.impl_class = impl_class
            self.maxAccess = 'readcreate'
            base_class.__init__(self, *args, **kwargs)

        def __read_getnext__(self, name, val, idx, acInfo, oName=None):
            engine = acInfo[1]
            if engine.unity_client == None:
                engine = create_unity_client(engine)

            if engine.unity_client == None:
                # TODO: need to consider how to handle this scenario
                return

            if self.name == name:
                row_list = self.impl_class().get_idx(name, idx,
                                                     engine.unity_client)
                self.unregisterSubtrees(*self._vars.keys())
                for row in row_list:
                    row_instance_id = self.entry.getInstIdFromIndices(row)
                    self.createTest(name + row_instance_id, val, idx, acInfo)
                    self.createCommit(name + row_instance_id, val, idx, acInfo)
            next_node = self.getNextNode(name, idx)
            return next_node.readGet(next_node.name, val, idx, acInfo)

        newclass = type(name + "Instance", (base_class,),
                        {"__init__": __init__,
                         "protoInstance": proto_inst,
                         "readGetNext": __read_getnext__})
        return newclass
