# -*- coding: utf-8 -*-
"""HPS root.
"""
import numpy as np
from hpsolver import hps
from hpsolver.sem import hpsdata
from hpsolver.sem import specunit


def newroot(x_1, x_2):
    """Creates new HPS root.

    Parameters
    ----------
    x_1 : float
        West endpoint of the interval.
    x_2 : float
        East endpoint of the interval.

    Returns
    -------
    HPSNode
        Root of the HPS tree.

    """
    return newroot_from_data(
        hpsdata.HPSData(x_1, x_2)
    )


def newroot_from_data(data):
    return HPSRoot.from_rank(0).with_data(data)


class HPSRoot(hps.HPSNode):
    """Root of the HPS tree.

    Properties
    ----------

    Name   | Decription
    -------|--------------------------------------
    `u_1`  | Solution value at the west endpoint.
    `u_2`  | Solution value at the east endpoint.

    """

    @property
    def u_1(self):
        return self.data.dtnopr.u_1

    @property
    def u_2(self):
        return self.data.dtnopr.u_2

    @u_1.setter
    def u_1(self, value):
        self.data.dtnopr.u_1[:] = value

    @u_2.setter
    def u_2(self, value):
        self.data.dtnopr.u_2[:] = value

    @property
    def unit(self):
        return self.data.cache['unit']

    def reset(self):
        """Deactivates the tree after computation.
        """
        self.run_nodes('reset')
        self.data.cache = {}

    def activate(self, order) -> None:
        """Activates the tree for computation.

        Parameters
        ----------
        order : int
            Order of the scheme (2-6).

        """

        self.run_nodes(
            'activate', order
        )

        self.data.cache['unit'] = specunit.getunit(order + 1)

    def setcoeffs(self, data):
        """Defines the equation coefficients.

        Parameters
        ----------
        data : dict
            Provides equation coefficients as lists.

        """

        data = {
            k: self.stack(v) for k, v in data.items()
        }

        self.run_nodes(
            'setcoeffs', data
        )

    def build_operator(self) -> None:
        """Builds the solution operator.
        """
        self.run_nodes('solve')
        self.make_dtn_leaf()
        self.make_opr()

    def build_solution(self) -> None:
        """Builds the solution after boundary conditions are applied.
        """
        self.make_sol()
        self.make_sol_leaf()

    def dtn_mat(self):
        """Returns the matrix of the DtN operator.
        """

        a11 = self.data.dtnopr.a11[0]
        a12 = self.data.dtnopr.a12[0]
        a21 = self.data.dtnopr.a21[0]
        a22 = self.data.dtnopr.a22[0]

        return np.array(
            [[a11, a12], [a21, a22]]
        )

    def dtn_vec(self):
        """Returns the vector of the DtN operator.
        """

        b_1 = self.data.dtnopr.b_1[0]
        b_2 = self.data.dtnopr.b_2[0]

        return np.array([b_1, b_2])

    def vmesh(self):
        """Retrieves mesh elements and stacks them vertically.

        Parameters
        ----------
        root : HPSNode
            Root of the HPS tree.

        Returns
        -------
        2d-array
            Mesh as a vertical stack of elements.

        """
        return np.vstack(
            [node.data.get_points() for node in self.get_nodes()]
        )

    def hmesh(self):
        """Retrieves mesh elements and stacks them horizontally.

        Parameters
        ----------
        root : HPSNode
            Root of the HPS tree.

        Returns
        -------
        flat-array
            Mesh as a horizontal stack of elements.

        """
        return np.hstack(
            [node.data.get_points() for node in self.get_nodes()]
        )

    def vdata(self):
        """Retrieves data from elements and stacks them vertically.

        Parameters
        ----------
        root : HPSNode
            Root of the HPS tree.

        Returns
        -------
        2d-array
            Data from elements stacked vertically.

        """
        return np.vstack(
            [node.data.body for node in self.get_nodes()]
        )

    def hdata(self):
        """Retrieves data from elements and stacks them horizontally.

        Parameters
        ----------
        root : HPSNode
            Root of the HPS tree.

        Returns
        -------
        flat-array
            Data from elements stacked horizontally.

        """
        return np.hstack(
            [node.data.body for node in self.get_nodes()]
        )

    def vgrad(self):
        """Retrieves gradient from elements and stacks it vertically.

        Parameters
        ----------
        root : HPSNode
            Root of the HPS tree.

        Returns
        -------
        2d-array
            Gradient from elements stacked vertically.

        """
        return np.vstack(
            [node.data.get_grad() for node in self.get_nodes()]
        )

    def hgrad(self):
        """Retrieves data from elements and stacks it horizontally.

        Parameters
        ----------
        root : HPSNode
            Root of the HPS tree.

        Returns
        -------
        flat-array
            Gradient from elements stacked horizontally.

        """
        return np.hstack(
            [node.data.get_grad() for node in self.get_nodes()]
        )

    def stack(self, data):
        return list(
            reversed(data)
        )
