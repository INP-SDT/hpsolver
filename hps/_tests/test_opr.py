# -*- coding: utf-8 -*-
"""Tests HPS operator.
"""
import numpy as np
import unittest
from hpsolver import hps as hps


def setter(_):
    return np.array([[0., 0.], [1., 1.]])


def newroot():
    return hps.newpsn(-1, 1).add_nodes().set_nodes(setter)


def test_opr_mat(dtn):
    assert dtn.a11 == - 0.5
    assert dtn.a12 == + 0.5
    assert dtn.a21 == - 0.5
    assert dtn.a22 == + 0.5


def test_opr_vec(dtn):
    assert dtn.b_1 == - 1.
    assert dtn.b_2 == + 1.


class TestOpr(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.ROOT = newroot().make_dtn_leaf().make_opr()

    def test_opr_mat(self):
        test_opr_mat(self.ROOT.data.dtnopr)

    def test_opr_vec(self):
        test_opr_vec(self.ROOT.data.dtnopr)

    def test_opr_merger(self):
        assert self.ROOT.data.merger.q_1 == + 0.5
        assert self.ROOT.data.merger.q_2 == + 0.5
        assert self.ROOT.data.merger.r12 == - 0.5


class TestMat(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.ROOT = newroot().make_dtn_leaf().make_opr_mat()

    def test_opr_mat(self):
        test_opr_mat(self.ROOT.data.dtnopr)

    def test_opr_merger(self):
        assert self.ROOT.data.merger.q_1 == + 0.5
        assert self.ROOT.data.merger.q_2 == + 0.5
        assert self.ROOT.data.merger.r12 == + 0.0


class TestVec(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.ROOT = newroot().make_dtn_leaf().make_opr_mat().make_opr_vec()

    def test_opr_mat(self):
        test_opr_mat(self.ROOT.data.dtnopr)

    def test_opr_vec(self):
        test_opr_vec(self.ROOT.data.dtnopr)

    def test_opr_merger(self):
        assert self.ROOT.data.merger.q_1 == + 0.5
        assert self.ROOT.data.merger.q_2 == + 0.5
        assert self.ROOT.data.merger.r12 == - 0.5


if __name__ == '__main__':
    unittest.main()
