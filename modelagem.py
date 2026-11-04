from scipy.integrate import odeint
from math import *
import numpy as np
import matplotlib.pyplot as plt

#PARÂMETROS
m = #massa do bloco (kg)
g = 9.81 #aceleração da gravidade (m/s²)
v0 = #velocidade inicial (m/s)
L = #comprimento do plano (m)
h = #altura do plano em relação ao chão (m)
k = #coeficiente de atrito (adimensional)
p = 1.225 # densidade do ar (kg/m3)
A = #área de seção transversal do bloco (m²)
Cd = #coeficiente de resistência do ar (adimensional)

#MODELO

def modelo(X, t):
    x = X[0] #posição (m)
    vx = X[1] #velocidade (m/s)
    y = X[2] #altura (m)
    vy = X[3] #velocidade vertical (m/s)

    dxdt = vx
    dvxdt = -k/m - (1/(2*m)) * p * Cd * A * vx**2
    dydt = vy
    dvydt = -g - (1/(2*m)) * p * Cd * A * vy**2
    dXdt = [dxdt, dvxdt, dydt, dvydt]
    return dXdt
    

#CONDIÇÕES INICIAIS + SIMULAÇÃO DO MODELO
lista_t = np.arange(0, 10, 0.1) #tempo de simulação (s)
CI = [0, v0, h, 0] #condições iniciais --> ADICIONAR A ALTURA DA MESA
solucao = odeint(modelo, CI, lista_t) #solução do modelo
lista_x = solucao[:, 0] #posição (m)
lista_vx = solucao[:, 1] #velocidade (m/s)
lista_y = solucao[:, 2] #altura (m)
lista_vy = solucao[:, 3] #velocidade vertical (m/s)

plt.figure()
plt.plot(lista_t, lista_x, label='Posição (m)')
plt.plot(lista_t, lista_y, label='Altura (m)')
plt.title('Simulação do Modelo')
plt.xlabel('Tempo (s)')
plt.ylabel('Posição (m)')
plt.legend()
plt.grid()
plt.show()

plt.figure()
plt.plot(lista_t, lista_vx, label='Velocidade Horizontal(m/s)')
plt.plot(lista_t, lista_vy, label='Velocidade Vertical (m/s)')
plt.title('Simulação do Modelo')
plt.xlabel('Tempo (s)')
plt.ylabel('Velocidade (m/s)')
plt.legend()
plt.grid()
plt.show()

#IMPORTAÇÃO DOS DADOS EXPERIMENTAIS


#GRÁFICO DA VALIDAÇÃO


#QUALIDADE DA VALIDAÇÃO


#GRÁFICO CONCLUSIVO

