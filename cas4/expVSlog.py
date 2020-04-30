#!/bin/python

# Nikola Radojević 2019/176

import matplotlib.pyplot as plt
import numpy as np
from numpy import linspace
from scipy.integrate import odeint
from scipy.optimize import fsolve
from os import system

_=system("clear")

# Funkcija koja vraća dP/dt

def exp_growth(x, t, r):
    return r*x

def log_growth(x, t, r, K):
    return r*x*(1-x/K)

opcije = [
        {'c':'b'},
        {'c':'orange'},
        {'c':'g'},
        ] 

r = [.1, .2, .3]
x0 = 50
K = 500

t = linspace(0, 70, 1000)


for rr, op in zip(r, opcije):
    #sol = odeint(exp_growth, x0, t, args=(rr,))
    sol = odeint(log_growth, x0, t, args=(rr, K))

    plt.plot(t, sol, label = f'r = {rr}', **op)


plt.plot(t, [K for i in t], '--', c = 'r')

plt.xlabel('$t$')
plt.ylabel('$x(t)$')
plt.title('$K = 500, x(0) = 50$')
plt.legend()
plt.grid()
plt.show()

plt.ylim(0, 600)
for rr, op in zip(r, opcije):
    soll = odeint(log_growth, x0, t, args=(rr, K))
    plt.plot(t, soll, label = f'r = {rr}', **op)

    sole = odeint(exp_growth, x0, t, args=(rr,))
    plt.plot(t, sole, c = '.8')



plt.plot(t, [K for i in t], '--', c = 'r')

plt.xlabel('$t$')
plt.ylabel('$x(t)$')
plt.title('$K = 500, x(0) = 50$')
plt.legend()
plt.grid()
plt.show()
