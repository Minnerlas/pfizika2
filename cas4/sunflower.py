#!/bin/python

# Nikola Radojević 2019/176

import matplotlib.pyplot as plt
import numpy as np
from numpy import linspace
from scipy.integrate import odeint
from scipy.optimize import fsolve
from os import system
from csv import reader

_=system("clear")

with open('csv/sunflower_data.csv') as f:
    ulaz = list(reader(f))

ulaz = ulaz[:]
age = [float(a[0]) for a in ulaz[1:]] 
height = [float(a[1]) for a in ulaz[1:]] 


# Funkcija koja vraća dP/dt

def exp_growth(x, t, r):
    return r*x

def log_growth(x, t, r, K):
    return r*x*(1-x/K)

r = .1

tmin = min(age)
tmax = max(age)
K = max(height)
x0 = height[0]

t = linspace(tmin, tmax, 200)

plt.ylim(0, 280)

sole = odeint(exp_growth, x0, t, args=(r,))
soll = odeint(log_growth, x0, t, args=(r, K))

plt.plot(t, soll, label = 'Логистички модел', c = 'b')
plt.plot(t, sole, label = 'Експоненцијални модел', c = 'r')


plt.scatter(age, height, marker = '.', c = '0', label = 'Експериментални подаци')

plt.xlabel('Старост (дани)')
plt.ylabel('Висина $(cm)$')
plt.title('Раст сунцокрета')
plt.legend()
plt.grid()
plt.show()
