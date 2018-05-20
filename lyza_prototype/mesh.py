from lyza_prototype.node import Node
from lyza_prototype.cell_quantity import CellQuantity

class Mesh:

    def __init__(self):
        self.nodes = []
        self.cells = []
        self.boundary_cells = []

        self.construct_mesh()

        for idx, n in enumerate(self.nodes):
            n.idx = idx

        for idx, c in enumerate(self.cells):
            c.idx = idx

    def construct_mesh(self):
        pass

    def add_node(self, coors):
        self.nodes.append(Node(coors, len(self.nodes)))

    def add_cell(self, cell):
        self.cells.append(cell)

    def get_n_nodes(self):
        return len(self.nodes)

    def get_basic_quantities(self, quadrature_degree_map, spatial_dim, domain=None, skip_basis=False):
        quantity_dict = {}

        quad_weight = CellQuantity(self, (1,1))
        quad_coor = CellQuantity(self, (3,1))

        for idx, cell in enumerate(self.cells):
            if domain:
                pass
            else:
                if cell.is_boundary: continue

            degree = quadrature_degree_map(cell)
            quad_weights, quad_coors = cell.get_quad_points(degree)

            for weight in quad_weights:
                quad_weight.add_quantity_by_cell_idx(idx, weight)

            for coor in quad_coors:
                quad_coor.add_quantity_by_cell_idx(idx, coor)

        quantity_dict = {
            'XL': quad_coor,
            'W': quad_weight,
        }

        if not skip_basis:
            N = CellQuantity(self, (1,1))
            B = CellQuantity(self, (1, spatial_dim))
            J = CellQuantity(self, (spatial_dim, 1))
            DETJ = CellQuantity(self, (1,1))
            JINVT = CellQuantity(self, (1,spatial_dim))
            XG = CellQuantity(self, (3, 1))

            for idx, cell in enumerate(self.cells):
                if domain:
                    pass
                else:
                    if cell.is_boundary: continue

                degree = quadrature_degree_map(cell)

                N_arr, B_arr, J_arr, DETJ_arr, JINVT_arr, XG_arr \
                    = cell.calculate_basis_values(spatial_dim, degree)

                for i in N_arr: N.add_quantity_by_cell_idx(idx, i)
                for i in B_arr: B.add_quantity_by_cell_idx(idx, i)
                for i in J_arr: J.add_quantity_by_cell_idx(idx, i)
                for i in DETJ_arr: DETJ.add_quantity_by_cell_idx(idx, i)
                for i in JINVT_arr: JINVT.add_quantity_by_cell_idx(idx, i)
                for i in XG_arr: XG.add_quantity_by_cell_idx(idx, i)

        quantity_dict = {
            **quantity_dict,
            'N': N,
            'B': B,
            'J': J,
            'DETJ': DETJ,
            'JINVT': JINVT,
            'XG': XG,
        }

        return quantity_dict

