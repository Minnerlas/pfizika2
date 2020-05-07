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


X0=251.5920017110562; A0=101.03080674548222; alfa=1.2537600635601762; t0=0.696722080272715; omegad=5.771954544595728
omega0=5.9065534418861985; ksi=0.2122659306981231

m = 3.84
L = .49

t = linspace(0, 5, 1000)


def koleno(teta, t, ksi, omega0):
    return [teta[1], -2*ksi*omega0*teta[1] - omega0**2*teta[0]]

args=(ksi, omega0)

sol = odeint(koleno, (0, omega0), t, args=args)

plt.plot(t, sol[:,0])
plt.grid()
plt.show()
