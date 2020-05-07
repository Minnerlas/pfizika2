#!/bin/python

# Nikola Radojević 2019/176

import matplotlib.pyplot as plt
import numpy as np
from numpy import linspace
from scipy.integrate import odeint
from scipy.optimize import fsolve
from os import system
from math import sin, cos, asin, sqrt
from numpy import conj, argmin, interp

_=system("clear")

def zipWith(f, l1, l2):
    return np.array([f(i,j) for (i,j) in zip(l1, l2)])

d = 101e-9
n0 = 1
n1 = 1.36
ns = 1.5

lambd = linspace(380e-9, 750e-9, 371)#linspace(380e-9, 1e-p, 750e-9)
#print(lambd)
tetai1 = 0
epsilon0 = 8.845e-12
mi0 = 4*np.pi*1e-7

tetat1 = asin(n0*sin(tetai1)/n1)
tetai2 = tetat1

tetat2 = asin(n1*sin(tetai2)/ns)

Y0   = sqrt(epsilon0/mi0)*n0*cos(tetai1)
YS   = sqrt(epsilon0/mi0)*ns*cos(tetat2)
Y1TE = sqrt(epsilon0/mi0)*n1*cos(tetai2)
Y1TM = sqrt(epsilon0/mi0)*n1/cos(tetai2)

h = n1*d*cos(tetai2)

k0 = np.array([2*np.pi/i for i in lambd])

m11TE = np.array([cos(h*k) for k in k0])
m12TE = np.array([1j*sin(h*k)/Y1TE for k in k0])
m21TE = np.array([1j*sin(h*k)*Y1TE for k in k0])
m22TE = np.array([cos(h*k) for k in k0])

m11TM = np.array([cos(h*k) for k in k0])
m12TM = np.array([1j*sin(h*k)/Y1TM for k in k0])
m21TM = np.array([1j*sin(h*k)*Y1TM for k in k0])
m22TM = np.array([cos(h*k) for k in k0])

rTE = ((Y0*m11TE + Y0*YS*m12TE - m21TE - YS*m22TE)
        /(Y0*m11TE + Y0*YS*m12TE + m21TE + YS*m22TE))

rTM = ((Y0*m11TM + Y0*YS*m12TM - m21TM - YS*m22TM)
        /(Y0*m11TM + Y0*YS*m12TM + m21TM + YS*m22TM))

tTE = (2*Y0)/(Y0*m11TE + Y0*YS*m12TE + m21TE + YS*m22TE)
tTM = (2*Y0)/(Y0*m11TM + Y0*YS*m12TM + m21TM + YS*m22TM)

RTE = rTE * conj(rTE)
RTM = rTM * conj(rTM)

TTE = tTE*conj(tTE)*(ns/n0)*cos((tetat2)/cos(tetai1))
TTM = tTM*conj(tTM)*(ns/n0)*cos((tetat2)/cos(tetai1))

R = np.array(list(map(np.real, (RTE + RTM)*.5)))
T = np.array(list(map(np.real, (TTE + TTM)*.5)))

print(f"Таласна дужина која је најмање присутна у рефлектованој светлости је {lambd[argmin(R)]/1e-9}nm.")

print(interp(632.8, lambd, T))

plt.plot(lambd/1e-9, R*100)
plt.grid()
plt.title("График зависности R[%] од таласне дужине[nm]")
plt.xlabel("Таласна дужина [nm]")
plt.ylabel("R[%]")
plt.show()

plt.plot(lambd/1e-9, T*100)
plt.grid()
plt.title("График зависности T[%] од таласне дужине[nm]")
plt.xlabel("Таласна дужина [nm]")
plt.ylabel("T[%]")
plt.show()

plt.plot(lambd/1e-9, (R+T)*100)
plt.grid()
plt.title("График зависности збира R+T[%] од таласне дужине[nm]")
plt.xlabel("Таласна дужина [nm]")
plt.ylabel("R+T[%]")
plt.show()
