# -*- coding: utf-8 -*-
"""Tests HPS solution.
"""
import numpy as np
import unittest
from hpsolver import hps as hps


def setter(_):
    return np.array([[0., 0.], [1., 1.]])


def newroot():
    return hps.newpsn(-1, 1).add_nodes().add_nodes()


class TestSol(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        cls.ROOT = newroot().set_nodes(setter).make_dtn_leaf().make_opr()

        cls.ROOT.data.dtnopr.u_1[:] = 0.
        cls.ROOT.data.dtnopr.u_2[:] = 0.

        cls.ROOT = cls.ROOT.make_sol()
        cls.ROOT = cls.ROOT.make_sol_leaf()

    def test_sol_west(self):
        assert self.ROOT.west_node.west_node.data.dtnopr.u_1 == + 0.0
        assert self.ROOT.west_node.west_node.data.dtnopr.u_2 == - 0.375
        assert self.ROOT.west_node.east_node.data.dtnopr.u_1 == - 0.375
        assert self.ROOT.west_node.east_node.data.dtnopr.u_2 == - 0.5

    def test_sol_east(self):
        assert self.ROOT.east_node.west_node.data.dtnopr.u_1 == - 0.5
        assert self.ROOT.east_node.west_node.data.dtnopr.u_2 == - 0.375
        assert self.ROOT.east_node.east_node.data.dtnopr.u_1 == - 0.375
        assert self.ROOT.east_node.east_node.data.dtnopr.u_2 == + 0

    def test_sol_leafs(self):
        assert self.ROOT.west_node.west_node.data.body[0, 0] == + 0
        assert self.ROOT.west_node.west_node.data.body[0, 1] == - 0.375
        assert self.ROOT.west_node.east_node.data.body[0, 0] == - 0.375
        assert self.ROOT.west_node.east_node.data.body[0, 1] == - 0.5
        assert self.ROOT.east_node.west_node.data.body[0, 0] == - 0.5
        assert self.ROOT.east_node.west_node.data.body[0, 1] == - 0.375
        assert self.ROOT.east_node.east_node.data.body[0, 0] == - 0.375
        assert self.ROOT.east_node.east_node.data.body[0, 1] == + 0.0


if __name__ == '__main__':
    unittest.main()
