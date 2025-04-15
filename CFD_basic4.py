# -*- coding: utf-8 -*-
"""
Created on Mon Apr 14 23:29:40 2025

@author: ordi
"""

#Burgers' equation


import numpy as np
import matplotlib.pyplot as plt


###variable declarations
nx = 101
nt = 100
dx = 2 * np.pi / (nx - 1)
nu = 0.07
dt = dx * nu

x = np.linspace(0, 2 * np.pi, nx)
un = np.empty(nx)
t = 0

u =  #initialize u

for n in range(nt):
    un = u.copy()
    for i in range(1, nx-1):
        u[i] = un[i] - un[i] * dt / dx *(un[i] - un[i-1]) + nu * dt / dx**2 *\
                (un[i+1] - 2 * un[i] + un[i-1])
    u[0] = un[0] - un[0] * dt / dx * (un[0] - un[-2]) + nu * dt / dx**2 *\
                (un[1] - 2 * un[0] + un[-2])
    u[-1] = u[0]
        
u_analytical = #compute analytical solution of Burgers' equation

plt.figure(figsize=(11, 7), dpi=100)
plt.plot(x,u, marker='o', lw=2, label='Computational')
plt.plot(x, u_analytical, label='Analytical')
plt.xlim([0, 2 * np.pi])  #limits to be adapted
plt.ylim([0, 10]) #limits to be adapted
plt.legend()