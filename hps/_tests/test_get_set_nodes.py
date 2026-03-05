# -*- coding: utf-8 -*-
"""Tests nodes get/set.
"""
import unittest
from hpsolver import hps as hps


def newroot():
    return hps.newgeom(-1, 1)


def export_data(node):
    return [
        node.data.x_1, node.data.x_2
    ]


def export_body(node):
    return node.data.body


class TestGetter(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        cls.ROOT = newroot().add_nodes()
        cls.DATA = cls.ROOT.get_nodes(postproc=export_data)

    def test_data(self):
        assert self.DATA[0] == [-1, +0]
        assert self.DATA[1] == [+0, +1]


class TestSetter(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        cls.ROOT = newroot().add_nodes()

        data = cls.ROOT.get_nodes(postproc=export_data)

        cls.ROOT = cls.ROOT.set_nodes(data)
        cls.DATA = cls.ROOT.get_nodes(postproc=export_body)

    def test_data(self):
        assert self.DATA[0] == [-1, +0]
        assert self.DATA[1] == [+0, +1]


if __name__ == '__main__':
    unittest.main()
