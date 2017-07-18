from clients import UnityClient


class ScalarInstanceFactory(object):
    @staticmethod
    def build(name, base_class, impl_class):
        def __init__(self, *args, **kwargs):
            self.impl_class = impl_class
            base_class.__init__(self, *args, **kwargs)

        def __read_get__(self, name, val, idx, acInfo):
            engine = acInfo[1]
            if engine.unity_client == None:
                storage_context = engine.storage_context
                client_name = storage_context.spa + '_' + storage_context.port
                try:
                    engine.unity_client = UnityClient.get_unity_client(client_name, storage_context.spa,
                                                                       storage_context.user,
                                                                       storage_context.password)
                except:
                    engine.unity_client = None

            if engine.unity_client == None:
                return

            idx_len = self.instId[0]
            idx_name = ''.join([chr(x) for x in self.instId[1: idx_len + 1]])

            try:
                return name, self.getSyntax().clone(
                    self.impl_class().read_get(name, idx_name, engine.unity_client)
                )
            except:
                # TODO: logging ...
                raise

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
                storage_context = engine.storage_context
                client_name = storage_context.spa + '_' + storage_context.port
                try:
                    engine.unity_client = UnityClient.get_unity_client(client_name, storage_context.spa,
                                                                       storage_context.user,
                                                                       storage_context.password)
                except:
                    engine.unity_client = None

            if engine.unity_client == None:
                # TODO: need to consider how to handle this scenario
                return

            if self.name == name:
                # TODO: need to get row_list first
                row_list = self.impl_class().get_idx(name, idx, engine.unity_client)
                for row in row_list:
                    row_instance_id = self.entry.getInstIdFromIndices(row)
                    # TODO: destory subtree first?
                    self.createTest(name + row_instance_id, val, idx, acInfo)
                    self.createCommit(name + row_instance_id, val, idx, acInfo)
                    # TODO: use 1, 2, 3, ... as idx
                    # for row_id, row in enumerate(row_list, 1):
                    #     val = self.entry.getInstIdFromIndices(row)
                    #     self.createTest(name + (row_id,), val, idx, acInfo)
                    #     self.createCommit(name + (row_id,), val, idx, acInfo)
            next_node = self.getNextNode(name, idx)
            return next_node.readGet(next_node.name, val, idx, acInfo)

        newclass = type(name + "Instance", (base_class,),
                        {"__init__": __init__,
                         "protoInstance": proto_inst,
                         "readGetNext": __read_getnext__})
        return newclass
