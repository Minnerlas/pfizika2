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


v = 60
L = 2.4 #km
T = 180 #s
deltax = 50 #m
deltat = 0.1 #s
vm = 57.91 #km/h
rom = 103.55 #km^-1

T = T /3600 #h
deltax = deltax / 1000 #km
deltat = deltat / 3600 #h

nt = int(T / deltat)
nx = int(L / deltax)

#print(T, deltat, nt)
#print(L, deltax, nx)

napmat = lambda n, m : [[0] * n for i in range(m)]

ro = napmat(nx, nt)

x = np.linspace(0, L, nx)
t = np.linspace(0, T, nt)

def c(x):
    global vm, rom
    return vm*(1-(x/rom))

for i in range(nt):
    ro[i][0] = .3 * rom


def f(a, v, deltat, deltax):
    for x in range(1, len(a[0])):
        for t in range(0, len(a)-1):
            a[t+1][x] = a[t][x] - (c(a[t][x])*deltat/deltax)*(a[t][x]-a[t][x-1])

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

fig, axs = plt.subplots(1, 3)

for ind, tt in enumerate([100, 120, 160]):
    i = int((tt/3600)/deltat)
    axs[ind].grid()
    axs[ind].plot(x, ro[i])
    axs[ind].set_title(f't = {tt}s')

axs[0].set(ylabel = r'$\rho$ $[km^{-1}]$' )
axs[1].set(xlabel = r'$x$ $[km]$' )
plt.show()

