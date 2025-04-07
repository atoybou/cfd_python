# -*- coding: utf-8 -*-
"""
Created on Sat Apr  5 10:33:39 2025

@author: ordin
"""

#1D Linear convection

import numpy as np
import matplotlib.pyplot as plt

nx=41   #number of grid points
dx=2/(nx-1)   #distance between any pair of adjacent grid points
nt=25   #number of timesteps
dt=0.025
c=1 #wavespeed c=1

u = np.ones(nx)      #setting up our initial condition (IC)
u[int(0.5/dx):int(1/dx+1)]=2  #setting u=2 between 0.5 and 1 as per our IC
plt.plot(np.linspace(0,2,nx),u)

un = np.ones(nx) #initialize a temporary array
for n in range(nt):  
    un = u.copy()
    for i in range(1, nx): 
        u[i] = un[i] - c * dt / dx * (un[i] - un[i-1])
        
plt.plot(np.linspace(0,2,nx),u)
plt.show()