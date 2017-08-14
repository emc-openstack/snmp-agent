import os

from pysmi.codegen.pysnmp import baseMibs
from pysmi.codegen.symtable import SymtableCodeGen
from pysmi.compiler import MibCompiler
from pysmi.parser.smi import SmiV2Parser
from pysmi.reader.localfile import FileReader
from pysmi.searcher.stub import StubSearcher


class InMemoryMibParser(object):
    def __init__(self):
        self.oids = {}

    def putData(self, mibname, data, comments=(), dryRun=False):
        self.oids[mibname] = [(name, value) for (name, value) in data.items()
                              if (not name.startswith("_"))]

    def getData(self, filename):
        pass

    def getOids(self, name):
        return self.oids.get(name)


def get_mib_symbols(name):
    mib_parser = InMemoryMibParser()
    mibCompiler = MibCompiler(SmiV2Parser(), SymtableCodeGen(), mib_parser)
    # Add Unity-MIB mib file to source dir
    mib_dir_path = os.path.join(os.path.dirname(__file__), '..', 'docs',
                                'mibs')
    mibCompiler.addSources(FileReader(mib_dir_path))
    mibCompiler.addSearchers(StubSearcher(*baseMibs))
    mibCompiler.compile(name)

    return mib_parser.getOids(name)
