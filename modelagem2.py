import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from math import *

#PARÂMETROS
m = 1
g = 9.81
R = 1

#MODELO
def modelo(lista,t):
    x = lista[0]
    y = lista[1]
    vx = lista[2]
    vy = lista[3]

    cos_theta = (R - y) / R
    sen_theta = x / R

    v = sqrt(vx**2 + vy**2)

    if x > R*sqrt(2)/2 :
        N = 0
    else:
        N = m * g * cos_theta + m * v ** 2 / R

    dxdt = vx
    dydt = vy
    dvxdt = - N * sen_theta / m
    dvydt = N * cos_theta / m - g

    derivadas = [ dxdt , dydt , dvxdt , dvydt ]
    return derivadas