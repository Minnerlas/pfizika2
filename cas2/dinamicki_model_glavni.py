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

def dif(P, t, gama, a, b, c, d):
    dPdt = gama*((a+c)-P*(b+d))
    return dPdt

a = 22
b = 2
c = 5
d = 7
gama = 0.1

P = linspace(0, 10, 1000)

Qd = lambda P,a=a, b=b: a - b*P
Qs = lambda P,c=c, d=d: -c + d*P

plt.plot(P, list(map(Qd,P)), 'b', label='Q$_d$')
plt.plot(P, list(map(Qs,P)), 'r', label='Q$_s$')
plt.xlabel('P')
plt.ylabel('Q$_d$(P),Q$_s$(P)')
plt.legend()
plt.grid()
plt.show()

f = lambda P: Qd(P)-Qs(P)

znaci = list(map(lambda x: sign(f(x)), P))
razlike = diff(znaci)
zc = find(razlike)

#print(razlike)

Peq=[]

for i in zc:
    Peq+=[fsolve(f, P[i])]

if d == -5:
    Peq+=[fsolve(f,40)]

if len(Peq) == 0:
    print("Nema rešenja za Peq")
    exit() 

print(Peq[0][0])

Peq = Peq[0][0] # Peq je niz nizova rešenja, ali u ovom slučaju postoji samo jedno rešenje

Pnule=[Peq, 2*Peq, 0.5*Peq] 

argumenti = [
                {'c':'b', 'label':'$P_0=P_{eq}$'},
                {'c':'r', 'label':'$P_0=2\\cdot P_{eq}$'},
                {'c':'g', 'label':'$P_0=0.5\\cdot P_{eq}$'}
            ]

# Rešavanje diferencijalne jednačine

for P0, arg in zip(Pnule, argumenti):
    t = linspace(0, 10, 1000)
    sol = odeint(dif, P0, t, args=(gama, a, b, c, d))

    plt.plot(t, sol, **arg)

plt.xlabel('$t$')
plt.ylabel('$P(t)$')
plt.legend()
plt.grid()
plt.show()




a = 22
b = 2
c = 5
d = -5
gama = 0.1

P = linspace(0, 10, 1000)

Qd = lambda P,a=a, b=b: a - b*P
Qs = lambda P,c=c, d=d: -c + d*P

plt.plot(P, list(map(Qd,P)), 'b', label='Q$_d$')
plt.plot(P, list(map(Qs,P)), 'r', label='Q$_s$')
plt.xlabel('P')
plt.ylabel('Q$_d$(P),Q$_s$(P)')
plt.legend()
plt.grid()
plt.show()

f = lambda P: Qd(P)-Qs(P)

znaci = list(map(lambda x: sign(f(x)), P))
razlike = diff(znaci)
zc = find(razlike)

#print(razlike)

Peq=[]

for i in zc:
    Peq+=[fsolve(f, P[i])]

if d == -5:
    Peq+=[fsolve(f,40)]

if len(Peq) == 0:
    print("Nema rešenja za Peq")
    exit() 

print(Peq[0][0])

Peq = Peq[0][0] # Peq je niz nizova rešenja, ali u ovom slučaju postoji samo jedno rešenje

Pnule=[Peq, 2*Peq, 0.5*Peq] 

argumenti = [
                {'c':'b', 'label':'$P_0=P_{eq}$'},
                {'c':'r', 'label':'$P_0=2\\cdot P_{eq}$'},
                {'c':'g', 'label':'$P_0=0.5\\cdot P_{eq}$'}
            ]

# Rešavanje diferencijalne jednačine

for P0, arg in zip(Pnule, argumenti):
    t = linspace(0, 10, 1000)
    sol = odeint(dif, P0, t, args=(gama, a, b, c, d))

    plt.plot(t, sol, **arg)

plt.xlabel('$t$')
plt.ylabel('$P(t)$')
plt.legend()
plt.grid()
plt.show()
