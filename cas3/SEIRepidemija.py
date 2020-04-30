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
Ep = 0
Ip = 100
Rp = 0
yp = [Sp, Ep, Ip, Rp]
alfa = 2.65e-6
beta = 1
delta = [.3, .5, 1]


# Funkcija koja vraća dP/dt

def SIR(y, t, alfa, beta, delta):
    S = y[0]
    E = y[1]
    I = y[2]
    R = y[3]
    return [-alfa*S*I, 
            alfa*S*I - delta*E, 
            delta*E - beta*I, 
            beta*I]

t = linspace(0, 52, 1000)


for i in range(3):
    sol = odeint(SIR, yp, t, args=(alfa, beta, delta[i]))
    
    
    ind_I = maks(sol[:,2])
    maks_I = sol[:,2][ind_I]
    vreme_max_I = t[ind_I]
    
    udeo = (.5/100)*Sp
    
    
    print(f"Највећи број заражених: {maks_I:.2f}\nза {vreme_max_I:.2f} недеља")

    ind = 0
    ind2 = 0
    tii = 0
    tee = 0

    for ti, v, ii in zip(t[ind_I:], sol[:,2][ind_I:], range(ind_I, len(sol)-ind_I)):
        if v<udeo:
            ind = ii
            tii = ti
            break;
    
    print(f"Потребно време до краја епидемије је {tii:.2f}")
    print(f"Подложан удео популације је {sol[:,0][ind]*100/Sp:.2f}%.")

    ind_I = maks(sol[:,1])
    maks_I = sol[:,1][ind_I]
    vreme_max_I = t[ind_I]
    
    print(f"Највећи број заражених: {maks_I:.2f}\nза {vreme_max_I:.2f} недеља")

    for te, v, ii in zip(t[ind_I:], sol[:,1][ind_I:], range(ind_I, len(sol)-ind_I)):
        if v<udeo:
            ind2 = ii
            tee = te
            break;
    
    print(f"Потребно време до краја епидемије је {tee:.2f}")
    print(f"Подложан удео популације је {sol[:,0][ind2]*100/Sp:.2f}%.\n")



    plt.plot(t, sol[:,0] ,c = 'b', label='S(t)')
    plt.plot(t, sol[:,1] ,c = 'y', label='E(t)')
    plt.plot(t, sol[:,2] ,c = 'r', label='I(t)')
    plt.plot(t, sol[:,3] ,c = 'g', label='R(t)')
    
    plt.title(f"$\\delta={delta[i]}$")
    plt.xlabel('$t$')
    plt.ylabel('Број јединки')
    plt.legend()
    plt.grid()
    plt.show()
