#!/bin/python

# Nikola Radojević 2019/176

import matplotlib.pyplot as plt
import numpy as np
from numpy import linspace
from scipy.integrate import odeint
from scipy.optimize import fsolve, curve_fit
from math import sqrt
from os import system

_=system("clear")


from podaci2 import *

<<<<<<< HEAD
plt.plot(tc, xc)
plt.grid()
plt.show()

#print(xc)
=======
XC_fit = xc[83:222]
vreme_fit = t[83:222]

f = lambda t, X0, A0, alfa, t0, omegad: X0 + A0*np.exp(-alfa*(t-t0))*np.sin(omegad*(t - t0))


xopt, xcov = curve_fit(f, vreme_fit, XC_fit)
# print(xcov)

x = [f(t,*xopt) for t in vreme_fit]
X0=xopt[0]
A0=xopt[1]
alfa=xopt[2]
t0=xopt[3]
omegad=xopt[4]
m = 3.84
L = .49
g = 9.81

ksi = np.sqrt(alfa**2/(alfa**2+omegad**2))
omega0 = alfa/ksi

plt.plot(vreme_fit, x, label = "Оптимална крива") 


plt.plot(vreme_fit, XC_fit, label = "Експериментални подаци")
plt.legend()
plt.xlabel(r"t [s]")
plt.ylabel(r"x [пиксели]")
plt.grid()
plt.show()

print(f"X0={xopt[0]}; A0={xopt[1]}; alfa={xopt[2]}; t0={xopt[3]}; omegad={xopt[4]}\nomega0={omega0}; ksi={ksi}")
>>>>>>> 5a7f8aa31b2bff1f276470420b11e433d66f52fd
