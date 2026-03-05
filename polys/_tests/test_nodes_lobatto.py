# -*- coding: utf-8 -*-
"""Test the Lobatto nodes.
"""
import unittest
import numpy as np
from hpsolver import polys


def _test_integ(quad):
    return np.sum(
        quad.weights * (quad.nodes ** 4)
    )


class TestLobatto:

    QUAD = None

    def test_weights_sum(self):
        assert np.round(np.sum(self.QUAD.weights), 14) == 2

    def test_quadrature(self):
        assert np.round(_test_integ(self.QUAD), 14) == 0.4


class TestLobatto4(TestLobatto, unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.QUAD = polys.lbtgauss(4)


class TestLobatto5(TestLobatto, unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.QUAD = polys.lbtgauss(5)


class TestLobatto6(TestLobatto, unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.QUAD = polys.lbtgauss(6)


class TestLobatto7(TestLobatto, unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.QUAD = polys.lbtgauss(7)


if __name__ == '__main__':
    unittest.main()
