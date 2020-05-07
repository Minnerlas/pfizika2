#!/bin/python

# Nikola Radojević 2019/176

import matplotlib.pyplot as plt
import numpy as np
from numpy import linspace
from scipy.integrate import odeint
from scipy.optimize import fsolve
from os import system
from math import sin, cos, asin, sqrt
from numpy import conj, argmin, interp, matrix

_=system("clear")

def zipWith(f, l1, l2):
    return np.array([f(i,j) for (i,j) in zip(l1, l2)])

dd = [100e-9, 120e-9, 140e-9]
n0 = 1
n1 = 1.36
ns = 1.5

pod = [
        {"c":"r", "label":f"d={dd[0]/1e-9:.0f}nm"},
        {"c":"g", "label":f"d={dd[1]/1e-9:.0f}nm"},
        {"c":"b", "label":f"d={dd[2]/1e-9:.0f}nm"},
        ]
novi = [1, 3.9716, 1.9971, 1.5]
slojevi=[0] + [1, 2]*4 +[ 3]

lambd = linspace(380e-9, 750e-9, 371)#linspace(380e-9, 1e-9, 750e-9)
tetai1 = 0
epsilon0 = 8.845e-12
mi0 = 4*np.pi*1e-7
tetai = [0]
tetat = []
r = []
t = []


k0 = np.array([2*np.pi/i for i in lambd])


Mn = [matrix("1+0j 0+0j; 0+0j 1+0j") for i in lambd]


for d, arg in zip(dd, pod):
    tetai = [0]
    tetat = []
    r = []
    t = []
    for sloj, sled in zip(slojevi, slojevi[1:]):
        for i, l in enumerate(lambd):
            n0 = novi[sloj]
            n1 = novi[sled]
            tetat += [asin(n0*sin(tetai[i])/n1)]
            tetai += [tetat[-1]]
            Y = sqrt(epsilon0/mi0)*n1*cos(tetat[-1])
            h = n1*d*cos(tetai[-1])
            Mi = matrix([[cos(k0[i]*h),      1j*sin(k0[i]*h)/Y],
                         [1j*Y*sin(k0[i]*h), cos(k0[i]*h)     ]])
            Mn[i]*=Mi
   
    Y0 = sqrt(epsilon0/mi0)*novi[ 0]*cos(tetai[ 0])
    Ys = sqrt(epsilon0/mi0)*novi[-1]*cos(tetat[-1])

    for M in Mn:
        r += [(Y0*M[0, 0]+Y0*Ys*M[0, 1]-M[1, 0]-Ys*M[1, 1])
            / (Y0*M[0, 0]+Y0*Ys*M[0, 1]+M[1, 0]+Ys*M[1, 1])]

        t += [(2*Y0) / (Y0*M[0, 0]+Y0*Ys*M[0, 1]+M[1, 0]+Ys*M[1, 1])]

    r = np.array(r)
    t = np.array(t)

    R = np.real(r*conj(r))
    T = np.real((novi[-1]/novi[0]) * (cos(tetat[-1]) / cos(tetai[0]))*t*conj(t))

    plt.plot(lambd/1e-9, R*100, **arg)
    #plt.plot(lambd/1e-9, T*100, label ="T[%]", c="r")
plt.legend()
plt.title("График зависности R[%] и T[%] од таласне дужине [nm] за различите дебљине слојева")
plt.xlabel("Таласна дужина [nm]")
plt.ylabel("[%]")
plt.grid()
plt.show()

    #plt.plot(lambd/1e-9, (R+T)*100)
    #plt.grid()
    #plt.show()
