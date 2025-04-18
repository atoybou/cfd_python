# -*- coding: utf-8 -*-
"""
Created on Sat Apr 19 00:52:35 2025

@author: ordin
"""

#2D Diffusion equation
#Central Difference scheme

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm


nx=31  #number of grid points, for x-coordinates
ny=31 #number of grid points, for y-coordinates
dx=2/(nx-1)   #distance between any pair of adjacent grid points
dy=2./(ny-1)
nt=15  #number of timesteps
nu=0.05   #the value of viscosity
sigma=0.25 #sigma is a parameter
dt=sigma*dx*dy/nu  

x=np.linspace(0, 2, nx)
y=np.linspace(0, 2, ny)

u=np.ones((ny, nx))  # create a 1xn vector of 1's
un=np.ones((ny, nx))

###Assign initial conditions
# set hat function I.C. : u(.5<=x<=1 && .5<=y<=1 ) is 2
u[int(.5 / dy):int(1 / dy + 1),int(.5 / dx):int(1 / dx + 1)]=2  
    
for n in range(nt+1): 
   un= u.copy()
   u[1:-1,1:-1]=(un[1:-1,1:-1]+nu*dt/dx**2*(un[1:-1,2:]-2*un[1:-1,1:-1]+un[1:-1, 0:-2])+nu*dt/dy**2*(un[2:,1:-1]-2*un[1:-1,1:-1]+un[0:-2, 1:-1]))
   u[0,:]=1
   u[-1,:]=1
   u[:,0]=1
   u[:,-1]= 1

fig=plt.figure()
ax=fig.add_subplot(2, 1, 2, projection="3d")
X, Y = np.meshgrid(x, y) 
plt.title("u(x,y,t)") #showing the title of the graph
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
ax.set_zlabel('$z$')
ax.set_zlim(1, 2.5)
surf = ax.plot_surface(X, Y, u[:], rstride=1, cstride=1, cmap=cm.viridis, linewidth=0, antialiased=True)