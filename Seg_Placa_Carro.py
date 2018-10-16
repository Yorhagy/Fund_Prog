# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 14:10:12 2018

@author: Yorhagy
"""

import numpy as np
import matplotlib.pyplot as pyl
import matplotlib.image as im

#%% Imagen Original y gris
carro = im.imread('Placa_Carro.jpg')
p = np.array(carro[:,:,0])
#pyl.figure()
#pyl.imshow(p,cmap= pyl.cm.gray)
#pyl.show()
f,c = np.shape(p)

#%% Tamaño de ventanas
Ancho = np.full((f,c),0)
Largo = np.full((f,c),0)
W_Largo = np.empty((15,3))
W_peq = np.empty((3,3))
W_Ancho = np.empty((3,15))

offset_ancho = 7
offset_alto = 1

#%% Ventana ancha
for fila in range(offset_alto,f):
    for columna in range(offset_ancho,c-offset_ancho+1):
        W_Ancho = p[fila-offset_alto:fila+offset_alto, columna-offset_ancho:columna+offset_ancho]
        W_peq = p[fila-offset_alto:fila+offset_alto, columna-offset_alto:columna+offset_alto]
        Mean_Ancho = np.mean(W_Ancho)/np.mean(W_peq)
        Ancho[fila,columna] = Mean_Ancho >= 1.5        
#pyl.figure()
#pyl.imshow(Ancho)
        
#%% Ventana Larga
for fila in range(offset_ancho-1,f-offset_ancho+1):
    for columna in range(offset_alto,c-offset_alto+1):
        W_Largo = p[fila-offset_ancho+1:fila+offset_ancho, columna-offset_alto:columna+offset_alto]
        W_peq = p[fila-offset_alto:fila+offset_alto, columna-offset_alto:columna+offset_alto]
        Mean_Largo = np.mean(W_Largo)/np.mean(W_peq)
        Largo[fila,columna] = Mean_Largo >= 1.6
        
#pyl.figure()
#pyl.imshow(Largo)
        
#%%
n_carro = np.logical_or(Ancho,Largo) 
#pyl.figure()
#pyl.imshow(n_carro)
#pyl.show()

#%% convertir la matriz en 0 y 1
ncarro = np.full((f,c),0)
for m in range(f):
    for n in range(c):
        ncarro[m,n] = int(n_carro[m,n])

    

    


















