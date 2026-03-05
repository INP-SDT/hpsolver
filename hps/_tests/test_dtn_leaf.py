# -*- coding: utf-8 -*-
"""Tests DtN on leaf nodes.
"""
import numpy as np
import unittest
from hpsolver import hps as hps


def setter(_):
    return np.array([[0., 0.], [1., 1.]])


def newroot():
    return hps.newpsn(-1, 1).add_nodes().set_nodes(setter)


def test_dtn_mat(dtn):
    assert dtn.a11 == - 1.
    assert dtn.a12 == + 1.
    assert dtn.a21 == - 1.
    assert dtn.a22 == + 1.


def test_dtn_vec(dtn):
    assert dtn.b_1 == - 0.5
    assert dtn.b_2 == + 0.5


class TestDtN(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.ROOT = newroot().make_dtn_leaf()

    def test_dtn_mat(self):
        test_dtn_mat(self.ROOT.west_node.data.dtnopr)
        test_dtn_mat(self.ROOT.east_node.data.dtnopr)

    def test_dtn_vec(self):
        test_dtn_vec(self.ROOT.west_node.data.dtnopr)
        test_dtn_vec(self.ROOT.east_node.data.dtnopr)


class TestMat(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.ROOT = newroot().make_mat_leaf()

    def test_dtn_mat(self):
        test_dtn_mat(self.ROOT.west_node.data.dtnopr)
        test_dtn_mat(self.ROOT.east_node.data.dtnopr)


class TestVec(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.ROOT = newroot().make_vec_leaf()

    def test_dtn_mat(self):
        test_dtn_vec(self.ROOT.west_node.data.dtnopr)
        test_dtn_vec(self.ROOT.east_node.data.dtnopr)


if __name__ == '__main__':
    unittest.main()
