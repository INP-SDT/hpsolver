# -*- coding: utf-8 -*-
"""Gauss-Lobatto nodes.
"""
import numpy as np
from hpsolver.polys.abcpolys import NodeSet


class LobattoNodes(NodeSet):
    """Set of Gauss-Lobatto nodes in [-1, 1].
    """

    def find_nodes(self, number):
        return np.array(NODES[number])

    def find_weights(self, nodes):
        return np.array(
            WEIGHTS[len(nodes)]
        )


NODES3 = [
    -1., 0., +1.
]

WEIGHTS3 = [
    1./3., 4./3., 1./3.
]

NODES4 = [
    - 1.,
    - 1./np.sqrt(5.),
    + 1./np.sqrt(5.),
    + 1
]

WEIGHTS4 = [
    1./6.,
    5./6.,
    5./6.,
    1./6.
]

NODES5 = [
    - 1.,
    - 0.6546536707079771,
    + 0.,
    + 0.6546536707079771,
    + 1.
]

WEIGHTS5 = [
    1./10.,
    49./90.,
    32./45.,
    49./90.,
    1./10.
]

NODES6 = [
    - 1.,
    - 0.7650553239294647,
    - 0.2852315164806451,
    + 0.2852315164806451,
    + 0.7650553239294647,
    + 1.
]

WEIGHTS6 = [
    1./15.,
    (14. - np.sqrt(7.)) / 30.,
    (14. + np.sqrt(7.)) / 30.,
    (14. + np.sqrt(7.)) / 30.,
    (14. - np.sqrt(7.)) / 30.,
    1./15.
]

NODES7 = [
    - 1.,
    - 0.8302238962785669,
    - 0.4688487934707142,
    + 0.0,
    + 0.4688487934707142,
    + 0.8302238962785669,
    + 1.
]

WEIGHTS7 = [
    0.0476190476190476,
    0.2768260473615659,
    0.4317453812098626,
    0.4876190476190476,
    0.4317453812098626,
    0.2768260473615659,
    0.0476190476190476
]

NODES = {
    3: NODES3,
    4: NODES4,
    5: NODES5,
    6: NODES6,
    7: NODES7
}

WEIGHTS = {
    3: WEIGHTS3,
    4: WEIGHTS4,
    5: WEIGHTS5,
    6: WEIGHTS6,
    7: WEIGHTS7
}
