# -*- coding: utf-8 -*-
"""
Created on Thu Apr 17 17:12:50 2025

@author: ordin
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import  cm


###variable declarations
nx = 81
ny = 81
nt = 100
c = 1
dx = 2 / (nx - 1)
dy = 2 / (ny - 1)
sigma = .2
dt = sigma * dx

x =np.linspace(0, 2, nx)
y = np.linspace(0, 2, ny)

u = np.ones((ny, nx)) ##create a 1xn vector of 1's
un = np.ones((ny, nx)) ##

###Assign initial conditions

##set hat function I.C. : u(.5<=x<=1 && .5<=y<=1 ) is 2
u[int(.5 / dy):int(1 / dy + 1),int(.5 / dx):int(1 / dx + 1)] = 2 

###Plot Initial Condition
##the figsize parameter can be used to produce different sized images
fig = plt.figure(figsize=(11, 7), dpi=100)
ax = fig.add_subplot(2, 1, 2, projection="3d")   
X, Y = np.meshgrid(x, y)
plt.title("u(x,y,0)") #showing the title of the graph                                            
surf = ax.plot_surface(X, Y, u[:], cmap=cm.viridis)

for n in range(nt + 1): ##loop across number of time steps
    un=u.copy()
    u[1:, 1:]=(un[1:, 1:] - (c * dt / dx * (un[1:, 1:] - un[1:, :-1])) -
                              (c * dt / dy * (un[1:, 1:] - un[:-1, 1:])))
    u[0,:]=1
    u[-1,:]=1
    u[:,0]=1
    u[:,-1]=1

fig=plt.figure(figsize=(11, 7), dpi=100)
ax=fig.add_subplot(2, 2, 2, projection="3d") 
plt.title("u(x,y,t)") #showing the title of the graph
plt.xlabel('axes des X') #coordonates in X
plt.ylabel('axes des Y') #coordonates in Y
surf2 = ax.plot_surface(X, Y, u[:], cmap=cm.viridis)
