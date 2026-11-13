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

#CONDIÇÕES INICIAIS + SIMULAÇÃO DO MODELO
tf = 2
dt = 0.0001
lista_t = np.arange( 0 , tf , dt )

CI = [ - R , R , 0 , 0 ]
solucao = odeint( modelo, CI, lista_t )

lista_x = solucao[:,0]
lista_y = solucao[:,1]

plt.plot(lista_x, lista_y)
plt.plot( [ R / sqrt(2) ] , [R - R / sqrt(2)] , 'ro' )
plt.title('Trajetória do bloco')
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.grid()
plt.axis('equal')

#TRAJETÓRIA DO BLOCO (COM E SEM ATRITO)
# SEU CÓDIGO DO ITEM 2A

# 2a iteracao
def modelo2(lista,t,u):
    x = lista[0]
    y = lista[1]
    vx = lista[2]
    vy = lista[3]

    cos_theta = (R - y) / R
    sen_theta = x / R

    if x > R*sqrt(2)/2 :
        N = 0
        A = 0
    else:
        N = m * g * cos_theta + m * ( vx**2 + vy**2 ) / R
        A = u * N
       
    dxdt = vx
    dydt = vy
    
    dvxdt = (- N * sen_theta - A * cos_theta) / m
    dvydt = (N * cos_theta - A * sen_theta) / m - g

    derivadas = [ dxdt , dydt , dvxdt , dvydt ]
    return derivadas

solucao2 = odeint( modelo2, CI, lista_t , args=(0.15,))
lista_x2 = solucao2[:,0]
lista_y2 = solucao2[:,1]

plt.plot(lista_x, lista_y, label = 'Sem atrito')
plt.plot(lista_x2, lista_y2, label = 'Com atrito')
plt.plot( [ R / sqrt(2) ] , [1 - R / sqrt(2)] , 'ro' )
plt.title('Trajetória do bloco')
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.grid()
plt.axis('equal')
plt.legend()
plt.show()