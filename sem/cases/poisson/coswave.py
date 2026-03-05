# -*- coding: utf-8 -*-
"""Sinwave test.
"""
import numpy as np
from matplotlib import pyplot as plt
import hpsolver.sem as hps


def acoef(mesh):
    return np.zeros_like(mesh)


def bcoef(mesh):
    return 1. + mesh


def ccoef(mesh):
    return np.zeros_like(mesh)


def dcoef(mesh):

    rho_1 = + 4 * np.pi**2 * (mesh + 1) * np.sin(2*np.pi*mesh)
    rho_2 = - 2 * np.pi * np.cos(2*np.pi*mesh)

    return rho_1 + rho_2


def reffunc(mesh):
    return np.sin(2*np.pi*mesh)


def refgrad(mesh):
    return 2*np.pi*np.cos(2*np.pi*mesh)

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

# POSTPROCESSSING

mesh = root.hmesh()
data = root.hdata()
grad = root.hgrad()

plt.plot(mesh, data, '.b')
plt.plot(mesh, reffunc(mesh), '-r')

err1 = np.amax(np.abs(data - reffunc(mesh)))
err2 = np.amax(np.abs(grad - refgrad(mesh)))

print(err1)
print(err2)
