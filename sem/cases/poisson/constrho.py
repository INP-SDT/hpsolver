# -*- coding: utf-8 -*-
"""Rho-one test.
"""
import numpy as np
from matplotlib import pyplot as plt
import hpsolver.sem as hps


def acoef(mesh):
    return np.zeros_like(mesh)


def bcoef(mesh):
    return np.ones_like(mesh)


def ccoef(mesh):
    return np.zeros_like(mesh)


def dcoef(mesh):
    return np.ones_like(mesh)


def reffunc(mesh):
    return mesh * (1 - mesh) * 0.5


def refgrad(mesh):
    return 0.5 - mesh

# MESH


root = hps.newroot(0, 1)

for _ in range(5):
    root = root.add_nodes()

root.activate(order=4)

# DATA

mesh = root.vmesh()

coeffs = {
    'a': acoef(mesh),
    'b': bcoef(mesh),
    'c': ccoef(mesh),
    'd': dcoef(mesh)
}

root.setcoeffs(coeffs)

# SOLVER

root.build_operator()

root.u_1 = 0.
root.u_2 = 0.

root.build_solution()

# POSTPROCESSING

mesh = root.hmesh()
data = root.hdata()
grad = root.hgrad()

plt.plot(mesh, data, '.b')
plt.plot(mesh, reffunc(mesh), '-r')

err1 = np.amax(np.abs(data - reffunc(mesh)))
err2 = np.amax(np.abs(grad - refgrad(mesh)))

print(err1)
print(err2)
