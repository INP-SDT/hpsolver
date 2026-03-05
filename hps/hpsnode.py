# -*- coding: utf-8 -*-
"""1D HPS node.
"""
from hpsolver.hps import bintrees
from hpsolver.hps import hpsgeom
from hpsolver.hps import hpspsn


def newgeom(x_1, x_2):
    """Creates a new HPS node with HPS-Geometry data.

    Parameters
    ----------
    x_1 : float
        West endpoint of the interval.
    x_2 : float
        East endpoint of the interval.

    Returns
    -------
    HPSNode
        HPS node with HPS-Geometry data.

    """
    return HPSNode.from_rank(0).with_data(hpsgeom.HPSGeom(x_1, x_2))


def newpsn(x_1, x_2):
    """Creates a new HPS node with HPS-Poisson data.

    Parameters
    ----------
    x_1 : float
        West endpoint of the interval.
    x_2 : float
        East endpoint of the interval.

    Returns
    -------
    HPSNode
        HPS node with HPS-Poisson data.

    """
    return HPSNode.from_rank(0).with_data(hpspsn.HPSPoisson(x_1, x_2))


class HPSNode(bintrees.Node):
    """1D HPS node.
    """

    def add_nodes(self, mask=None):
        """Adds nodes to the unit.

        Parameters
        ----------
        mask : Callable = None
            Boolean predicate that selects the nodes to expand (a).

        Returns
        -------
        self
            Node itself.

        Notes
        -----

        (a) By default, all leaf nodes are expanded.

        """
        _ = bintrees.add_nodes(self, mask)
        return self

    def del_nodes(self, mask=None):
        """Removes nodes from the unit.

        Parameters
        ----------
        mask : Callable = None
            Boolean predicate that selects the nodes to delete (a).

        Returns
        -------
        self
            Node itself.

        Notes
        -----

        (a) By default, all leaf nodes are deleted.

        """
        _ = bintrees.del_nodes(self, mask)
        return self

    def get_nodes(self, postproc=None):
        """Fetches leaf nodes from the unit.

        Parameters
        ----------
        postproc : Callable = None
            Post-processor of the nodes.

        Returns
        -------
        list
            Fetched nodes.

        """

        nodes = bintrees.get_nodes(self, mask=None)

        if postproc is None:
            return nodes

        return [
            postproc(node) for node in nodes
        ]

    def set_nodes(self, bank):
        """Sets data on the leaf nodes.

        Parameters
        ----------
        bank : Callable | Iterable
            Data on leaf nodes as a function or stack.

        Returns
        -------
        self
            Node itself.

        """
        _ = bintrees.set_nodes(self, bank)
        return self

    def run_nodes(self, method_name, *args, **kwargs):
        """Runs a method on the data of leaf nodes.

        Parameters
        ----------
        method_name : str
            Name of the method.
        args : tuple
            Positional arguments of the method.
        kwargs : dict
            Keyword arguments of the method.

        Returns
        -------
        self
            Node itself.

        """

        _ = bintrees.run_leafs(
            self, method_name, *args, **kwargs
        )

        return self

    def get_tree(self) -> list:
        """Returns all nodes of the tree as a list.
        """
        return bintrees.get_nodes(self, lambda _: True)

    def make_sol(self):
        """Computes the global solution.
        """
        _ = bintrees.run_nodes_down(self, build_sol)
        return self

    def make_opr(self):
        """Builds the global solution operator.
        """
        _ = bintrees.run_nodes_up(self, build_dtns)
        return self

    def make_opr_mat(self):
        _ = bintrees.run_nodes_up(self, merge_dtns)
        return self

    def make_opr_vec(self):
        _ = bintrees.run_nodes_up(self, update_rhs)
        return self

    def make_dtn_leaf(self):
        """Builds the DtN operators on leaf nodes.
        """
        _ = bintrees.run_leafs(self, 'make_dtn')
        return self

    def make_mat_leaf(self):
        _ = bintrees.run_leafs(self, 'make_dtn_mat')
        return self

    def make_vec_leaf(self):
        _ = bintrees.run_leafs(self, 'make_dtn_vec')
        return self

    def make_sol_leaf(self):
        """Builds the solution on leaf nodes.
        """
        _ = bintrees.run_leafs(self, 'make_sol')
        return self


def build_sol(head, west, east):
    """Builds the solution on children nodes.
    """

    head.data.merger.build_sol(head.data.dtnopr)

    west.data.dtnopr.u_1[:] = head.data.dtnopr.u_1[:]
    east.data.dtnopr.u_2[:] = head.data.dtnopr.u_2[:]

    west.data.dtnopr.u_2[:] = head.data.merger.u12.copy()
    east.data.dtnopr.u_1[:] = head.data.merger.u12.copy()


def build_dtns(head, west, east):
    """Builds DtN operators on the inner nodes.
    """

    merge_dtns(head, west, east)
    update_rhs(head, west, east)


def merge_dtns(head, west, east):
    """Merges DtN operators on the inner nodes.
    """

    head.data.merger.merge_dtns(
        west.data.dtnopr, east.data.dtnopr, head.data.dtnopr
    )


def update_rhs(head, west, east):
    """Updates RHS on the inner nodes.
    """

    head.data.merger.update_rhs(
        west.data.dtnopr, east.data.dtnopr, head.data.dtnopr
    )
