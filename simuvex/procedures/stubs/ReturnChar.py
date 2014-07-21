import simuvex

######################################
# Returns a valid char
######################################

class ReturnChar(simuvex.SimProcedure):
    def __init__(self): # pylint: disable=W0231,
        s_var = self.state.new_symbolic("char_ret", self.state.arch.bits)
        self.state.add_constraints(self.state.claripy.And(self.state.claripy.ULE(s_var, 126), self.state.claripy.UGE(s_var, 9)))
        self.exit_return(s_var)
