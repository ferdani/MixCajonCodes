#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 11:48:34 2019

@author: Daniel Fernandez Fernandez
daniel.fernandez.fernandez.94@gmail.com

EVALUAR EL NUMERO DE LADRILLOS DE LEGO QUE SON NECESARIOS PARA PODER CONSTRUIR LA CARTA DE NUCLEOS
ADEMAS DEL NUMERO DE COLORES Y LADRILLOS POR COLOR. ESE COLOR REPRESENTA EL DECAY:
A --> alpha
Bplus --> Beta decay +
Bminus --> Beta decay -
N --> Neutron
Stable --> Stability
SF --> Spontaneus Fission
P --> Proton
x --> Unknown
xx --> Doesn't exist in NNDC NuDat2.7
"""

import numpy as np
import math
import matplotlib
import matplotlib.pyplot as plt

"""
---------------- Leer los datos del .txt descargado del NNDC ---------------------------
"""

Data_path = '/Users/macbookpro/Dani/INVESTIGACIÓN/ProyectosDivulgacion/LEGO-IGFAE/CartaNucelar/'
Data_name = 'Mass_Binding.txt'

dtype1 = np.dtype([('N', 'f'),
                  ('Z', 'f'),
                  ('A', 'f'),
                  ('El', '<U8'),
                  ('Mass_excess', 'f16'),
                  ('Binding_energy_A', 'f16'),
                  ('Decay_Channel', '<U16')])

file_data = np.loadtxt(Data_path + Data_name, dtype=dtype1, skiprows=1, usecols=(0,1,2,3,4,5,6))

N = file_data['N'] #neutrones
Z = file_data['Z'] #electrones
A = file_data['A'] #Atomic mass
El = file_data['El'] #Element
Mass_excess = file_data['Mass_excess'] #exceso de masa
Binding_A = file_data['Binding_energy_A'] #energia ligadura dividida por A
Decay_Channel = file_data['Decay_Channel'] #canal desintegracion

'''
--------------------- calcular numero de ladrillos --------------------------------------
Dos tipos de bloque LEGO: 1x1 de 1cm de alto (REF-LEGO: 3005) y 1x1 de 0.33 cm de alto (REF-LEGO:3024)
'''

MassExcess_over_A = np.array([])
MassExcess_over_A_corrected = np.array([])
Bricks_nucleo = [[0.0]] #este será el numero de bricks por nucleo

#Para todos los elementos evaluamos el ratio del exceso de masa sobre A
for i in range(0, len(El)):
   ratio = Mass_excess[i]/A[i]
   MassExcess_over_A = np.append(MassExcess_over_A, ratio)

Offset_groundfloor = abs(min(MassExcess_over_A)) #en absoluto porque el minimo esta en un valor negativo
#Para todos los elementos se les suma este Offset_groundfloor haciendo que empiecen desde cero

#indice_min = np.argmin(MassExcess_over_A)
#indice_max = np.argmax(MassExcess_over_A)

for i in range(0, len(El)):
   MassExcess_over_A_corrected = np.append(MassExcess_over_A_corrected, Offset_groundfloor + MassExcess_over_A[i])

#Ahora se adjudica al máximo un numero de ladrillos (cm), este será el valor mas alto de las columnas que tendrá la carte de nucleos
Fixed_max_cm = 95 #cm
#Ahora se pone un mínimo de bricks para poner el cero (si se pone en cero habrá elementos tocando la base)
Offset_bricks = 5 #bricks = cm

for i in range(0, len(El)):
   cm_evaluated = MassExcess_over_A_corrected[i] * Fixed_max_cm / max(MassExcess_over_A_corrected)
   #adjudicamos 1-cm a 1-brick, lo que sea decimal se adjudicará al brick de 0.33-cm
   Bricks_nucleo_integer = cm_evaluated // 1
   Bricks_nucle_decimal = cm_evaluated % 1

   bb = [Bricks_nucleo_integer + Offset_bricks, (Bricks_nucle_decimal/0.33) // 1]
   Bricks_nucleo.append(bb)

del Bricks_nucleo[0] #eliminar el primer elemento que es un cero puesto como inicializador antes

'''
--------------------- calcular numero de ladrillos de colores --------------------------------------
Hay 7 colores, uno por decay, y dos tipos de ladrillos
'''

Bminus_color = [[0.0]] #numero de bloques necesarios de cada tipo del color concreto del Bminus decay
Bplus_color = [[0.0]] #numero de bloques necesarios de cada tipo del color concreto del Bplus decay
N_color = [[0.0]] #numero de bloques necesarios de cada tipo del color concreto del N decay
P_color = [[0.0]] #numero de bloques necesarios de cada tipo del color concreto del P decay
SF_color = [[0.0]] #numero de bloques necesarios de cada tipo del color concreto del SF decay
Stable_color = [[0.0]] #numero de bloques necesarios de cada tipo del color concreto del Stable
alpha_color = [[0.0]] #numero de bloques necesarios de cada tipo del color concreto del alpha decay

for i in range(0, len(Decay_Channel)):
   if Decay_Channel[i] == 'Bminus':
      a = [Bricks_nucleo[i][0], Bricks_nucleo[i][1]] #bloques de 1x1 de 1 cm , bloques de 1x1 de 0.33 cm
      Bminus_color.append(a)
   if Decay_Channel[i] == 'Bplus':
      b = [Bricks_nucleo[i][0], Bricks_nucleo[i][1]] #bloques de 1x1 de 1 cm , bloques de 1x1 de 0.33 cm
      Bplus_color.append(b)
   if Decay_Channel[i] == 'N':
      c = [Bricks_nucleo[i][0], Bricks_nucleo[i][1]] #bloques de 1x1 de 1 cm , bloques de 1x1 de 0.33 cm
      N_color.append(c)
   if Decay_Channel[i] == 'P':
      d = [Bricks_nucleo[i][0], Bricks_nucleo[i][1]] #bloques de 1x1 de 1 cm , bloques de 1x1 de 0.33 cm
      P_color.append(d)
   if Decay_Channel[i] == 'SF':
      e = [Bricks_nucleo[i][0], Bricks_nucleo[i][1]] #bloques de 1x1 de 1 cm , bloques de 1x1 de 0.33 cm
      SF_color.append(e)
   if Decay_Channel[i] == 'Stable':
      f = [Bricks_nucleo[i][0], Bricks_nucleo[i][1]] #bloques de 1x1 de 1 cm , bloques de 1x1 de 0.33 cm
      Stable_color.append(f)
   if Decay_Channel[i] == 'alpha':
      g = [Bricks_nucleo[i][0], Bricks_nucleo[i][1]]
      alpha_color.append(g)

del Bminus_color[0] #eliminar el primer elemento que es un cero puesto como inicializador antes
del Bplus_color[0] #eliminar el primer elemento que es un cero puesto como inicializador antes
del N_color[0] #eliminar el primer elemento que es un cero puesto como inicializador antes
del P_color[0] #eliminar el primer elemento que es un cero puesto como inicializador antes
del SF_color[0] #eliminar el primer elemento que es un cero puesto como inicializador antes
del Stable_color[0] #eliminar el primer elemento que es un cero puesto como inicializador antes
del alpha_color[0] #eliminar el primer elemento que es un cero puesto como inicializador antes

'''
#--------------------- Evaluacion Final de ladrillos y precio --------------------------------------
'''
rojo_grande = 0.0
rojo_peque = 0.0
azul_grande = 0.0
azul_peque = 0.0
amarillo_grande = 0.0
amarillo_peque = 0.0
negro_grande = 0.0
negro_peque = 0.0
verde_grande = 0.0
verde_peque = 0.0
violeta_grande = 0.0
violeta_peque = 0.0
naranja_grande = 0.0
naranja_peque = 0.0

for i in range(0, len(Bminus_color)):
   rojo_grande = rojo_grande + Bminus_color[i][0]
   rojo_peque = rojo_peque + Bminus_color[i][1]

for i in range(0, len(Bplus_color)):
   azul_grande = azul_grande + Bplus_color[i][0]
   azul_peque = azul_peque + Bplus_color[i][1]

for i in range(0, len(alpha_color)):
   amarillo_grande = amarillo_grande + alpha_color[i][0]
   amarillo_peque = amarillo_peque + alpha_color[i][1]

for i in range(0, len(Stable_color)):
   negro_grande = negro_grande + Stable_color[i][0]
   negro_peque = negro_peque + Stable_color[i][1]

for i in range(0, len(SF_color)):
   verde_grande = verde_grande + SF_color[i][0]
   verde_peque = verde_peque + SF_color[i][1]

for i in range(0, len(N_color)):
   violeta_grande = violeta_grande + N_color[i][0]
   violeta_peque = violeta_peque + N_color[i][1]

for i in range(0, len(P_color)):
   naranja_grande = naranja_grande + P_color[i][0]
   naranja_peque = naranja_peque + P_color[i][1]


print('Ladrillos color rojo beta_menos grandes ', rojo_grande, ' y pequeños ', rojo_peque)
print('Ladrillos color azul beta_mas grandes ', azul_grande, ' y pequeños ', azul_peque)
print('Ladrillos color amarillo alpha grandes', amarillo_grande, ' y pequeños ', amarillo_peque)
print('Ladrillos color negro estables grandes ', negro_grande, ' y pequeños ', negro_peque)
print('Ladrillos color verde fision espontanea grandes ', verde_grande, ' y pequeños ', verde_peque)
print('Ladrillos color violeta neutron grandes ', violeta_grande, ' y pequeños ', violeta_grande)
print('Ladrillos color naranja proton grandes ', naranja_grande, ' y pequeños ', naranja_peque)
print('-----------------------------------------------------------------------------------')
print('Cantidad ladrillos grandes ', rojo_grande + azul_grande + amarillo_grande + negro_grande + verde_grande + violeta_grande + naranja_grande)
print('Cantidad ladrillos pequeños ', rojo_peque + azul_peque + amarillo_peque + negro_peque + verde_peque + violeta_peque + naranja_peque)
print('-----------------------------------------------------------------------------------')
Price_grandes = (rojo_grande + azul_grande + amarillo_grande + negro_grande + verde_grande + violeta_grande + naranja_grande)*0.07
Price_peques = (rojo_peque + azul_peque + amarillo_peque + negro_peque + verde_peque + violeta_peque + naranja_peque)*0.04
print('Precio con 0.07 euros/bloque grande ', Price_grandes)
print('Precio con 0.04 euros/bloque pequeño ', Price_peques)
Price_Total = Price_grandes + Price_peques
print('TOTAL: ', Price_Total)
