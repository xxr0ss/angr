from __future__ import annotations
import angr


class UnresolvableJumpTarget(angr.SimProcedure):
    NO_RET = True

    def run(self):  # pylint: disable=arguments-differ
        return
