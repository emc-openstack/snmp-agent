import os

from pysmi.codegen import JsonCodeGen
from pysmi.codegen.symtable import SymtableCodeGen
from pysmi.reader.localfile import FileReader
from pysmi.searcher.pyfile import PyFileSearcher
from pysmi.searcher.pypackage import PyPackageSearcher
from pysmi.searcher.stub import StubSearcher
from pysmi.writer.pyfile import PyFileWriter
from pysmi.parser.smi import SmiV2Parser
from pysmi.codegen.pysnmp import PySnmpCodeGen, baseMibs
from pysmi.compiler import MibCompiler


class InMemoryMibGenerator(object):
    def __init__(self):
        self.oids = {}

    def putData(self, mibname, data, comments=(), dryRun=False):
        self.oids[mibname] = [(name, value) for (name, value) in data.items()
                              if (not name.startswith("_"))]

    def getData(self, filename):
        pass

    def getOids(self):
        return self.oids


def get_mib_symbols():
    mib_generator = InMemoryMibGenerator()
    mibCompiler = MibCompiler(SmiV2Parser(), SymtableCodeGen(), mib_generator)
    mibCompiler.addSources(FileReader(os.path.abspath('../mib')))
    mibCompiler.addSearchers(StubSearcher(*baseMibs))
    mibCompiler.compile('Unity-MIB')

    return mib_generator.getOids()