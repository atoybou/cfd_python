# -*- coding: utf-8 -*-
"""
Created on Thu Jul  3 22:49:09 2025

@author: ordin
"""


import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm


nx=61
ny=61
nt=600
dx=2/(nx-1)
dy=2/(ny-1)
nu=0.01   #the value of viscosity
sigma=0.0009 #sigma is a parameter
dt=sigma*dx*dy/nu  

x=np.linspace(0,2,nx)
y=np.linspace(0,2,ny)

u=np.ones((ny,nx))
v=np.ones((ny,nx))
u_n=np.ones((ny,nx))
v_n=np.ones((ny,nx))

##set hat function I.C. : u(.5<=x<=1 && .5<=y<=1 ) is 2
u[int(.5/dy):int(1/dy + 1),int(.5/dx):int(1/dx + 1)]=1.75
v[int(.5/dy):int(1/dy + 1),int(.5/dx):int(1/dx + 1)]=1.75


for i in range(nt+1):
    u_n=u.copy()
    v_n=v.copy()

    u[1:-1, 1:-1]=(u_n[1:-1,1:-1] -
                     dt/dx * u_n[1:-1,1:-1] * 
                     (u_n[1:-1,1:-1] - u_n[1:-1,0:-2]) - 
                     dt / dy * v_n[1:-1,1:-1] * 
                     (u_n[1:-1,1:-1] - u_n[0:-2,1:-1]) + 
                     nu * dt / dx**2 * 
                     (u_n[1:-1,2:] - 2*u_n[1:-1,1:-1] + u_n[1:-1,0:-2]) + 
                     nu * dt / dy**2 * 
                     (u_n[2:,1:-1] - 2*u_n[1:-1,1:-1] + u_n[0:-2,1:-1]))
    
    v[1:-1,1:-1]=(v_n[1:-1,1:-1] - 
                     dt / dx * u_n[1:-1,1:-1] *
                     (v_n[1:-1,1:-1] - v_n[1:-1,0:-2]) -
                     dt / dy * v_n[1:-1, 1:-1] * 
                    (v_n[1:-1,1:-1] - v_n[0:-2,1:-1]) + 
                     nu * dt / dx**2 * 
                     (v_n[1:-1,2:] - 2*v_n[1:-1, 1:-1] + v_n[1:-1,0:-2]) +
                     nu * dt / dy**2 *
                     (v_n[2:,1:-1] - 2*v_n[1:-1,1:-1] + v_n[0:-2,1:-1]))
     
    u[0,:]=1
    u[-1,:]=1
    u[:,0]=1
    u[:,-1]=1
    
    v[0,:]=1
    v[-1,:]=1
    v[:,0]=1
    v[:,-1]=1

X,Y=np.meshgrid(x,y)
fig=plt.figure()
ax=fig.add_subplot(projection='3d')
plt.title("u(x,y,t)") #showing the title of the graph
ax.set_xlabel('axe des $x$')
ax.set_ylabel('axe des $y$')
ax.set_zlabel('$z$')
surf = ax.plot_surface(X, Y, v, rstride=1, cstride=1, cmap=cm.viridis, linewidth=0, antialiased=True)