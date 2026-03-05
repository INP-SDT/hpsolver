# -*- coding: utf-8 -*-
"""DtN operators (scalar).
"""
import numpy as np


class OperatDtN:
    """DtN operator.
    """

    MAT_KEYS = [
        'a11', 'a12', 'a21', 'a22'
    ]

    def __init__(self, size):

        self.size = size

        self.mat = {
            k: np.zeros(size) for k in self.MAT_KEYS
        }

        self.b_1 = np.zeros(size)
        self.b_2 = np.zeros(size)

        self.u_1 = np.zeros(size)
        self.u_2 = np.zeros(size)

    @classmethod
    def from_size(cls, size):
        return cls(size)

    @property
    def a11(self):
        return self.mat['a11']

    @property
    def a12(self):
        return self.mat['a12']

    @property
    def a21(self):
        return self.mat['a21']

    @property
    def a22(self):
        return self.mat['a22']

    @a11.setter
    def a11(self, value):
        self.mat['a11'][:] = value

    @a12.setter
    def a12(self, value):
        self.mat['a12'][:] = value

    @a21.setter
    def a21(self, value):
        self.mat['a21'][:] = value

    @a22.setter
    def a22(self, value):
        self.mat['a22'][:] = value


class MergerDtN:
    """Merger of DtN operators. 

    Attributes
    ----------
    q_1 : vector
        1-st bridge matrix.
    q_2 : vector
        2-nd bridge matrix.
    q12 : vector
        Complement matrix.
    r12 : vector
        Bridge vector.
    u12 : vector
        Bridge solution.

    """

    def __init__(self, size):

        self.size = size

        self.q_1 = np.zeros(size)
        self.q_2 = np.zeros(size)
        self.q12 = np.zeros(size)

        self.r12 = np.zeros(size)
        self.u12 = np.zeros(size)

        self.cache = {}

    @property
    def west(self):
        return self.cache['west-dtn']

    @property
    def east(self):
        return self.cache['east-dtn']

    @property
    def head(self):
        return self.cache['head-dtn']

    def build_sol(self, head_dtn) -> None:
        """Builds the bridge solution.
        """

        u_1 = head_dtn.u_1
        u_2 = head_dtn.u_2

        self.u12 = self.q_1 * u_1 + self.q_2 * u_2 + self.r12

    def merge_dtns(self, west_dtn, east_dtn, head_dtn) -> None:
        """Merges DtN operators.
        """

        self.cache['head-dtn'] = head_dtn
        self.cache['west-dtn'] = west_dtn
        self.cache['east-dtn'] = east_dtn

        self.build_bridge()
        self.build_newdtn()

    def build_bridge(self):

        self.q12 = np.reciprocal(
            self.west.a22 - self.east.a11
        )

        self.q_1 = - self.q12 * self.west.a21
        self.q_2 = + self.q12 * self.east.a12

    def build_newdtn(self):

        self.build_newdtn_1()
        self.build_newdtn_2()

    def build_newdtn_1(self):

        self.head.a11 = self.west.a12 * self.q_1 + self.west.a11
        self.head.a12 = self.west.a12 * self.q_2

    def build_newdtn_2(self):

        self.head.a22 = self.east.a21 * self.q_2 + self.east.a22
        self.head.a21 = self.east.a21 * self.q_1

    def update_rhs(self, west_dtn, east_dtn, head_dtn) -> None:
        """Updates RHS of DtN operators.
        """

        self.cache['head-dtn'] = head_dtn
        self.cache['west-dtn'] = west_dtn
        self.cache['east-dtn'] = east_dtn

        self.update_bridge()
        self.update_newdtn()

    def update_bridge(self):
        self.r12 = self.q12 * (self.east.b_1 - self.west.b_2)

    def update_newdtn(self):

        self.update_newdtn_1()
        self.update_newdtn_2()

    def update_newdtn_1(self):
        self.head.b_1 = self.west.a12 * self.r12 + self.west.b_1

    def update_newdtn_2(self):
        self.head.b_2 = self.east.a21 * self.r12 + self.east.b_2
