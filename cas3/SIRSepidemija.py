#!/bin/python

# Nikola Radojević 2019/176

import matplotlib.pyplot as plt
import numpy as np
from numpy import linspace
from scipy.integrate import odeint
from scipy.optimize import fsolve
from os import system

_=system("clear")

def maks(l):
    ind = maks = l[0]
    for i, v in enumerate(l):
        if v>maks:
            maks = v
            ind = i
    return ind

# Funkcija koja vraća dP/dt

def SIR(y, t, alfa, beta, gama):
    S = y[0]
    I = y[1]
    R = y[2]
    return [-alfa*S*I + gama*R, alfa*S*I - beta*I, beta*I - gama*R]

Sp = 1e6
Ip = 100
Rp = 0
yp = [Sp, Ip, Rp]
alfa = 2.65e-6
beta = 1
gama = .85



t = linspace(0, 30, 1000)
sol = odeint(SIR, yp, t, args=(alfa, beta, gama))


ind_I = maks(sol[:,1])
maks_I = sol[:,1][ind_I]
vreme_max_I = t[ind_I]

plt.plot(t, sol[:,0] ,c = 'b', label='S(t)')
plt.plot(t, sol[:,1] ,c = 'r', label='I(t)')
plt.plot(t, sol[:,2] ,c = 'g', label='R(t)')

plt.xlabel('$t$')
plt.ylabel('Број јединки')
plt.legend()
plt.grid()
plt.show()
