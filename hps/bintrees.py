# -*- coding: utf-8 -*-
"""Binary trees.
"""
from abc import ABC, abstractmethod
from operator import methodcaller


def add_nodes(root, mask=None):
    """Adds nodes to the tree.

    Parameters
    ----------
    root : node-like
        Root of the tree.
    mask : Callable = None
        Boolean mask applied to nodes (a).

    Notes
    -----

    (a) By default, all leaf nodes are expanded.

    """
    return UTraverser.from_visit(NodesAdder(mask)).run(root)


def del_nodes(root, mask=None):
    """Deletes nodes from the tree.

    Parameters
    ----------
    root : node-like
        Root of the tree.
    mask : Callable = None
        Boolean mask applied to nodes (a).

    Notes
    -----

    (a) By default, all leaf nodes are removed.

    """
    return DTraverser.from_visit(NodesDeler(mask)).run(root)


def get_nodes(root, mask=None):
    """Fetches nodes from the tree.

    Parameters
    ----------
    root : node-like
        Root of the tree.
    mask : Callable = None
        Boolean mask applied to nodes (a).

    Returns
    -------
    list
        Fetched nodes.

    Notes
    -----

    (a) By default, leaf nodes are fetched.

    """
    return list(
        filter(
            bool, DTraverser.from_visit(NodesGetter(mask)).run(root)
        )
    )


def set_nodes(root, bank):
    """Sets data of the leaf nodes.

    Parameters
    ----------
    root : node-like
        Root of the tree.
    bank : Callable | Iterable
        Data bank as a function or stack.

    """
    return DTraverser.from_visit(NodesSetter(bank)).run(root)


def run_leafs(root, method_name, *args, **kwargs):
    """Runs a method on the data of the leaf nodes.
    """

    visit = LeafsRunner(
        method_name, *args, **kwargs
    )

    return DTraverser.from_visit(visit).run(root)


def run_nodes_up(root, func):
    """Runs a function on the inner nodes in up-traversal.
    """
    return UTraverser.from_visit(NodesRunner(func)).run(root)


def run_nodes_down(root, func):
    """Runs a function on the inner nodes in down-traversal.
    """
    return DTraverser.from_visit(NodesRunner(func)).run(root)


class Node:
    """Basic tree node.
    """

    def __init__(self, rank):

        self.rank = rank
        self.data = None

        self.west_node = None
        self.east_node = None

    @classmethod
    def from_rank(cls, rank):
        return cls(rank)

    def with_data(self, data):
        self.data = data
        return self

    def next_node(self):
        return self.from_rank(self.rank + 1)

    def is_leaf(self):
        if self.west_node is None and self.east_node is None:
            return True
        return False

    def is_leaf_parent(self):

        if self.is_leaf():
            return False

        west = self.west_node.is_leaf()
        east = self.east_node.is_leaf()

        if west is True and east is True:
            return True
        return False


class NodeData(ABC):
    """ABC for node data.
    """

    @abstractmethod
    def new_data_west(self):
        """Creates new west data when adding nodes.
        """

    @abstractmethod
    def new_data_east(self):
        """Creates new east data when adding nodes.
        """

    @abstractmethod
    def collect_data(self, west_data, east_data):
        """Collects children data when removing nodes.
        """

    @abstractmethod
    def from_data(self, data):
        """Defines data from a data bank.
        """

    @abstractmethod
    def from_func(self, func):
        """Defines data from a function.
        """


class Traverser:
    """Base tree traverser.
    """

    def __init__(self, visit=None):
        self.visit = visit
        self.cache = []

    @classmethod
    def from_visit(cls, visit):
        return cls(visit)

    def run(self, root):

        self.cache.clear()
        self.traverse(root)

        output = self.cache.copy()

        self.cache.clear()
        return output

    def traverse(self, node):
        return node


class DTraverser(Traverser):
    """Downward tree traverser (pre-order). 
    """

    def traverse(self, node):

        if node is None:
            return

        self.cache.append(
            self.visit(node)
        )

        self.traverse(node.west_node)
        self.traverse(node.east_node)


class UTraverser(Traverser):
    """Upward tree traverser (post-order). 
    """

    def traverse(self, node):

        if node is None:
            return

        self.traverse(node.west_node)
        self.traverse(node.east_node)

        self.cache.append(
            self.visit(node)
        )


class NodesAdder:
    """Adds tree nodes.
    """

    def __init__(self, mask=None):
        self.mask = mask

    def __call__(self, node):

        if not node.is_leaf():
            return None

        if self.mask is None:
            return self.add_nodes(node)

        if self.mask(node) is True:
            return self.add_nodes(node)

        return None

    def add_nodes(self, node):

        west_data = node.data.new_data_west()
        east_data = node.data.new_data_east()

        node.west_node = node.next_node().with_data(west_data)
        node.east_node = node.next_node().with_data(east_data)

        node.data.body = None


class NodesDeler:
    """Removes tree nodes.
    """

    def __init__(self, mask=None):
        self.mask = mask

    def __call__(self, node):

        if not node.is_leaf_parent():
            return False

        if self.mask is None:
            return self.del_nodes(node)
        if self.mask(node) is True:
            return self.del_nodes(node)

        return False

    def del_nodes(self, node):

        west_data = node.west_node.data
        east_data = node.east_node.data

        node = node.with_data(
            node.data.collect_data(west_data, east_data)
        )

        del node.west_node
        del node.east_node

        node.west_node = None
        node.east_node = None

        return True


class NodesGetter:
    """Gets nodes.
    """

    def __init__(self, mask=None):
        self.mask = mask

    def __call__(self, node):

        if self.mask is not None:
            if self.mask(node) is True:
                return node
            return None

        if node.is_leaf():
            return node
        return None


class NodesSetter:
    """Sets data on the leaf nodes.
    """

    def __init__(self, bank):
        self.bank = self.set_bank(bank)

    def set_bank(self, bank):
        if callable(bank):
            return bank
        return list(
            reversed(bank)
        )

    def __call__(self, node):

        if node.is_leaf() is False:
            return None

        if callable(self.bank):
            node.data.from_func(self.bank)
            return None

        node.data.from_data(self.bank.pop())
        return None


class LeafsRunner:
    """Runs a method on the data of leaf nodes.
    """

    def __init__(self, method_name, *args, **kwargs):

        self.caller = methodcaller(
            method_name, *args, **kwargs
        )

    def __call__(self, node):
        if node.is_leaf() is False:
            return None
        return self.caller(node.data)


class NodesRunner:
    """Runs a function on the inner nodes.
    """

    def __init__(self, func):
        self.func = func

    def __call__(self, node):

        if node.is_leaf() is True:
            return None

        return self.func(
            node, node.west_node, node.east_node
        )
