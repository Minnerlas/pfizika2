#!/bin/python

# Nikola Radojević 2019/176

import matplotlib.pyplot as plt
import numpy as np
from numpy import linspace
from scipy.integrate import odeint
from scipy.optimize import fsolve
from math import sqrt
from os import system
from cv2 import VideoCapture, imwrite, imshow, waitKey

_=system("clear")


from podaci import * 


X0=251.5920017110562; A0=101.03080674548222; alfa=1.2537600635601762; t0=0.696722080272715; omegad=5.771954544595728
omega0=5.9065534418861985; ksi=0.2122659306981231



m = 3.84
L = .49

t = linspace(0, 5, 1000)


def koleno(teta, t, ksi, omega0):
    return [teta[1], -2*ksi*omega0*teta[1] - omega0**2*teta[0]]

args=(ksi, omega0)

sol = odeint(koleno, (0, omega0), t, args=args)

teta = sol[:,0]

plt.plot(t, teta)
plt.xlabel("t[s]")
plt.ylabel(r"$\theta$ [rad]")
plt.grid()
plt.show()



XC_fit = xc[83:222]
vreme_fit = tc[83:222]

f = lambda t, X0, A0, alfa, t0, omegad: X0 + A0*np.exp(-alfa*(t-t0))*np.sin(omegad*(t - t0))
x = [f(t, X0, A0, alfa, t0, omegad) for t in vreme_fit]


K = (max(x)-X0)/max(teta)

X = [K*xx+X0 for xx in teta]
t = [tt+t0 for tt in t]

print(vreme_fit[0])

plt.plot(vreme_fit, XC_fit, label="Експериментални подаци")
plt.plot(t, X, label="Модел")
plt.legend()
plt.xlabel("t[s]")
plt.ylabel(r"x [пиксели]")
plt.grid()
plt.show()
