# -*- coding: utf-8 -*-
"""
Created on Mon Apr  7 22:58:56 2025

@author: ordin
"""

#1D Non-Linear convection

import numpy as np
import matplotlib.pyplot as plt

nx=41   #number of grid points
dx=2/(nx-1)   #distance between any pair of adjacent grid points
nt=25   #number of timesteps
dt=0.025

u=np.ones(nx)      #setting up our initial condition (IC)
u[int(0.5/dx):int(1/dx+1)]=2  #setting u=2 between 0.5 and 1 as per our IC

plt.grid(True)   #activate the grid
plt.plot(np.linspace(0,2,nx),u,"g--", linewidth=0.8, label="u_0(x)")  #plot of u_0(x)

un = np.ones(nx) #initialize a temporary array
for n in range(nt):  
    un=u.copy()
    for i in range(1, nx): 
        u[i]=un[i]-un[i]*dt/dx*(un[i] - un[i-1])
        
plt.title("Representation of u_0 and u")       
plt.plot(np.linspace(0,2,nx),u, "b", linewidth=0.8, label="u(x,t)") #plot of u(x,t)
plt.legend() #permet d'afficher la legende 
plt.show()