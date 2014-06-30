from raco.datalog.grammar import parse
from raco.language.myrialang import MyriaLeftDeepTreeAlgebra
from raco.algebra import LogicalAlgebra
from raco.compile import optimize

import logging
LOG = logging.getLogger(__name__)


class RACompiler(object):
    """Thin wrapper interface for lower level functions parse, optimize,
    compile"""

    def fromDatalog(self, program):
        """Parse datalog and convert to RA"""
        self.physicalplan = None
        self.target = None
        self.source = program
        self.parsed = parse(program)
        LOG.debug("parser output: %s", self.parsed)
        self.logicalplan = self.parsed.toRA()

    def optimize(self, target=MyriaLeftDeepTreeAlgebra(),
                 eliminate_common_subexpressions=False,
                 environment_variables=None):
        """Convert logical plan to physical plan"""
        self.target = target
        self.physicalplan = optimize(
            self.logicalplan,
            target=self.target,
            source=LogicalAlgebra,
            eliminate_common_subexpressions=eliminate_common_subexpressions
        )
