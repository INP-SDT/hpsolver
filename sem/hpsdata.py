# -*- coding: utf-8 -*-
"""HPS data.
"""
import numpy as np
from hpsolver import hps
from hpsolver.sem import specunit
from hpsolver.sem import operator


class HPSData(hps.HPSData):
    """HPS data object.
    """

    SIZE = 1

    def new_body_west(self):

        if self.body is None:
            return None

        return self.body @ self.cache['unit'].splitmats[0].T

    def new_body_east(self):

        if self.body is None:
            return None

        return self.body @ self.cache['unit'].splitmats[1].T

    def new_body_join(self, west_data, east_data):

        if west_data.body is None:
            return None

        if east_data.body is None:
            return None

        mat1 = west_data.cache['unit'].joinmats[0]
        mat2 = east_data.cache['unit'].joinmats[1]

        west = west_data.body @ mat1.T
        east = east_data.body @ mat2.T

        return west + east

    @property
    def unit(self):
        return self.cache['unit']

    @property
    def oprt(self):
        return self.cache['oprt']

    @property
    def avec(self):
        return self.cache['coefs']['a']

    @property
    def bvec(self):
        return self.cache['coefs']['b']

    @property
    def cvec(self):
        return self.cache['coefs']['c']

    @property
    def dvec(self):
        return self.cache['coefs']['d']

    def activate(self, order):
        """Activates the node for computing.

        Parameters
        ----------
        order : int
            Order of the node (3-6).

        """
        self.cache['unit'] = specunit.getunit(order + 1)
        self.cache['oprt'] = operator.getoprt(order + 1)

    def reset(self):
        """Deactivates the node.
        """
        self.body = None
        self.cache = {}

    def setcoeffs(self, data):
        """Defines the equation coefficients.

        Parameters
        ----------
        data : dict
            Provides equation coefficients as lists.

        """

        self.cache['coefs'] = {
            'a': data['a'].pop(),
            'b': data['b'].pop(),
            'c': data['c'].pop(),
            'd': data['d'].pop()
        }

    def solve(self):
        """Performs local solve step.
        """

        amat = self.unit.conver(self.avec)
        bmat = self.unit.differ(self.bvec)
        cmat = self.unit.masser(self.cvec)
        dvec = self.unit.source(self.dvec)

        bmat = bmat * (2.0 / self.d_x)

        cmat = cmat * self.d_x * 0.5
        dvec = dvec * self.d_x * 0.5

        self.oprt.feed(
            - amat + bmat + cmat, dvec
        )

        self.oprt.solve()

    def get_points(self):
        return self.x_0 + 0.5 * self.d_x * self.cache['unit'].points

    def get_grad(self):
        return self.unit.grad(self.body) * (2.0 / self.d_x)

    def mat_from_body(self):
        return {
            'a11': self.oprt.get_a11(),
            'a12': self.oprt.get_a12(),
            'a21': self.oprt.get_a21(),
            'a22': self.oprt.get_a22()
        }

    def vec_from_body(self):
        return {
            'b_1': self.oprt.get_b_1(),
            'b_2': self.oprt.get_b_2()
        }

    def make_sol(self):

        u_1 = self.u_1[:]
        u_2 = self.u_2[:]

        q_1 = self.oprt.sol.q_1
        q_2 = self.oprt.sol.q_2
        rhs = self.oprt.sol.vec

        self.body = np.r_[
            u_1, q_1 * u_1 + q_2 * u_2 + rhs, u_2
        ]
