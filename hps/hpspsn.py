# -*- coding: utf-8 -*-
"""HPS-Poisson-Data.
"""
import numpy as np
from hpsolver.hps import hpsdata



class HPSPoisson(hpsdata.HPSData):
    """HPS-Poisson data.

    - Derived from `HPSData`.
    - Implements P1-FEM for the Poisson equation.

    Attributes
    ----------
    body : 2x2-float-matrix.
        Potential and density stored row-by-row.

    Notes
    -----

    Operator used:

    ```
    Uxx = Rho
    ```

    with `U` being the potential and `Rho` being the density.

    """

    SIZE = 1

    WEST_MERGE = np.array([[0.5], [0.5]])
    EAST_MERGE = np.array([[0.5], [0.5]])

    WEST_SPLIT = np.array([[1.0, 0.0], [0.5, 0.5]]).T
    EAST_SPLIT = np.array([[0.5, 0.5], [0.0, 1.0]]).T

    @property
    def pot(self):
        """Potential.
        """
        return self.body[0, :]

    @property
    def rho(self):
        """Density.
        """
        return self.body[1, :]

    def new_body_west(self):

        if self.body is None:
            return None

        return self.body @ self.WEST_SPLIT

    def new_body_east(self):

        if self.body is None:
            return None

        return self.body @ self.EAST_SPLIT

    def new_body_join(self, west_data, east_data):

        if west_data.body is None:
            return None

        if east_data.body is None:
            return None

        west = west_data.body @ self.WEST_MERGE
        east = east_data.body @ self.EAST_MERGE

        return np.hstack([west, east])

    def make_sol(self):

        self.body[0, 0] = self.dtnopr.u_1[0]
        self.body[0, 1] = self.dtnopr.u_2[0]

    def mat_from_body(self):

        g_x = 1.0 / self.d_x

        return {
            'a11': - np.r_[g_x],
            'a12': + np.r_[g_x],
            'a21': - np.r_[g_x],
            'a22': + np.r_[g_x]
        }

    def vec_from_body(self):

        if self.body is None:
            return {
                'b_1': np.r_[0],
                'b_2': np.r_[0]
            }

        r_1 = self.rho[0] * (self.d_x * 0.5)
        r_2 = self.rho[1] * (self.d_x * 0.5)

        return {
            'b_1': - np.r_[r_1],
            'b_2': + np.r_[r_2]
        }
