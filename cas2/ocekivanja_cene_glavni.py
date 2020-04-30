#!/bin/python

# Nikola Radojević 2019/176

import matplotlib.pyplot as plt
import numpy as np
from numpy import linspace
from scipy.integrate import odeint
from scipy.optimize import fsolve
from math import sqrt
from os import system

_=system("clear")

# Funkcija koja vraća dP/dt

def dif(P, t, a, b, c, d, m, n):
    P1, P2 = P
    dPdt = [P2, ((b+d)/n)*P1 - (m/n)*P2 - (a+c)/n]
    return dPdt

Pnule=[12, 1]

parametri = [
        (40, 2, 6, 8, -4, 1),
        (40, 2, 8, 7, -4, -3),
        (40, 2, 5, 3, 0.5, -1)
        ]

# Rešavanje diferencijalne jednačine
t = linspace(0, 20, 1000)

for arg in parametri:
    sol = odeint(dif, Pnule, t, args=arg) 

    fig, axes = plt.subplots(1, 2)
    axes[0].plot(t,sol[:,0])
    axes[0].grid()
    axes[0].set(ylabel="$P(t)$", xlabel="$t$")
    
    axes[1].plot(sol[:,0],sol[:,1])
    axes[1].grid()
    axes[1].set(ylabel="$\dot{P}$", xlabel="$P$")

    plt.show()

a = 40
b = 2
c = 8
d = 7
n = -0.1
m = 2*n*sqrt((-b-d)/n)

para = (a, b, c, d, m, n)


sol = odeint(dif, Pnule, t, args=para) 


fig, axes = plt.subplots(1, 2)
axes[0].plot(t,sol[:,0])
axes[0].grid()
axes[0].set(ylabel="$P(t)$", xlabel="$t$")

axes[1].plot(sol[:,0],sol[:,1])
axes[1].grid()
axes[1].set(ylabel="$\dot{P}$", xlabel="$P$")

plt.show()


a = 100
b = 2
c = 8
d = 7
n = -0.1
m = 2*n*sqrt((-b-d)/n)

para = (a, b, c, d, m, n)


sol = odeint(dif, Pnule, t, args=para) 


fig, axes = plt.subplots(1, 2)
axes[0].plot(t,sol[:,0])
axes[0].grid()
axes[0].set(ylabel="$P(t)$", xlabel="$t$")

axes[1].plot(sol[:,0],sol[:,1])
axes[1].grid()
axes[1].set(ylabel="$\dot{P}$", xlabel="$P$")

plt.show()

imaks=0
Pmaks=sol[:,0][imaks]
for i, v in enumerate(sol[:,0]):
    if Pmaks<v:
        imaks=i
        Pmaks=v

tmaks=t[imaks]

print(f"Najveća vrednost cene {Pmaks} se dostiže u t={tmaks}")
