#!/bin/python

from math import sin, cos, sqrt
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

def A(x):
    global omega0, alfa, F0, m
    return (F0/m)/(sqrt(((omega0**2)-(x**2))**2+((2*alfa*x)**2)))


# solve ODE
y0 = [x0,v0]

o = linspace(0, 2*omega0, 200)
an = [A(om) for om in o]

# plot results
plt.plot(o,an,label='Аналитичко решење')

t = linspace(0,300,2000)

num=[]
for om in o:
    sol = odeint(pend, [x0,v0], t, args=(omega0, F0, om, m, alfa))
    x=sol[:,0]
    num+=[max(x[ int(len(x)*5/6) :])]

plt.plot(o,num, 'r--', label='Нумеричко решење')
plt.xlabel('$\Omega$')
plt.ylabel('A($\Omega$)')
plt.grid()
plt.legend()

plt.show()

print(f'{(max(num)-max(an))/max(an)*100:.4f}%')
