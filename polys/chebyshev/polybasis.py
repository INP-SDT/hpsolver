# -*- coding: utf-8 -*-
"""Public Chebyshev class.
"""
import numpy as np
from hpsolver.polys.abcpolys import PolyBasis, NodeSet
from hpsolver.polys.chebyshev import funcsderivs
from hpsolver.polys.chebyshev import integrators


class Chebyshev(PolyBasis):
    """Basis formed by the Chebyshev polynomials of the 1st kind.
    """

    def polys(self):
        return funcsderivs.Polys()

    def derivs(self, order):
        if order == 1:
            return funcsderivs.Derivs()
        raise NotImplementedError(
            'currently not implemented for Chebyshev'
        )

    def integax(self, weighted=False):
        if not weighted:
            return integrators.IntegT0TnAX()
        return integrators.IntegT1TnAX()

    def integxb(self, weighted=False):
        if not weighted:
            return integrators.IntegT0TnXB()
        return integrators.IntegT1TnXB()


class ChebLobatto(NodeSet):
    """Set of Chebyshev-Lobatto nodes in [-1, 1].
    """

    def find_nodes(self, number):
        return np.cos(
            np.pi * np.arange(number - 1, -1, -1) / (number - 1)
        )

    def find_weights(self, _):
        return None


class ChebGauss(NodeSet):
    """Set of Chebyshev-Gauss nodes in [-1, 1].
    """

    def find_nodes(self, number):
        return np.cos(
            np.pi * (np.flip(np.arange(number)) + 0.5) / number
        )

    def find_weights(self, _):
        return None


def chblobatto(count=None):
    """Returns the Chebyshev-Lobatto nodes.

    Parameters
    ----------
    count : int = None
        Number of quadrature points.

    Returns
    -------
    NodeSet
        The resulting node set.

    """

    nodes = ChebLobatto()

    if count is None:
        return nodes
    return nodes.withcount(count)


def chbgauss(count=None):
    """Returns the Chebyshev-Gauss nodes.

    Parameters
    ----------
    count : int = None
        Number of quadrature points.

    Returns
    -------
    NodeSet
        The resulting node set.

    """

    nodes = ChebGauss()

    if count is None:
        return nodes
    return nodes.withcount(count)
