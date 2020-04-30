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

Sp = 1e6
Ip = 100
Rp = 0
yp = [Sp, Ip, Rp]
alfa0 = 2.65e-6
beta = 1
k = [.3e-5, .8e-5, 1.7e-5]

alfa = lambda I, k, alfa0=alfa0: alfa0/(1+k*I)

# Funkcija koja vraća dP/dt

def SIR(y, t, alfa, beta, k):
    S = y[0]
    I = y[1]
    R = y[2]
    return [-alfa(I, k)*S*I, alfa(I, k)*S*I - beta*I, beta*I]

t = linspace(0, 30, 1000)


for i in range(3):
    sol = odeint(SIR, yp, t, args=(alfa, beta, k[i]))
    
    
    ind_I = maks(sol[:,1])
    maks_I = sol[:,1][ind_I]
    vreme_max_I = t[ind_I]
    
    udeo = (.5/100)*Sp
    
    tudeo = 0
    
    print(f"Највећи број заражених: {maks_I:.2f}\nза {vreme_max_I:.2f} недеља")

    ind = 0
    
    for ti, v, ii in zip(t[ind_I:], sol[:,1][ind_I:], range(ind_I, len(sol)-ind_I)):
        if v<udeo:
            ind = ii
            tudeo = ti
            break;
    
    print(f"Потребно време до краја епидемије је {tudeo:.2f}")
    print(f"Подложан удео популације је {sol[:,0][ind]*100/Sp:.2f}%.\n")

    
    plt.plot(t, sol[:,0] ,c = 'b', label='S(t)')
    plt.plot(t, sol[:,1] ,c = 'r', label='I(t)')
    plt.plot(t, sol[:,2] ,c = 'g', label='R(t)')
    
    plt.title(f"k={k[i]}")
    plt.xlabel('$t$')
    plt.ylabel('Број јединки')
    plt.legend()
    plt.grid()
    plt.show()
