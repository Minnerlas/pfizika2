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
alfa = omega0/10
x0 = 10
v0 = 20
m=1
sol=[]

# solve ODE
y0 = [x0,v0]
t = linspace(0, 60, 1000)
sol = odeint(pend, [x0,v0], t, args=(omega0, alfa))

x=sol[:,0]
v=sol[:,1]

Ek=[m*vv**2/2 for vv in v]
Ep=[m*(omega0**2)*xx**2/2 for xx in x ]

# plot results
plt.plot(t,Ek,label='E$_k$')
plt.plot(t,Ep,label='E$_p$')
plt.xlabel('t')
plt.ylabel('E(t)')
plt.legend()
plt.grid()
plt.show()

plt.plot(t,[x+y for (x,y) in zip(Ek,Ep)],label='E$_u$')
plt.xlabel('t')
plt.ylabel('E(t)')
plt.legend()
plt.grid()
plt.show()


'''
fig, axes = plt.subplots(2, 2)
axes[0,0].plot(t,sol[0][:,0])
axes[0,0].grid()

axes[0,1].plot(t,sol[1][:,0])
axes[0,1].grid()

axes[1,0].plot(t,sol[2][:,0])
axes[1,0].grid()

axes[1,1].plot(t,sol[3][:,0])
axes[1,1].grid()
'''

plt.show()
