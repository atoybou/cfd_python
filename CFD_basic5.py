# -*- coding: utf-8 -*-
"""
Created on Thu Apr 17 17:12:50 2025

@author: ordin
"""

from mpl_toolkits.mplot3d import Axes3D    ##New Library required for projected 3d plots

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
surf = ax.plot_surface(X, Y, u[:], cmap=cm.viridis)