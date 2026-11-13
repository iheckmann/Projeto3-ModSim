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

#ALTURA MÁXIMA DO BLOCO (COM E SEM ATRITO)
def ymax( lista_x, lista_y ):
    for i in range( len( lista_x ) ):
        if lista_x[i] > R*sqrt(2)/2 and lista_y[i] > lista_y[i-1] and lista_y[i] > lista_y[i+1]:
            return lista_y[i]
            break

print("Sem atrito:")
print( ymax( lista_x, lista_y ) )
print("Com atrito:")
print( ymax( lista_x2, lista_y2 ) )

#VALIDAÇÃO DO MODELO
# Lista com os instantes t do experimento
lista_t_exp = [0.375375, 0.383717, 0.392059, 0.4004, 0.408742, 0.417084, 0.425425, 0.433767,
    0.442109, 0.45045, 0.458792, 0.467134, 0.475475, 0.483817, 0.492159, 0.500501,
    0.508842, 0.517184, 0.525526, 0.533867, 0.542209, 0.550551, 0.558892, 0.567234,
    0.575576, 0.583917, 0.592259, 0.600601, 0.608942, 0.617284, 0.625626, 0.633967,
    0.642309, 0.650651, 0.658992, 0.667334, 0.675676, 0.684017, 0.692359, 0.700701,
    0.709042, 0.717384, 0.725726, 0.734067, 0.742409, 0.750751, 0.759092, 0.767434,
    0.775776, 0.784117, 0.792459, 0.800801, 0.809142, 0.817484, 0.825826, 0.834168,
    0.842509, 0.850851, 0.859193, 0.867534, 0.875876, 0.884218, 0.892559, 0.900901,
    0.909243, 0.917584, 0.925926, 0.934268, 0.942609, 0.950951, 0.959293, 0.967634,
    0.975976, 0.984318, 0.992659, 1.001001, 1.009343]
# Lista com os valores da posição x(t) do experimento
lista_x_exp = [0.1037, 0.0937, 0.079, 0.0601, 0.0429, 0.0204, 0.0036, -0.0104,
    -0.0276, -0.0462, -0.0597, -0.0742, -0.0874, -0.097, -0.1056, -0.1131,
    -0.1242, -0.1321, -0.1428, -0.1529, -0.1629, -0.1776, -0.1901, -0.1972,
    -0.204, -0.2115, -0.2201, -0.2285, -0.2369, -0.2435, -0.2539, -0.2604,
    -0.2728, -0.2806, -0.2884, -0.2963, -0.3047, -0.3093, -0.3159, -0.326,
    -0.336, -0.3431, -0.3517, -0.3642, -0.3746, -0.3854, -0.3975, -0.4065,
    -0.4147, -0.4215, -0.4326, -0.4401, -0.4463, -0.4553, -0.4671, -0.4778,
    -0.4868, -0.4968, -0.5025, -0.5114, -0.52, -0.5301, -0.5376, -0.5476,
    -0.553, -0.5619, -0.5694, -0.5802, -0.5884, -0.5984, -0.6052, -0.6145,
    -0.6235, -0.6295, -0.6388, -0.6464, -0.6526]
# Lista com os valores da posição y(t) do experimento
lista_y_exp = [0.0717, 0.0535, 0.0424, 0.0313, 0.0238, 0.0181, 0.0185, 0.0174,
    0.0213, 0.026, 0.0303, 0.0391, 0.0494, 0.0572, 0.064, 0.0701,
    0.0783, 0.083, 0.0898, 0.0937, 0.0987, 0.1045, 0.1077, 0.1077,
    0.1073, 0.107, 0.1045, 0.102, 0.0994, 0.0967, 0.0922, 0.0902,
    0.0831, 0.0785, 0.0759, 0.072, 0.0648, 0.0602, 0.0541, 0.0441,
    0.0348, 0.0266, 0.018, 0.0098, -0.001, -0.0117, -0.0271, -0.0411,
    -0.0561, -0.0733, -0.0904, -0.1069, -0.118, -0.1373, -0.1555, -0.1749,
    -0.1971, -0.2128, -0.2325, -0.2543, -0.2776, -0.2983, -0.3209, -0.3481,
    -0.3692, -0.3924, -0.4229, -0.4476, -0.4744, -0.4991, -0.5256, -0.5571,
    -0.5882, -0.619, -0.6494, -0.6787, -0.7079]
# Lista com os valores da velocidade vx(t) do experimento
lista_vx_exp = []
# Lista com os valores da velocidade vy(t) do experimento
lista_vy_exp = []

for i in range(len(lista_x_exp) - 1):
    vx = (lista_x_exp[i+1] - lista_x_exp[i]) / dt
    vy = (lista_y_exp[i+1] - lista_y_exp[i]) / dt
    lista_vx_exp.append(vx)
    lista_vy_exp.append(vy)
    lista_vx_exp.append(lista_vx_exp[-1])
    lista_vy_exp.append(lista_vy_exp[-1])

CI_exp = [ lista_x_exp[0], lista_y_exp[0], lista_vx_exp[0], lista_vy_exp[0] ]

u = 0.06
solucao3 = odeint( modelo2, CI_exp, lista_t , args=(u,))

lista_x3 = solucao3[:,0]
lista_y3 = solucao3[:,1]
lista_vx3 = solucao3[:,2]

plt.plot(lista_x3, lista_y3, label = f"Com u = {u}")
plt.plot(lista_x_exp, lista_y_exp, 'rx', label = 'Experimental')
plt.axis('equal')
plt.title('Trajetória do bloco')
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.grid()
plt.axis('equal')
plt.legend()
plt.show()

plt.plot(lista_t, lista_vx3, label = f"Com u= {u}")
plt.plot(lista_t_exp, lista_vx_exp, 'rx', label = 'Experimental')
plt.title('Trajetória do bloco')
plt.xlabel('t (s)')
plt.ylabel('vx (m/s)')
plt.grid()
plt.legend()
plt.show()


#VERIFICANDO INFLUÊNCIA DO COEFICIENTE DE ATRITO NA TRAJETÓRIA DO BLOCO
lista_u = np.arange( 0 , 0.2, 0.01 )

for u in lista_u :
    solucao = odeint( modelo2, CI, lista_t , args=(u,) )
    lista_x = solucao[:,0]
    lista_y = solucao[:,1]

    plt.plot(lista_x, lista_y)

plt.title('Trajetória do bloco')
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.grid()
plt.axis('equal')
plt.show()