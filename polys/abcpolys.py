# -*- coding: utf-8 -*-
"""ABCs for polynomial bases.
"""
from abc import ABC, abstractmethod
import numpy as np

__all__ = [
    'PolyBasis', 'PolyOpr', 'NodeSet'
]


class PolyOpr(ABC):
    """ABC for operators on a polynomial sequence.
    """

    def __init__(self):
        self.nodes = None
        self.indices = None

    def with_nodes(self, nodes):
        """Defines the output points and returns the instance.

        Parameters
        ----------
        nodes : number | array-like
            Collocation point(s) within `[a,b]`.

        Returns
        -------
        self
            The instance itself.

        """
        self.nodes = nodes
        return self

    def with_polys(self, *indices):
        """Defines a polynomial sequence and returns the instance.

        Parameters
        ----------
        indices: *int
            Indices of the polynomials to include.

        Returns
        -------
        self
            The instance itself.

        """
        self.indices = indices
        return self

    def asdict(self) -> dict:
        """Realizes the operator as an index-to-output mapping.

        Returns
        -------
        dict
            Maps the indices of polynomials to the output values.

        """

        outputs = self.getoutputs(
            nodes=self.nodes, maxindex=max(self.indices)
        )

        return self.mapresults(outputs)

    def asmat(self):
        """Realizes the operator as a Vandermonde-like matrix.

        Returns
        -------
        ndarray
            The operator as a Vandermonde-like matrix (a).

        (a) Columns are images of the polynomials tabulated at the nodes.

        """
        asdict = self.asdict()
        return self.dict_to_mat(asdict)

    def dict_to_mat(self, mapping):

        data = list(
            mapping.values()
        )

        return np.array(data).T

    @abstractmethod
    def getoutputs(self, nodes, maxindex) -> list:
        pass

    def mapresults(self, outs):
        return {
            i: v for i, v in enumerate(outs) if i in self.indices
        }


class PolyBasis:
    """ABC for a polynomial basis.

    - Returns *operators* derived from `PolyOpr`.
    - Returns *node sets* derived from `NodeSet`.

    """

    @abstractmethod
    def polys(self):
        """Returns an *operator* that evaluates polynomials.
        """

    @abstractmethod
    def derivs(self, order=1):
        """Returns an *operator* that differentiates polynomials.

        Parameters
        ----------
        order : int = 1
            Order of the desired derivative starting from one.

        """

    @abstractmethod
    def integax(self, weighted=False):
        """Returns an *operator* that integrates polynomials over `[a,x]`.

        Parameters
        ----------
        weighted : bool = False
            Polynomials are multiplied by `x`, if True.

        """

    @abstractmethod
    def integxb(self, weighted=False):
        """Returns an *operator* that integrates polynomials over `[x,b]`.

        Parameters
        ----------
        weighted : bool = False
            Polynomials are multiplied by `x`, if True.

        """


class NodeSet(ABC):
    """Set of nodes associated with a polynomials basis.

    - Represents a set of distinct points in `[a,b]`.
    - May hold weights of the accompanying quadrature rule. 

    Attributes
    ----------
    nodes : ndarray
        Points as a flat numpy array.
    weights : ndarray | None
        Weights as a flat numpy array, if any.

    """

    def __init__(self):
        self.nodes = None
        self.weights = None

    def withcount(self, count):

        _nodes = self.find_nodes(count)
        _weights = self.find_weights(_nodes)

        self.nodes = _nodes
        self.weights = _weights

        return self

    @abstractmethod
    def find_nodes(self, number):
        pass

    @abstractmethod
    def find_weights(self, nodes):
        return None
