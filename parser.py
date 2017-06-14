import os

from pysmi.reader.localfile import FileReader
from pysmi.searcher.pyfile import PyFileSearcher
from pysmi.searcher.pypackage import PyPackageSearcher
from pysmi.searcher.stub import StubSearcher
from pysmi.writer.pyfile import PyFileWriter
from pysmi.parser.smi import SmiV2Parser
from pysmi.codegen.pysnmp import PySnmpCodeGen, baseMibs
from pysmi.compiler import MibCompiler

class MibOIDParser(object):
    def putData(self, mibname, data, comments=(), dryRun=False):
       pass

    def genCode(self, ast, symbolTable, **kwargs):
        sorted(symbolTable.get("Unity-MIB").keys())
        pass

mibCompiler = MibCompiler(SmiV2Parser(), MibOIDParser(), MibOIDParser())
mibCompiler.addSources(FileReader(os.path.abspath('./mib')))
# mibCompiler.addSearchers(PyFileSearcher('/tmp/pysnmp/mibs'))
# mibCompiler.addSearchers(PyPackageSearcher('pysnmp.mibs'))
mibCompiler.addSearchers(StubSearcher(*baseMibs))
results = mibCompiler.compile('Unity-MIB')
x = "1"


