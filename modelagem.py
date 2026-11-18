import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from math import *

m = 0.013
g = 9.81
R = 0.13

# Centro do círculo deslocado 1,5 cm para a direita
xc = - 0.015

# Ponta da rampa: abertura de 45°
x_saida = xc + R*sqrt(2)/2
y_saida = R - R/sqrt(2)
def modelo(lista, t):
    x = lista[0]
    y = lista[1]
    vx = lista[2]
    vy = lista[3]

    cos_theta = (R - y) / R
    sen_theta = (x - xc) / R

    v = sqrt(vx**2 + vy**2)

    if x > x_saida:
        N = 0
    else:
        N = m*g*cos_theta + m*v**2/R

    dxdt = vx
    dydt = vy
    dvxdt = -N*sen_theta/m
    dvydt = N*cos_theta/m - g

    derivadas = [dxdt, dydt, dvxdt, dvydt]
    return derivadas
# SEU CÓDIGO DO ITEM 1C

tf = 0.6

dt = 0.0001
lista_t = np.arange(0, tf, dt)

CI = [xc - R, R, 0, -2.77]

solucao = odeint(modelo, CI, lista_t)

lista_x = solucao[:, 0]
lista_y = solucao[:, 1]

plt.plot(lista_x, lista_y)
plt.plot([xc + R/sqrt(2)], [R - R/sqrt(2)], 'ro')
plt.title('Trajetória do bloco')
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.grid()
plt.axis('equal')
def modelo2(lista, t, u):
    x = lista[0]
    y = lista[1]
    vx = lista[2]
    vy = lista[3]

    cos_theta = (R - y) / R
    sen_theta = (x - xc) / R

    v = sqrt(vx**2 + vy**2)

    # Velocidade na direção da rampa
    v_tangencial = vx*cos_theta + vy*sen_theta

    if x > x_saida:
        N = 0
        A = 0

    # Se parar depois do meio da rampa, não deixa voltar
    elif x >= xc and v_tangencial <= 0.01:
        return [0, 0, 0, 0]

    else:
        N = m*g*cos_theta + m*v**2/R
        A = u*N

    dxdt = vx
    dydt = vy

    dvxdt = (-N*sen_theta - A*cos_theta)/m
    dvydt = (N*cos_theta - A*sen_theta)/m - g

    derivadas = [dxdt, dydt, dvxdt, dvydt]
    return derivadas

solucao2 = odeint( modelo2, CI, lista_t , args=(0.15,))
lista_x2 = solucao2[:,0]
lista_y2 = solucao2[:,1]

plt.plot(lista_x, lista_y, label = 'Sem atrito')
plt.plot(lista_x2, lista_y2, label = 'Com atrito')
plt.plot([x_saida], [y_saida], 'ro')
plt.title('Trajetória do bloco')
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.grid()
plt.axis('equal')
plt.legend()
plt.show()
def ymax(lista_x, lista_y):
    lista_y_depois_meio = []

    for i in range(len(lista_x)):
        if lista_x[i] >= xc:
            lista_y_depois_meio.append(lista_y[i])

    return max(lista_y_depois_meio)
    print('Sem atrito:')
print(ymax(lista_x, lista_y))

