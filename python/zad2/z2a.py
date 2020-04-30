#!/bin/python

from math import sin, cos
import numpy as np
from numpy import linspace
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# function that returns dy/dt
def pend(y, t, omega0, F0, Omega, m, alfa):
    y1, y2 = y
    dydt = [y2, F0*sin(t*Omega)-(omega0**2*y1)-2*alfa*y2] 
    return dydt

omega0 = 10
alfa = omega0/20
x0 = 10
v0 = 0
F0 = 20
Omega = 2
m = 1
sol = []

# solve ODE
y0 = [x0,v0]
t = linspace(0, 60, 1000)
sol = odeint(pend, [x0,v0], t, args=(omega0, F0, Omega, m, alfa))

# plot results
plt.plot(t,sol[:, 0])
plt.xlabel('$t$')
plt.ylabel('$x(t)$')
plt.grid()
plt.show()

plt.plot(sol[:, 0],sol[:, 1])
plt.xlabel('$x$')
plt.ylabel(r'$\frac{dx}{dt}$')
plt.grid()
plt.show()

plt.plot(sol[:, 0],sol[:, 1])
plt.xlabel('$x$')
plt.ylabel(r'$\frac{dx}{dt}$')
plt.grid()
plt.xlim(-1,1)
plt.ylim(-5,5)
plt.show()
