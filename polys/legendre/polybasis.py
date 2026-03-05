# -*- coding: utf-8 -*-
"""Public Legendre class.
"""
from hpsolver.polys.abcpolys import PolyBasis
from hpsolver.polys.legendre import funcsderivs
from hpsolver.polys.legendre import integrators
from hpsolver.polys.legendre import gaussnodes
from hpsolver.polys.legendre import lbtnodes


class Legendre(PolyBasis):
    """Basis formed by the Legendre polynomials.
    """

    def polys(self):
        return funcsderivs.Polys()

    def derivs(self, order=1):
        return funcsderivs.Derivs(order)

    def integax(self, weighted=False):
        if not weighted:
            return integrators.IntegP0PmAX()
        return integrators.IntegP1PmAX()

    def integxb(self, weighted=False):
        if not weighted:
            return integrators.IntegP0PmXB()
        return integrators.IntegP1PmXB()


def lgngauss(count=None):
    """Returns the Legendre-Gauss node set.

    Parameters
    ----------
    count : int = None
        Number of quadrature points.

    Returns
    -------
    NodeSet
        The resulting node set.

    """

    if count is None:
        return gaussnodes.GaussNodes()

    return gaussnodes.GaussNodes().withcount(count)


def lbtgauss(count):
    """Returns the Lobatto-Gauss node set.

    Parameters
    ----------
    count : int
        Number of quadrature points (3 - 7).

    Returns
    -------
    NodeSet
        The resulting node set.

    """

    if count not in [3, 4, 5, 6, 7]:
        raise NotImplementedError(
            f'Lobatto quadrature with {count} nodes is not implemented'
        )

    return lbtnodes.LobattoNodes().withcount(count)
