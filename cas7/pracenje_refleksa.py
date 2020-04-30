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

MIN, MAX = 0, 0

def ogranici(x):
    if x > 255:
        return 0
    return x

def kontrast(x):
    global MIN, MAX
    return np.clip(0, 255, (255/(MAX-MIN))*(x-MIN))

prag = 0.625
def im2bw(x):
    global prag
    if x/256<prag:
        return 0
    return 255



vidcap = VideoCapture('snimci/referentni_klip.avi')
success, image = vidcap.read()
count = 0
channel_initials = list('BGR')
xc, yc = [], []



while success:
    # Obrada slike
    
    rgb_slika = image

    crvena_slika = np.zeros(shape=image.shape, dtype=np.uint8)
    crvena_slika[:, :, 0] = image[:,:,2]
    crvena_slika[:, :, 1] = image[:,:,2]
    crvena_slika[:, :, 2] = image[:,:,2]
    
    siva_slika = np.zeros(shape=image.shape, dtype=np.uint8)
    siva_slika[:, :, 0] = siva_slika[:, :, 1] = siva_slika[:, :, 2] = image[:,:,2]*.3 + image[:,:,1]*.59 + image[:,:,0]*.11

    razlika_slika = np.vectorize(ogranici)(crvena_slika.astype(np.uint16) - siva_slika.astype(np.uint16)).astype(np.uint8)

    MIN = np.amin(razlika_slika) # odredjivanje minimalne vrednosti intenziteta u slici
    MAX = np.amax(razlika_slika) # odredjivanje maksimalne vrednosti intenziteta u slici
    sv_slika = ((255/(MAX-MIN))*(razlika_slika.astype(np.float)-MIN)).astype(np.uint8)
    cb_slika = np.vectorize(im2bw)(sv_slika).astype(np.uint8)
    
    #imshow('crvena slika', crvena_slika)
    #imshow('siva slika', siva_slika)
    #imshow('razlika slika', razlika_slika)
    #imshow('sv slika', sv_slika)
    #imshow('cb slika', cb_slika)

    xu, yu = 0, 0
    n = 0
    for x in range(cb_slika.shape[0]):
        for y in range(cb_slika.shape[1]):
            if cb_slika[x,y,0] > 128:
                xu += x
                yu += y
                n  += 1
    xc += [xu/n]
    yc += [yu/n]



    #waitKey(0)

    print(crvena_slika)
    imwrite(f"frejmovi/frame{count:03}.jpg", cb_slika)     # save frame as JPEG file      

    success, image = vidcap.read()
    print('Read a new frame: ', success, '\t', count)
    count += 1


print(xc)
print(yc)

t = [i/120 for i in range(count)]

plt.plot(t, yc)
plt.grid()
plt.xlabel("време[s]")
plt.ylabel("положај маркера на апсциси [пискел]")
plt.show()

print("\a")
