#!/bin/python


import numpy as np
from numpy import linspace
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# function that returns dy/dt
def pend(y, t, omega0, alfa):
    y1, y2 = y
    dydt = [y2, -(omega0**2*y1)-2*alfa*y2] 
    return dydt

omega0 = 1
alfa = [omega0, omega0/10, omega0*15, 0]
x0 = 10
v0 = 20
sol=[]

# solve ODE
for i in range(4):
    y0 = [x0,v0]
    t = linspace(0, 60, 1000)
    sol += [odeint(pend, [x0,v0], t, args=(omega0, alfa[i]))]

# plot results
'''
plt.plot(t,sol[:, 0])
plt.xlabel('time')
plt.ylabel('y(t)')
plt.grid()
plt.show()
'''

fig, axes = plt.subplots(2, 2)
axes[0,0].plot(sol[0][:,0],sol[0][:,1])
axes[0,0].grid()

axes[0,1].plot(sol[1][:,0],sol[1][:,1])
axes[0,1].grid()

axes[1,0].plot(sol[2][:,0],sol[2][:,1])
axes[1,0].grid()

axes[1,1].plot(sol[3][:,0],sol[3][:,1])
axes[1,1].grid()

plt.show()
