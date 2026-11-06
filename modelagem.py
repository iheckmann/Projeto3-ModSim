from scipy.integrate import odeint
from math import *
import numpy as np
import matplotlib.pyplot as plt

#PARÂMETROS
m = 0.5 #massa do bloco (kg)
mu = 0.3 #coeficiente de atrito cinético
L = 1.0 #comprimento da mesa (m)
h = 0.8 #altura da mesa (m)
v0 = 3.0 #velocidade inicial (m/s)
p = 1.225 #densidade do ar (kg/m3)
Cd = 1.05 #coeficiente de arrasto
A = 0.01 #área da seção transversal (m2)
g = 9.81 #aceleração da gravidade (m/s2)

#MODELO
def modelo(X, t):
    x = X[0]
    y = X[1]
    vx = X[2]
    vy = X[3]

    v = sqrt(vx**2 + vy**2)

    #Forças
    P = m * g
    if x <= L:          #fase 1 (mesa)
        N = P
    else:               #fase 2 (queda)
        N = 0
    Fat = mu * N
    Far = (1/2) * p * A * Cd * v**2

    #Bloco parou na mesa
    if N > 0 and vx <= 0:
        return 0, 0, 0, 0

    #Direção da velocidade
    if v > 0:
        cos_a = vx / v
        sen_a = vy / v
    else:
        cos_a = 0
        sen_a = 0

    #Resultante
    Rx = -Fat - Far * cos_a
    Ry = N - P - Far * sen_a

    dxdt = vx
    dydt = vy
    dvxdt = Rx / m
    dvydt = Ry / m
    dXdt = [dxdt, dydt, dvxdt, dvydt]
    return dXdt
    

#CONDIÇÕES INICIAIS + SIMULAÇÃO DO MODELO
lista_t = np.arange(0, 3, 1e-3) #ver quantos segundos o bloco leva para cair da mesa
CI = [0, h, v0, 0]
solucao = odeint(modelo, CI, lista_t)
lista_x = solucao[:, 0]
lista_y = solucao[:, 1]
lista_vx = solucao[:, 2]
lista_vy = solucao[:, 3]

plt.figure(figsize=(5, 5))
plt.title("Trajetória $y(x)$", fontsize=16)
plt.plot(lista_x, lista_y)
plt.axvline(L, linestyle="--", color="purple")
plt.ylabel("y (m)", fontsize=14)
plt.xlabel("x (m)", fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.grid()
plt.show()

plt.figure(figsize=(5, 5))
plt.title("$v_x(t)$", fontsize=16)
plt.plot(lista_t, lista_vx)
plt.ylabel("Velocidade (m/s)", fontsize=14)
plt.xlabel("t (s)", fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.grid()
plt.show()

plt.figure(figsize=(5, 5))
plt.title("$v_y(t)$", fontsize=16)
plt.plot(lista_t, lista_vy)
plt.ylabel("Velocidade (m/s)", fontsize=14)
plt.xlabel("t (s)", fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.grid()
plt.show()

#IMPORTAÇÃO DOS DADOS EXPERIMENTAIS


#GRÁFICO DA VALIDAÇÃO


#QUALIDADE DA VALIDAÇÃO


#GRÁFICO CONCLUSIVO

