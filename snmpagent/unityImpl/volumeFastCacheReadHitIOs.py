from pysnmp import cache, debug
from pysnmp.smi import exval, error
from pyasn1.error import PyAsn1Error


class volumeFastCacheReadHitIOs(object):
    def get_value(self, name, idx):
        return "VolumeFastCacheReadHitIOs"

    def getBranch(self, name, idx):
        if name in self._vars:
            return self._vars[name]
        raise error.NoSuchInstanceError(name=name, idx=idx)

    def setProtoInstance(self, protoInstance):
        self.protoInstance = protoInstance

    # Column creation (this should probably be converted into some state
    # machine for clarity). Also, it might be a good idea to inidicate
    # defaulted cols creation in a clearer way than just a val == None.

    def createTest(self, name, val, idx, acInfo):
        (acFun, acCtx) = acInfo
        # Make sure creation allowed, create a new column instance but
        # do not replace the old one
        if name == self.name:
            raise error.NoAccessError(idx=idx, name=name)
        if acFun:
            if val is not None and self.maxAccess != 'readcreate' or \
                    acFun(name, self.syntax, idx, 'write', acCtx):
                debug.logger & debug.flagACL and debug.logger(
                    'createTest: %s=%r %s at %s' % (name, val, self.maxAccess, self.name))
                raise error.NoCreationError(idx=idx, name=name)
        # Create instances if either it does not yet exist (row creation)
        # or a value is passed (multiple OIDs in SET PDU)
        if val is None and name in self.__createdInstances:
            return
        self.__createdInstances[name] = self.protoInstance(
            self.name, name[len(self.name):], self.syntax.clone()
        )
        self.__createdInstances[name].createTest(name, val, idx, acInfo)

    def createCommit(self, name, val, idx, acInfo):
        # Commit new instance value
        if name in self._vars:  # XXX
            if name in self.__createdInstances:
                self._vars[name].createCommit(name, val, idx, acInfo)
            return
        self.__createdInstances[name].createCommit(name, val, idx, acInfo)
        # ...commit new column instance
        self._vars[name], self.__createdInstances[name] = \
            self.__createdInstances[name], self._vars.get(name)

    def createCleanup(self, name, val, idx, acInfo):
        # Drop previous column instance
        self.branchVersionId += 1
        if name in self.__createdInstances:
            if self.__createdInstances[name] is not None:
                self.__createdInstances[name].createCleanup(name, val, idx,
                                                            acInfo)
            del self.__createdInstances[name]
        elif name in self._vars:
            self._vars[name].createCleanup(name, val, idx, acInfo)

    def createUndo(self, name, val, idx, acInfo):
        # Set back previous column instance, drop the new one
        if name in self.__createdInstances:
            self._vars[name] = self.__createdInstances[name]
            del self.__createdInstances[name]
            # Remove new instance on rollback
            if self._vars[name] is None:
                del self._vars[name]
            else:
                # Catch half-created instances (hackerish)
                try:
                    self._vars[name] == 0
                except PyAsn1Error:
                    del self._vars[name]
                else:
                    self._vars[name].createUndo(name, val, idx, acInfo)

    # Column destruction

    def destroyTest(self, name, val, idx, acInfo):
        (acFun, acCtx) = acInfo
        # Make sure destruction is allowed
        if name == self.name:
            raise error.NoAccessError(idx=idx, name=name)
        if name not in self._vars:
            return
        if acFun:
            if val is not None and self.maxAccess != 'readcreate' or \
                    acFun(name, self.syntax, idx, 'write', acCtx):
                raise error.NoAccessError(idx=idx, name=name)
        self._vars[name].destroyTest(name, val, idx, acInfo)

    def destroyCommit(self, name, val, idx, acInfo):
        # Make a copy of column instance and take it off the tree
        if name in self._vars:
            self._vars[name].destroyCommit(name, val, idx, acInfo)
            self.__destroyedInstances[name] = self._vars[name]
            del self._vars[name]

    def destroyCleanup(self, name, val, idx, acInfo):
        # Drop instance copy
        self.branchVersionId += 1
        if name in self.__destroyedInstances:
            self.__destroyedInstances[name].destroyCleanup(name, val,
                                                           idx, acInfo)
            debug.logger & debug.flagIns and debug.logger('destroyCleanup: %s=%r' % (name, val))
            del self.__destroyedInstances[name]

    def destroyUndo(self, name, val, idx, acInfo):
        # Set back column instance
        if name in self.__destroyedInstances:
            self._vars[name] = self.__destroyedInstances[name]
            self._vars[name].destroyUndo(name, val, idx, acInfo)
            del self.__destroyedInstances[name]

    def writeCommit(self, name, val, idx, acInfo):
        self.__delegateWrite('Commit', name, val, idx, acInfo)
        if name in self.__rowOpWanted:
            raise self.__rowOpWanted[name]

    def writeCleanup(self, name, val, idx, acInfo):
        self.branchVersionId += 1
        self.__delegateWrite('Cleanup', name, val, idx, acInfo)
        if name in self.__rowOpWanted:
            e = self.__rowOpWanted[name]
            del self.__rowOpWanted[name]
            debug.logger & debug.flagIns and debug.logger('%s dropped by %s=%r' % (e, name, val))
            raise e

    def writeUndo(self, name, val, idx, acInfo):
        if name in self.__rowOpWanted:
            self.__rowOpWanted[name] = error.RowDestructionWanted()
        self.__delegateWrite('Undo', name, val, idx, acInfo)
        if name in self.__rowOpWanted:
            e = self.__rowOpWanted[name]
            del self.__rowOpWanted[name]
            debug.logger & debug.flagIns and debug.logger('%s dropped by %s=%r' % (e, name, val))
            raise e