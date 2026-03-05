# -*- coding: utf-8 -*-
"""Tests nodes add/del.
"""
import unittest
from hpsolver import hps as hps


def newroot():
    return hps.newgeom(-1, 1)


def mask(node):
    if node.data.x_0 <= 0.0:
        return True
    return False


class TestAddUnmasked(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.ROOT = newroot().add_nodes()

    def test_nodes(self):

        assert self.ROOT.data.x_1 == - 1
        assert self.ROOT.data.x_2 == + 1

        assert self.ROOT.west_node.data.x_1 == - 1
        assert self.ROOT.west_node.data.x_2 == + 0

        assert self.ROOT.east_node.data.x_1 == + 0
        assert self.ROOT.east_node.data.x_2 == + 1


class TestAddMasked(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.ROOT = newroot().add_nodes(mask).add_nodes(mask)

    def test_nodes(self):

        assert self.ROOT.west_node.west_node.data.x_1 == - 1.0
        assert self.ROOT.west_node.west_node.data.x_2 == - 0.5

        assert self.ROOT.west_node.east_node.data.x_1 == - 0.5
        assert self.ROOT.west_node.east_node.data.x_2 == - 0.0

        assert self.ROOT.east_node.west_node is None
        assert self.ROOT.east_node.east_node is None


class TestDelUnmasked(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.ROOT = newroot().add_nodes().add_nodes().del_nodes()

    def test_nodes(self):

        assert self.ROOT.west_node.is_leaf() is True
        assert self.ROOT.east_node.is_leaf() is True

        assert self.ROOT.data.x_1 == - 1
        assert self.ROOT.data.x_2 == + 1


class TestDelMasked(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.ROOT = newroot().add_nodes(mask).add_nodes(mask).del_nodes(mask)

    def test_nodes(self):
        assert self.ROOT.west_node.is_leaf() is True
        assert self.ROOT.east_node.is_leaf() is True


if __name__ == '__main__':
    unittest.main()
