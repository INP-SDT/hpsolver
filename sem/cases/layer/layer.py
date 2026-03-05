# -*- coding: utf-8 -*-
"""Boundary layer.
"""
import numpy as np
from matplotlib import pyplot as plt
import hpsolver.sem as hps

# PARAMETERS

A = 5
B = 0.1


def acoef(mesh):
    return A * np.ones_like(mesh)


def bcoef(mesh):
    return B * np.ones_like(mesh)


def ccoef(mesh):
    return np.zeros_like(mesh)


def dcoef(mesh):
    return np.zeros_like(mesh)


def reffunc(x):
    return (np.exp(x*(A/B)) - np.exp(A/B)) / (1 - np.exp(A/B))


def refgrad(x):
    return (A/B) * np.exp(x*(A/B)) / (1 - np.exp(A/B))

# MESH


root = hps.newroot(0, 1)

for _ in range(6):
    root = root.add_nodes()

root.activate(order=5)

# DATA

mesh = root.vmesh()

coeffs = {
    'a': root.stack(acoef(mesh)),
    'b': root.stack(bcoef(mesh)),
    'c': root.stack(ccoef(mesh)),
    'd': root.stack(dcoef(mesh))
}

root.setcoeffs(coeffs)

# SOLVER

root.build_operator()

root.u_1 = 1.
root.u_2 = 0.

root.build_solution()

# POSTPROCESSING

mesh = root.hmesh()
data = root.hdata()
grad = root.hgrad()

plt.semilogx(1 - mesh, data, '.b')
plt.semilogx(1 - mesh, reffunc(mesh), '-r')

# plt.plot(mesh, grad, '.b')
# plt.plot(mesh, refgrad(mesh), '-r')

err1 = np.amax(np.abs(data - reffunc(mesh)))
err2 = np.amax(np.abs(grad - refgrad(mesh)))

print(err1)
print(err2)
