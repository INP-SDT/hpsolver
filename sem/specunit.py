# -*- coding: utf-8 -*-
"""Spectral computing unit.
"""
import numpy as np
from hpsolver import polys


def getunit(order):
    """Creates a spectral computing unit.

    Parameters
    ----------
    order : int
        Number of computing nodes.

    """
    return SpecUnit.from_order(order)


class SpecUnit:
    """Spectral computing unit.
    """

    def __init__(self, **kwargs):

        self.diffmat = kwargs['diffmat']
        self.specmat = kwargs['specmat']
        self.splitmats = kwargs['splitmats']
        self.joinmats = kwargs['joinmats']
        self.weights = kwargs['weights']
        self.points = kwargs['points']

    @classmethod
    def from_order(cls, order):
        return UnitMaker.from_order(order).get_unit()

    def differ(self, bvec):
        return (self.diffmat.T * (self.weights * bvec)) @ self.diffmat

    def conver(self, avec):
        return self.diffmat.T * (self.weights * avec)

    def masser(self, cvec):
        return np.diag(
            cvec * self.weights
        )

    def source(self, dvec):
        return dvec * self.weights

    def grad(self, data):
        return self.diffmat @ data


class UnitMaker:
    """Makes a spectral computing unit.
    """

    def __init__(self, order):
        self.order = order
        self.nodes = None

    @classmethod
    def from_order(cls, order):
        return cls(order)

    def get_unit(self):

        dat = self.make_data()
        obj = self.from_data(dat)

        return obj

    def from_data(self, data):
        return SpecUnit(**data)

    def make_data(self):

        nodes = self.get_nodes()
        diffmat = self.get_diffmat(nodes)
        specmat = self.get_specmat(nodes)
        splitmats = self.get_splitmats(nodes)
        joinmats = self.get_joinmats(nodes)

        return {
            'diffmat': diffmat,
            'specmat': specmat,
            'splitmats': splitmats,
            'joinmats': joinmats,
            'weights': nodes.weights,
            'points': nodes.nodes
        }

    def get_nodes(self):
        return get_nodeset(self.order)

    def get_diffmat(self, nodes):

        van0 = get_vander_0(
            self.order, nodes.nodes
        )

        van1 = get_vander_1(
            self.order, nodes.nodes
        )

        return van1 @ np.linalg.solve(van0, np.eye(self.order))

    def get_specmat(self, nodes):

        van0 = get_vander_0(
            self.order, nodes.nodes
        )

        return np.linalg.solve(
            van0, np.eye(self.order)
        )

    def get_splitmats(self, nodes):

        van0 = get_vander_0(
            self.order, nodes.nodes
        )

        smat = np.linalg.solve(
            van0, np.eye(self.order)
        )

        van1 = get_vander_0(
            self.order, 0.5 * nodes.nodes - 0.5
        )

        van2 = get_vander_0(
            self.order, 0.5 * nodes.nodes + 0.5
        )

        return [
            van1 @ smat,
            van2 @ smat
        ]

    def get_joinmats(self, nodes):

        mat1, mat2 = self.get_splitmats(nodes)

        mass_mat = nodes.weights
        mass_inv = 1.0 / nodes.weights[..., None]

        mat1 = 0.5 * mass_inv * (mat1.T * mass_mat)
        mat2 = 0.5 * mass_inv * (mat2.T * mass_mat)

        return [mat1, mat2]


def get_nodeset(order):
    return polys.lbtgauss(order)


def get_vander_0(order, points):

    van = polys.Legendre().polys()

    van = van.with_polys(*range(order))
    van = van.with_nodes(points)

    return van.asmat()


def get_vander_1(order, points):

    van = polys.Legendre().derivs()

    van = van.with_polys(*range(order))
    van = van.with_nodes(points)

    return van.asmat()
