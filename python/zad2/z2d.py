#!/bin/python

from math import sin, cos, atan, sqrt
import numpy as np
from numpy import linspace
from scipy.integrate import odeint
import matplotlib.pyplot as plt

omega0 = 10
alfa = omega0/20
x0 = 10
v0 = 0
F0 = 20
Omega = 2
m = 1

def A(x):
    global omega0, alfa, F0, m
    return (F0/m)/(sqrt(((omega0**2)-(x**2))**2+((2*alfa*x)**2)))

def fi(x):
    global alfa, omega0
    return atan(2*alfa*x/(omega0**2-x**2))

o = linspace(0, 2*omega0, 200)

a1 = [A(x) for x in o]
f1 = [fi(x) for x in o]

F0/=2

a2 = [A(x) for x in o]
f2 = [fi(x) for x in o]

F0*=2
alfa*=2

a3 = [A(x) for x in o]
f3 = [fi(x) for x in o]


# plot results
plt.plot(o, a1, 'b', label='Исти почетни услови')

plt.plot(o, a2, 'r', label=r'$F_0$ је двапут мања')

plt.plot(o, a3, 'g', label=r'$\alpha$ је двапут веће')

plt.xlabel(r'$\Omega$')
plt.ylabel(r'$A(\Omega)$')
plt.grid()
plt.legend()
plt.show()


plt.plot(o, f1, 'b', label='Исти почетни услови')

plt.plot(o, f2, 'r', label=r'$F_0$ је двапут мања')

plt.plot(o, f3, 'g', label=r'$\alpha$ је двапут веће')

plt.xlabel(r'$\Omega$')
plt.ylabel(r'$\varphi(\Omega)$')
plt.grid()
plt.legend()
plt.show()
