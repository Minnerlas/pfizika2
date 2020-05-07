#!/bin/python

# Nikola Radojević 2019/176

import matplotlib.pyplot as plt
import numpy as np
from numpy import linspace
from scipy.integrate import odeint
from scipy.optimize import fsolve
from os import system

_=system("clear")

def find(x):
    izlaz=[]
    for i, a in enumerate(x):
        if a!=0:
            izlaz+=[i]
    return izlaz

def sign(x):
    if x>0:
        return 1
    elif x<0:
        return -1
    return 0

diff = lambda x: [b-a for (a,b) in zip(x, x[1:])]

# Funkcija koja vraća dP/dt

def koleno(teta, t, J, m, g, L, omega0, ksi):
    T = ((m*g*L)/2-omega0)*J
    c = ksi*omega0*J
    return [teta[1], -(c/J)*teta[1] - ((m*g*L)/2 - T/J) * teta[0]]


t = linspace(0, 5, 1000)

args = (0.154, 4, 9.81, 0.34, 6.28, 0.228)


sol = odeint(koleno, (0, 2*3.14159265358979), t, args=args)

plt.grid()
plt.plot(t, sol[:,0])
plt.title(r"Зависност $\theta$ од времена")
plt.xlabel(r"t[s]")
plt.ylabel(r"$\theta [rad]$")
plt.show()

fig, axs = plt.subplots(2, 2)

ksi = [
        0.1,
        0.3,
        0.5,
        0.7
        ]

for ks, ax in zip(ksi, axs.flat):
    sol = odeint(koleno, (0, 2*3.14159265358979), t, args=(0.154, 4, 9.81, 0.34, 6.28, ks))
    ax.grid()
    ax.set_title(f"$\\xi = {ks}$")
    ax.plot(t, sol[:,0])

fig.suptitle(r"Зависност $\theta$ од времена за различите вредности $\xi$")
fig.text(0.5, 0.04, 't[s]', ha='center')
fig.text(0.04, 0.5, r'$\theta$ [rad]', va='center', rotation='vertical')

plt.show()
