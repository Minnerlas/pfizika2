from scipy.integrate import odeint
from scipy.optimize import fsolve
import numpy as np
from numpy import linspace
import matplotlib.pyplot as plt
from functools import reduce
from operator import iconcat

napmat = lambda n, m : [[0] * n for i in range(m)]

r = [1.00, 0.72, 1.53, 1.27]

a = [
        [1.00, 1.09, 1.52, 0.00],
        [0.00, 1.00, 0.44, 1.36],
        [2.33, 0.00, 1.00, 0.47],
        [1.21, 0.51, 0.35, 1.00],
    ]

def sistem(x, t, a, r):
    iz = []
    for xi, ri, ai in zip(x, r, a):
        s = 0
        for aij, xj in zip(ai, x):
            s += aij*xj
        iz += [ri*xi*(1-s)]
    return iz

rez = fsolve(sistem, [1 for _ in range(4)], args = (0, a, r))
print(rez)

t = linspace(0, 600, 10000)

stac = rez2 = odeint(sistem, rez, t, args=(a, r))
rez3 = odeint(sistem, [1 for i in range(4)], t, args=(a, r))

for i in range(4):
    plt.plot(t, rez2[:,i], label = f"Врста {i+1}")
plt.legend()
plt.grid()
plt.xlabel("Време у недељама")
plt.ylabel("популација $(\\cdot 1000)$")
plt.show()

args = [
        {'label' : "Повећање од 0,1%", },
        {'label' : "Повећање од 0,2%", },
        {'label' : "Повећање од 0,3%", },
        ]

for i, p in enumerate([1.001, 1.002, 1.003]):
    trez = rez.copy()
    trez[2]*=p
    rez2 = odeint(sistem, trez, t, args=(a, r))
    plt.plot(t, rez2[:,0], **args[i])
plt.legend()
plt.grid()
plt.xlabel("Време у недељама")
plt.ylabel("популација $(\\cdot 1000)$")
plt.show()



# FDM

deltat = t[1]


xevi = napmat(len(r), len(t))
for i, x in enumerate(rez):
    xevi[0][i] = x

def fdm(xevi, tu, a, r, deltat):
    for t in range(1, len(tu)):
        #for xi in range(1, len(xevi)):
        for i, (xi, ri, ai) in enumerate(zip(xevi[:][t-1], r, a)):
            s = 0
            for aij, xj in zip(ai, xevi[:][t-1]):
                s += aij*xj
            xevi[t][i] = xi + ri*xi*(1-s)*deltat


fdm(xevi, t, a, r, deltat)

xevi = np.array(xevi)

fig, axs = plt.subplots(2, 2)
for i, ax in enumerate(reduce(iconcat, axs, [])):
    ax.plot(t, stac[:,i], 'b', label = "fsolve")
    ax.plot(t, xevi[:,i], 'r--', label = "Метода коначних разлика")
    ax.title.set_text(f"Врста {i+1}")
    ax.legend()
    ax.grid()
fig.text(0.5, 0.02, "Време у недељама", ha='center', va='center')
fig.text(0.02, 0.5, "популација $(\\cdot 1000)$", ha='center', va='center', rotation='vertical')
plt.show()
