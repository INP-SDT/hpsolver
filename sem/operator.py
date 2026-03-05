# -*- coding: utf-8 -*-
"""Local solution operator.
"""
import numpy as np


def getoprt(order):
    """Creates a local operator.

    Parameters
    ----------
    order : int
        Number of computing nodes.

    """
    return NodeOpr(order)


class OprData:
    """Base of the local solution operator.
    """

    def __init__(self, size):
        self.mat = np.zeros((size, size))
        self.vec = np.zeros(size)
        self.sol = NodeSol(size)

    @property
    def m11(self):
        return self.mat[+0, +0]

    @property
    def m1n(self):
        return self.mat[+0, -1]

    @property
    def mn1(self):
        return self.mat[-1, +0]

    @property
    def mnn(self):
        return self.mat[-1, -1]

    @property
    def m1x(self):
        return self.mat[+0, 1:-1]

    @property
    def mnx(self):
        return self.mat[-1, 1:-1]

    @property
    def mx1(self):
        return self.mat[1:-1, +0]

    @property
    def mxn(self):
        return self.mat[1:-1, -1]

    @property
    def mxx(self):
        return self.mat[1:-1, 1:-1]

    @property
    def v_1(self):
        return self.vec[+0]

    @property
    def v_x(self):
        return self.vec[1:-1]

    @property
    def v_n(self):
        return self.vec[-1]


class NodeOpr(OprData):
    """Local solution operator.
    """

    def feed(self, mat, vec):
        self.mat[:] = mat
        self.vec[:] = vec

    def solve(self):

        inv = np.linalg.solve(
            self.mxx, np.eye(self.mat.shape[0] - 2)
        )

        self.sol.q_1[:] = - inv @ self.mx1
        self.sol.q_2[:] = - inv @ self.mxn
        self.sol.vec[:] = + inv @ self.v_x

    def get_a11(self):
        return + self.m11 + self.m1x @ self.sol.q_1

    def get_a12(self):
        return + self.m1n + self.m1x @ self.sol.q_2

    def get_a21(self):
        return - self.mn1 - self.mnx @ self.sol.q_1

    def get_a22(self):
        return - self.mnn - self.mnx @ self.sol.q_2

    def get_b_1(self):
        return self.m1x @ self.sol.vec - self.v_1

    def get_b_2(self):
        return self.v_n - self.mnx @ self.sol.vec


class NodeSol:
    """Node solution.
    """

    def __init__(self, size):
        self.q_1 = np.zeros(size - 2)
        self.q_2 = np.zeros(size - 2)
        self.vec = np.zeros(size - 2)
