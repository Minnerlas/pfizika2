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
    ind = 0
    maks = l[0]
    for i, v in enumerate(l):
        if v>maks:
            maks = v
            ind = i
    return ind

# Funkcija koja vraća dP/dt

def SIR(y, t, alfa, beta):
    S = y[0]
    I = y[1]
    R = y[2]
    return [-alfa*S*I, alfa*S*I - beta*I, beta * I ]

R0 = [3, 6, 15]
virusi = [
        "Инфлуенца",
        "Полио",
        "Рубеола"
        ]
Sp = 1e6
Ip = 100
Rp = 0
yp = [Sp, Ip, Rp]
beta = 1
alfa = [r0 * beta / Sp for r0 in R0]



t = linspace(0, 15, 1000)

for i in range(3):
    sol = odeint(SIR, yp, t, args=(alfa[i], beta))
    
    v = (1 - beta / (alfa[i] * Sp))*100
    print(virusi[i] + f" {v:.2f}%")

    plt.plot(t, sol[:,0] ,c = 'b', label='S(t)')
    plt.plot(t, sol[:,1] ,c = 'r', label='I(t)')
    plt.plot(t, sol[:,2] ,c = 'g', label='R(t)')
    
    plt.title(virusi[i] + f": $R_0={R0[i]}$")
    plt.xlabel('$t$')
    plt.ylabel('Број јединки')
    plt.legend()
    plt.grid()
    plt.show()