print('Com atrito:')
print(ymax(lista_x2, lista_y2))
# ModSim Videoanálise: WhatsApp Video 2026-11-10 at 18.12.16.mp4
# t em s; x e y em m; 80 pontos
lista_t_exp = [
    0.0, 0.004171, 0.008342, 0.012513, 0.016683, 0.025025, 0.033367, 0.041708,
    0.05005, 0.058392, 0.066733, 0.075075, 0.083417, 0.091758, 0.1001, 0.108442,
    0.116783, 0.125125, 0.133467, 0.141808, 0.15015, 0.158492, 0.166834, 0.175175,
    0.183517, 0.191859, 0.2002, 0.208542, 0.216884, 0.225225, 0.233567, 0.241909,
    0.25025, 0.258592, 0.266934, 0.275275, 0.283617, 0.291959, 0.3003, 0.308642,
    0.316984, 0.325325, 0.333667, 0.342009, 0.35035, 0.358692, 0.367034, 0.375375,
    0.383717, 0.392059, 0.4004, 0.408742, 0.417084, 0.425425, 0.433767, 0.442109,
    0.45045, 0.458792, 0.467134, 0.475475, 0.483817, 0.492159, 0.500501, 0.508842,
    0.517184, 0.525526, 0.533867, 0.542209, 0.550551, 0.558892, 0.567234, 0.575576,
    0.583917, 0.592259, 0.600601, 0.608942, 0.617284, 0.625626, 0.633967, 0.642309,
]
lista_x_exp = [
    -0.1018, -0.0942, -0.0866, -0.0788, -0.0723, -0.0547, -0.0378, -0.0186,
    0.0002, 0.0161, 0.033, 0.0496, 0.0672, 0.0801, 0.0913, 0.1003,
    0.1083, 0.1174, 0.1255, 0.1356, 0.1437, 0.1549, 0.1641, 0.175,
    0.1869, 0.1954, 0.2056, 0.2141, 0.2272, 0.2392, 0.2495, 0.259,
    0.266, 0.2735, 0.2818, 0.2885, 0.2944, 0.3006, 0.3086, 0.3161,
    0.324, 0.3328, 0.3408, 0.3492, 0.3572, 0.3644, 0.3707, 0.3804,
    0.3897, 0.3982, 0.405, 0.4152, 0.4216, 0.4309, 0.4399, 0.4488,
    0.459, 0.4692, 0.4802, 0.4912, 0.5013, 0.5087, 0.5201, 0.5282,
    0.5358, 0.542, 0.547, 0.557, 0.5669, 0.5741, 0.5831, 0.5928,
    0.6022, 0.6097, 0.6198, 0.6288, 0.6424, 0.6528, 0.6622, 0.6709,
]
lista_y_exp = [
    0.0507, 0.042, 0.0344, 0.0285, 0.0233, 0.013, 0.0051, 0.0001,
    0.0011, 0.0021, 0.0042, 0.0091, 0.0154, 0.027, 0.0357, 0.0443,
    0.0515, 0.0574, 0.0628, 0.0701, 0.0748, 0.0817, 0.0851, 0.0895,
    0.0922, 0.0945, 0.0971, 0.0983, 0.1005, 0.1003, 0.0997, 0.0966,
    0.0926, 0.0882, 0.0834, 0.0778, 0.0721, 0.0669, 0.0604, 0.0531,
    0.0455, 0.0366, 0.0276, 0.0179, 0.0086, -0.0024, -0.0126, -0.0239,
    -0.0402, -0.0545, -0.0696, -0.085, -0.1001, -0.1148, -0.1331, -0.1515,
    -0.1661, -0.1853, -0.2024, -0.2207, -0.2426, -0.2605, -0.2848, -0.3053,
    -0.3323, -0.356, -0.3761, -0.4002, -0.4249, -0.4513, -0.4791, -0.5062,
    -0.5351, -0.5619, -0.5907, -0.6203, -0.6509, -0.6804, -0.7114, -0.7396,
]
# Condições iniciais iguais às do experimento
CI_exp = [lista_x_exp[0], lista_y_exp[0], 1.82, -2.09]

# O que varia
u = 0.19

# Calcula o modelo nos mesmos instantes do vídeo
solucao3 = odeint(modelo2, CI_exp, lista_t_exp, args=(u,))

lista_x3 = solucao3[:, 0]
lista_y3 = solucao3[:, 1]

# Gráfico de validação: modelo e experimento
plt.plot(lista_x3, lista_y3, label=f'Modelo com μ = {u}')
plt.plot(lista_x_exp, lista_y_exp, 'rx', label='Experimental')
plt.plot([x_saida], [y_saida], 'ro', label='Ponta da rampa')

plt.title('Modelo com atrito e dados experimentais')
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.grid()
plt.axis('equal')
plt.legend()
plt.show()
# SEU CÓDIGO DO ITEM 2D

lista_u = np.arange(0, 0.51, 0.02)

for u in lista_u:
    solucao = odeint(modelo2, CI, lista_t, args=(u,))

    lista_x = solucao[:, 0]
    lista_y = solucao[:, 1]

    plt.plot(lista_x, lista_y)

plt.plot([x_saida], [y_saida], 'ro', label='Ponta da rampa')

plt.title('Influência de μ na trajetória do bloco')
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.grid()
plt.axis('equal')
plt.legend()
plt.show()
