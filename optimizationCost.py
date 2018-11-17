#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 07:31:21 2018

@author: yorhagy
"""
import numpy as np
from scipy.optimize import minimize

def precio(demanda, t, A, B, D):
    return (A - B * demanda) * ((D + t) / D)

def ingreso(demanda, precio):
    return np.sum(demanda * precio)
    
def objetive(x):
    demanda = x[0]
    return -ingreso(demanda, precio(demanda, t, A, B, D))

def constraint(x):
    demanda = x[0]
    return demanda

constrts = [{'type':'ineq', 'fun':constraint}]

t = np.arange(6, 18)
A, B, D = 200, 10, 10

demandaIdeal = minimize(objetive, [200], method='SLSQP', constraints=constrts)

if demandaIdeal['success'] :
    print('La demanda ideal es ideal: ', demandaIdeal['x'][0])
else :
    print('No se encontro un resultado optimo ')
    
