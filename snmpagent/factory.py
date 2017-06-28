from clients import UnityClient


class ScalarInstanceFactory(object):
    @staticmethod
    def build(name, base_class, impl_class):
        def __init__(self, *args, **kwargs):
            # TODO: instanciate UnityClient here?
            self.impl_class = impl_class
            base_class.__init__(self, *args, **kwargs)

        def __read_get__(self, name, val, idx, acInfo):
            try:
                storage_context = acInfo[1].storage_context
                # TODO: instanciate unique UnityClient instance for (host, username, password)
                client_name = storage_context.spa + '_' + storage_context.port
                unity_client = UnityClient.get_unity_client(client_name, storage_context.spa, storage_context.user,
                                                            storage_context.password)

                idx_name = ''.join([chr(x) for x in self.instId[1:]])
                print(idx_name)
                return name, self.getSyntax().clone(
                    self.impl_class().read_get(name, idx_name, unity_client)
                )

            except:
                # logging ...
                # return name, self.getSyntax().clone(
                #     # "exception"
                # )
                pass

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
            storage_context = acInfo[1].storage_context
            client_name = storage_context.spa + '_' + storage_context.port
            unity_client = UnityClient.get_unity_client(client_name, storage_context.spa, storage_context.user,
                                                        storage_context.password)

            if self.name == name:
                # TODO: need to get row_list first
                row_list = self.impl_class().get_idx(name, idx, unity_client)
                for row in row_list:
                    row_instance_id = self.entry.getInstIdFromIndices(row)
                    # TODO: destory subtree first?
                    self.createTest(name + row_instance_id, val, idx, acInfo)
                    self.createCommit(name + row_instance_id, val, idx, acInfo)
            next_node = self.getNextNode(name, idx)
            return next_node.readGet(next_node.name, val, idx, acInfo)

        newclass = type(name + "Instance", (base_class,),
                        {"__init__": __init__,
                         "protoInstance": proto_inst,
                         "readGetNext": __read_getnext__})
        return newclass
