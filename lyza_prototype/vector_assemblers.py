import itertools
from lyza_prototype.assembler import VectorAssembler
import numpy as np

class FunctionVector(VectorAssembler):
    def set_param(self, function, time):
        self.function = function
        self.time = time

    def calculate_element_vector(self, cell):
        n_node = len(cell.nodes)
        n_dof = n_node*self.function_size
        K = np.zeros((n_dof, n_dof))

        W_arr = self.mesh.quantities['W'].get_quantity(cell)
        N_arr = self.mesh.quantities['N'].get_quantity(cell)
        B_arr = self.mesh.quantities['B'].get_quantity(cell)
        DETJ_arr = self.mesh.quantities['DETJ'].get_quantity(cell)
        XG_arr = self.mesh.quantities['XG'].get_quantity(cell)

        f = np.zeros((n_dof,1))

        for idx in range(len(W_arr)):
            f_val = self.function(XG_arr[idx], self.time)
            N = N_arr[idx]
            W = W_arr[idx][0,0]
            DETJ = DETJ_arr[idx][0,0]

            for I, i in itertools.product(range(n_node), range(self.function_size)):
                alpha = I*self.function_size + i
                f[alpha] += f_val[i]*N[I,0]*DETJ*W

        return f