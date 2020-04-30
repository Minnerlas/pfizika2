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

with open('csv/lvm_data.csv') as f:
    ulaz = list(reader(f))

ulaz = ulaz[:]
godina = [float(a[0]) for a in ulaz[1:]] 
zec = [float(a[1]) for a in ulaz[1:]] 
lisica = [float(a[2]) for a in ulaz[1:]] 


# Funkcija koja vraća dP/dt

def exp_growth(x, t, r):
    return r*x

def log_growth(x, t, r, K):
    return r*x*(1-x/K)

def lv_model(y, t, r_prey, a, r_predator, b):
    x = y[0]
    y = y[1]
    return [r_prey*x - a*x*y, - r_predator*y + b*x*y]

r_prey = 0.4807; a = 0.02482; r_predator = 0.9272; b = 0.02756

tmin = min(godina)
tmax = max(godina)
K = max(zec)
x0 = zec[0]
y0 = lisica[0]

t = linspace(tmin, tmax, 200)

soll = odeint(lv_model, [x0, y0], t, args=(r_prey, a, r_predator, b))

plt.plot(t, soll[:,0], label = 'Зечеви', c = 'b')


plt.scatter(godina, zec, marker = '.', c = '0', label = 'Експериментални подаци за зечеве')

plt.xlabel('Година')
plt.ylabel('Зечеви ($\cdot 1000$)')
plt.title('Модел Lotka-Volterra')
plt.legend()
plt.grid()
plt.show()




plt.plot(t, soll[:,1], label = 'Лисице', c = 'b')


plt.scatter(godina, lisica, marker = '.', c = '0', label = 'Експериментални подаци за лисице')

plt.xlabel('Година')
plt.ylabel('Лисице ($\cdot 1000$)')
plt.title('Модел Lotka-Volterra')
plt.legend()
plt.grid()
plt.show()

print(f'omega = {(r_predator*r_prey)**.5}')



t = linspace(tmin, tmax+30, 200)

soll = odeint(lv_model, [x0, y0], t, args=(r_prey, a, r_predator, b))

plt.plot(t, soll[:,0], label = 'Зечеви', c = 'b')
plt.plot(t, soll[:,1], label = 'Лисице', c = 'orange')

plt.xlabel('Година')
plt.ylabel('Зечеви и лисице ($\cdot 1000$)')
plt.title('Модел Lotka-Volterra')
plt.legend()
plt.grid()
plt.show()



plt.plot(soll[:,0], soll[:,1], label = 'Зечеви', c = 'b', linewidth = 1)

plt.axvline(x = r_prey/a, linestyle = '--', c = 'r')
plt.axhline(y = r_predator/b, linestyle = '--', c = 'r')
plt.xlabel('Зечеви ($\cdot 1000$)')
plt.ylabel('Лисице ($\cdot 1000$)')
plt.title('Модел Lotka-Volterra')
plt.grid()
plt.show()


def lv_logistic_model(y, t, r_prey, K, a, r_predator, eps, b):
    x = y[0]
    y = y[1]
    return [r_prey*x*(1-x/K) - a*x*y, -r_predator*y + eps*b*y*x]

K = 250
eps = .9

t = linspace(1900, 2100, 1000)
soll = odeint(lv_logistic_model, [x0, y0], t, args=(r_prey, K, a, r_predator, eps, b))

plt.plot(t, soll[:,0], label = 'Зечеви', c = 'b')
plt.plot(t, soll[:,1], label = 'Лисице', c = 'orange')

plt.xlabel('Година')
plt.ylabel('Зечеви и лисице ($\cdot 1000$)')
plt.title('Модел Lotka-Volterra')
plt.legend()
plt.grid()
plt.show()




plt.plot(soll[:,0], soll[:,1], label = 'Зечеви', c = 'b', linewidth = 1)

plt.xlabel('Зечеви ($\cdot 1000$)')
plt.ylabel('Лисице ($\cdot 1000$)')
plt.title('Модел Lotka-Volterra')
plt.grid()
plt.show()
