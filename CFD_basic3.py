# -*- coding: utf-8 -*-
"""
Created on Sat Apr 12 23:30:47 2025

@author: ordin
"""

#1D Diffusion equation
#Central Difference scheme

import numpy as np
import matplotlib.pyplot as plt

nx=41   #number of grid points
dx=2/(nx-1)   #distance between any pair of adjacent grid points
nt=20   #number of timesteps
nu=0.3   #the value of viscosity
sigma=0.2 #sigma is a parameter
dt=sigma*(dx**2)/nu 

u=np.ones(nx)      #setting up our initial condition (IC)
u[int(0.5/dx):int(1/dx+1)]=2  #setting u=2 between 0.5 and 1 as per our IC

plt.grid(True)   #activate the grid
plt.plot(np.linspace(0,2,nx),u,"g--", linewidth=0.8, label="u_0(x)")  #plot of u_0(x)

un = np.ones(nx) #initialize a temporary array
for n in range(nt):  
    un=u.copy()
    for i in range(1, nx-1): 
        u[i]=un[i]+nu*dt/(dx**2)*(un[i+1]-2*un[i]+un[i-1])
        
plt.title("Representation of u_0 and u")       
plt.plot(np.linspace(0,2,nx),u, "b", linewidth=0.8, label="u(x,t)") #plot of u(x,t)
plt.legend() #showing the legend
plt.show()