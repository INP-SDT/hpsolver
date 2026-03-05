# -*- coding: utf-8 -*-
"""HPS operators.
"""
from abc import abstractmethod
from hpsolver.hps import bintrees
from hpsolver.hps import dtnoprs1
from hpsolver.hps import dtnoprs2

DTNOPRS = {
    1: dtnoprs1,
    2: dtnoprs2
}


class HPSData(bintrees.NodeData):
    """ABC for HPS-Data.

    Attributes
    ----------
    body : matrix-like
        Raw data on the HPS node.

    Properties
    ----------

    Name       | Description
    -----------|--------------------------------------
    `x12`      | Interval as a tuple.
    `d_x`      | Width of the interval.
    `u_1`      | West value of the solition.
    `u_2`      | East value of the solition.

    """

    SIZE = 0
    MODE = 1

    def __init__(self, x_1, x_2, body=None):

        self.x_1 = x_1
        self.x_2 = x_2

        self.dtnopr = DTNOPRS[self.MODE].OperatDtN(self.SIZE)
        self.merger = DTNOPRS[self.MODE].MergerDtN(self.SIZE)

        self.body = body
        self.cache = {}

    @property
    def x12(self):
        return [self.x_1, self.x_2]

    @property
    def x_0(self):
        return 0.5 * (
            self.x_1 + self.x_2
        )

    @property
    def d_x(self):
        return self.x_2 - self.x_1

    @property
    def u_1(self):
        return self.dtnopr.u_1

    @property
    def u_2(self):
        return self.dtnopr.u_2

    def from_data(self, data):
        self.body = data

    def from_func(self, func):
        self.body = func(self)

    def new_data_west(self):

        x_1 = self.x_1
        x_2 = self.x_0

        return type(self)(
            x_1, x_2, self.new_body_west()
        )

    def new_data_east(self):

        x_1 = self.x_0
        x_2 = self.x_2

        return type(self)(
            x_1, x_2, self.new_body_east()
        )

    def collect_data(self, west_data, east_data):

        x_1 = west_data.x_1
        x_2 = east_data.x_2

        return type(self)(
            x_1, x_2, self.new_body_join(west_data, east_data)
        )

    @abstractmethod
    def new_body_west(self):
        """Creates the new body for the west children.

        Returns
        -------
        matrix-like
            New body of the west children.

        """

    @abstractmethod
    def new_body_east(self):
        """Creates the new body for the east children.

        Returns
        -------
        matrix-like
            New body of the east children.

        """

    @abstractmethod
    def new_body_join(self, west_data, east_data):
        """Creates the new body from the children data.

        Returns
        -------
        matrix-like
            New body merged from the children data.

        """

    def make_dtn(self):
        self.make_dtn_mat()
        self.make_dtn_vec()

    def make_dtn_mat(self):

        mat = self.mat_from_body()

        self.dtnopr.a11 = mat['a11'].copy()
        self.dtnopr.a12 = mat['a12'].copy()
        self.dtnopr.a21 = mat['a21'].copy()
        self.dtnopr.a22 = mat['a22'].copy()

    def make_dtn_vec(self):

        vec = self.vec_from_body()

        self.dtnopr.b_1 = vec['b_1'].copy()
        self.dtnopr.b_2 = vec['b_2'].copy()

    @abstractmethod
    def mat_from_body(self) -> dict:
        """Makes the DtN matrix from a body.

        Returns
        -------
        dict
            Matrix entries as arrays.

        Notes
        -----

        Keys must be `a11`, `a12`, `a21`, `a22`.

        """

    @abstractmethod
    def vec_from_body(self) -> dict:
        """Makes the DtN vector from a body.

        Returns
        -------
        dict
            Vector entries as arrays.

        Notes
        -----

        Keys must be `b_1`, `b_2`.

        """

    @abstractmethod
    def make_sol(self) -> None:
        """Transfer the solution from the DtN operator to the body.

        Notes
        -----

        Transfers `u_1` and `u_2` to the body.

        """
