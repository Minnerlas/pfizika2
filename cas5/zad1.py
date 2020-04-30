#!/bin/python

# Nikola Radojević 2019/176
 
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
from numpy import linspace
from scipy.integrate import odeint
from scipy.optimize import fsolve
from os import system

_=system("clear")


v = 60 #km/h
L = 5 #km
T = 180 #s
deltax = 50 #m
deltat = 0.1 #s

T = T /3600 #h
deltax = deltax / 1000 #km
deltat = deltat / 3600 #h

nt = int(T / deltat)
nx = int(L / deltax)

#print(T, deltat, nt)
#print(L, deltax, nx)

napmat = lambda n, m : [[0] * n for i in range(m)]

ro = napmat(nx, nt)

ro[0][0] = 200

#for i in range(nx//2):
#    ro[0][i] = 200


for i in range(nt):
    ro[i][0] = 200

x = np.linspace(0, L, nx)
t = np.linspace(0, T, nt)

def f(a, v, deltat, deltax):
    for x in range(1, len(a[0])):
        for t in range(0, len(a)-1):
            a[t+1][x] = a[t][x] - (v*deltat/deltax)*(a[t][x]-a[t][x-1])

f(ro, v, deltat, deltax)




t = np.linspace(0, T*60, nt)

xosa, tosa = np.meshgrid(x,t)

fig = plt.figure()
ax = fig.gca(projection="3d")
surf = ax.plot_surface(xosa, tosa, np.array(ro) , cmap=cm.jet)
ax.set_xlabel("x(km)")
ax.set_ylabel("t(min)")
ax.set_zlabel(r"$\rho(km^{-1})$")
cbar = fig.colorbar(surf, shrink=.5)
cbar.ax.set_ylabel(r"$\rho(km^{-1})$")
plt.show()



plt.contourf(x, t, ro)
plt.xlabel("x(km)")
plt.ylabel("t(min)")
cbar = plt.colorbar()
cbar.ax.set_ylabel(r"$\rho(km^{-1})$")
plt.show()
