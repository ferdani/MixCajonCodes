#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 11:48:34 2019

@author: Daniel Fernandez Fernandez
dani.fernandez@usc.es

EVALUAR EL NUMERO DE LADRILLOS DE LEGO QUE SON NECESARIOS PARA PODER CONSTRUIR LA CARTA DE NUCLEOS
ADEMAS DEL NUMERO DE COLORES Y LADRILLOS POR COLOR. ESE COLOR REPRESENTA EL DECAY:

EVALUATE THE NUMBER OF LEGO BRICKS THAT ARE NECESSARY TO BE ABLE TO BUILD THE NUCLEUS CHART
IN ADDITION TO THE NUMBER OF COLORS AND BRICKS BY COLOR. THAT COLOR REPRESENTS THE DECAY:
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
from mpl_toolkits.mplot3d import Axes3D

"""
---------------- Read the data from .txt downloaded from NNDC ---------------------------
"""

Data_path = './'
Data_name = 'Mass_Binding.txt'

dtype1 = np.dtype([('N', 'f'),
                  ('Z', 'f'),
                  ('A', 'f'),
                  ('El', '<U8'),
                  ('Mass_excess', 'f16'),
                  ('Binding_energy_A', 'f16'),
                  ('Decay_Channel', '<U16')])

file_data = np.loadtxt(Data_path + Data_name, dtype=dtype1, skiprows=1, usecols=(0,1,2,3,4,5,6))

N = file_data['N'] #neutrons
Z = file_data['Z'] #electrons
A = file_data['A'] #Atomic mass
El = file_data['El'] #Elements
Mass_excess = file_data['Mass_excess'] #mass excess
Binding_A = file_data['Binding_energy_A'] #binding energy divided A
Decay_Channel = file_data['Decay_Channel'] #decay channel

'''
--------------------- bricks number calculation --------------------------------------
Two types of LEGO bricks: 1x1 de 1cm height (REF-LEGO: 3005) y 1x1 de 0.33 cm height (REF-LEGO:3024)
'''

MassExcess_over_A = np.array([])
MassExcess_over_A_corrected = np.array([])
Bricks_nucleo = [[0.0]] #this will be the number of bricks per nucleus

#For all the elements we evaluate the ratio of mass excess over A
for i in range(0, len(El)):
   ratio = Mass_excess[i]/A[i]
   MassExcess_over_A = np.append(MassExcess_over_A, ratio)

Offset_groundfloor = abs(min(MassExcess_over_A)) #in absolit value because the minimum was negative
#For all the elements this Offset_groundfloor is added, starting from zero

#indice_min = np.argmin(MassExcess_over_A)
#indice_max = np.argmax(MassExcess_over_A)

for i in range(0, len(El)):
   MassExcess_over_A_corrected = np.append(MassExcess_over_A_corrected, Offset_groundfloor + MassExcess_over_A[i])

#Now a number of bricks (cm) is awarded to the maximum, this will be the highest value of the columns that the core chart will have
Fixed_max_cm = 95 #cm
#Now you put a minimum of bricks to put the zero (if it is set to zero there will be elements touching the base)
Offset_bricks = 5 #bricks = cm

for i in range(0, len(El)):
   cm_evaluated = MassExcess_over_A_corrected[i] * Fixed_max_cm / max(MassExcess_over_A_corrected)
   #we award 1cm to 1-brick, whichever is decimal will be awarded to the brick of 0.33cm
   Bricks_nucleo_integer = cm_evaluated // 1
   Bricks_nucle_decimal = cm_evaluated % 1

   bb = [Bricks_nucleo_integer + Offset_bricks, (Bricks_nucle_decimal/0.33) // 1]
   Bricks_nucleo.append(bb)

del Bricks_nucleo[0] #delete the first element that is a zero set as an initializer before

'''
--------------------- calculate number of colored bricks --------------------------------------
There are 7 colors, one for decay, and two types of bricks
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
      a = [Bricks_nucleo[i][0], Bricks_nucleo[i][1]] #bricks of 1x1 of 1 cm , bricks of 1x1 of 0.33 cm
      Bminus_color.append(a)
   if Decay_Channel[i] == 'Bplus':
      b = [Bricks_nucleo[i][0], Bricks_nucleo[i][1]] #bricks of 1x1 of 1 cm , bricks of 1x1 of 0.33 cm
      Bplus_color.append(b)
   if Decay_Channel[i] == 'N':
      c = [Bricks_nucleo[i][0], Bricks_nucleo[i][1]] #bricks of 1x1 of 1 cm , bricks of 1x1 of 0.33 cm
      N_color.append(c)
   if Decay_Channel[i] == 'P':
      d = [Bricks_nucleo[i][0], Bricks_nucleo[i][1]] #bricks of 1x1 of 1 cm , bricks of 1x1 of 0.33 cm
      P_color.append(d)
   if Decay_Channel[i] == 'SF':
      e = [Bricks_nucleo[i][0], Bricks_nucleo[i][1]] #bricks of 1x1 of 1 cm , bricks of 1x1 of 0.33 cm
      SF_color.append(e)
   if Decay_Channel[i] == 'Stable':
      f = [Bricks_nucleo[i][0], Bricks_nucleo[i][1]] #bricks of 1x1 of 1 cm , bricks of 1x1 of 0.33 cm
      Stable_color.append(f)
   if Decay_Channel[i] == 'alpha':
      g = [Bricks_nucleo[i][0], Bricks_nucleo[i][1]] #bricks of 1x1 of 1 cm , bricks of 1x1 of 0.33 cm
      alpha_color.append(g)

del Bminus_color[0] #delete the first element that is a zero set as an initializer before
del Bplus_color[0] #delete the first element that is a zero set as an initializer before
del N_color[0] #delete the first element that is a zero set as an initializer before
del P_color[0] #delete the first element that is a zero set as an initializer before
del SF_color[0] #delete the first element that is a zero set as an initializer before
del Stable_color[0] #delete the first element that is a zero set as an initializer before
del alpha_color[0] #delete the first element that is a zero set as an initializer before

'''
#--------------------- Final evaluation of bricks and price --------------------------------------
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


print('Bricks red color beta_menos decay, large ', rojo_grande, ' and little ', rojo_peque)
print('Bricks blue color beta_mas decay, large ', azul_grande, ' and little ', azul_peque)
print('Bricks yellow color alpha decay, large ', amarillo_grande, ' and little ', amarillo_peque)
print('Bricks black color stable, large ', negro_grande, ' and little ', negro_peque)
print('Bricks green color spontaneus fission decay, large ', verde_grande, ' and little ', verde_peque)
print('Bricks violet color neutron decay, large ', violeta_grande, ' and little ', violeta_peque)
print('Bricks orange color proton decay, large ', naranja_grande, ' and little ', naranja_peque)
print('-----------------------------------------------------------------------------------')
print('Quantity large bricks ', rojo_grande + azul_grande + amarillo_grande + negro_grande + verde_grande + violeta_grande + naranja_grande)
print('Quantity small bricks ', rojo_peque + azul_peque + amarillo_peque + negro_peque + verde_peque + violeta_peque + naranja_peque)
print('-----------------------------------------------------------------------------------')
Price_grandes = (rojo_grande + azul_grande + amarillo_grande + negro_grande + verde_grande + violeta_grande + naranja_grande)*0.07
Price_peques = (rojo_peque + azul_peque + amarillo_peque + negro_peque + verde_peque + violeta_peque + naranja_peque)*0.04
print('Price with average 0.07 euros/large_brick ', Price_grandes)
print('Price with average 0.04 euros/little_brick ', Price_peques)
Price_Total = Price_grandes + Price_peques
print('TOTAL: ', Price_Total)

'''
--------------------- Isobaric representation of A  ------------
'''

#A chosen to represent:
A_choosen = 60.0

Isobar_array_N = np.array([])
Isobar_array_Z = np.array([])
Isobar_array_Bricks_big = np.array([])
Isobar_array_Bricks_small = np.array([])
Isobar_array_elements = np.array([])

for i in range(0, len(A)):
   if A[i] == A_choosen:
      Isobar_array_N = np.append(Isobar_array_N, N[i])
      Isobar_array_Z = np.append(Isobar_array_Z, Z[i])
      Isobar_array_Bricks_big = np.append(Isobar_array_Bricks_big, Bricks_nucleo[i][0])
      Isobar_array_Bricks_small = np.append(Isobar_array_Bricks_small, Bricks_nucleo[i][1])
      Isobar_array_elements = np.append(Isobar_array_elements, El[i])

#Building the representation
fig=plt.figure(figsize=(12,6))
fig.subplots_adjust(top=0.90, bottom=0.10, hspace=0.5, wspace=0.25)

ax=fig.add_subplot(1,2,1)
ax.set_title('Bricks for A = %s isobara' %A_choosen, fontsize=15)
ax.set_ylabel(r'Height [cm]', fontsize=12)
ax.set_xlabel(r'N', fontsize=12)
plt.stackplot(Isobar_array_N, Isobar_array_Bricks_big, Isobar_array_Bricks_small * 0.33, labels=['Big-Bricks','Small-Bricks'])
plt.grid(True)
plt.legend(loc = 'upper center')

ax_1=fig.add_subplot(1,2,2)
ax_1.set_title('Bricks for A = %s isobara' %A_choosen, fontsize=15)
ax_1.set_ylabel(r'Height [cm]', fontsize=12)
ax_1.set_xlabel(r'Z', fontsize=12)
plt.stackplot(Isobar_array_Z, Isobar_array_Bricks_big, Isobar_array_Bricks_small * 0.33, labels=['Big-Bricks','Small-Bricks'])
plt.grid(True)
plt.legend(loc = 'upper center')

'''
--------------------- Z - N - Mass excess over A (in log plane) Nucleus Chart plot ---------------
'''

fig_2 = plt.figure()
ax=fig_2.add_subplot(1,1,1)
plt.scatter(N,Z,c=np.log(MassExcess_over_A_corrected), marker='o', cmap='viridis')
plt.colorbar()
ax.set_title('Nucleus chart (arbitrary units)', fontsize=15)
ax.set_ylabel(r'Z', fontsize=12)
ax.set_xlabel(r'N', fontsize=12)


'''
--------------------- Nucleus Chart 3d ------------------------------
'''

# Create the work space
fig_3 = plt.figure()
plt.ioff() #inline mode off
ax = fig_3.add_subplot(111, projection='3d')

#plt.rcParams['agg.path.chunksize'] = 1000 #If exist a problem doing zoom is here with chunks. It works with TkAgg matplotlib backend

# Make histogram stuff with numpy in 2d
H, xedges, yedges = np.histogram2d(N, Z, bins=(178,119), weights=np.float32(MassExcess_over_A_corrected))

#make a mesh between points
xpos, ypos = np.meshgrid(xedges[:-1]+xedges[1:], yedges[:-1]+yedges[1:])

# H needs to be rotated and flipped
H = np.rot90(H)
H = np.flipud(H)

xpos = xpos.flatten()/2.
ypos = ypos.flatten()/2.
zpos = np.zeros_like(xpos)

dx = xedges [1] - xedges [0]
dy = yedges [1] - yedges [0]
dz = H.flatten()

cmap = plt.cm.get_cmap('YlOrRd') # Get desired colormap - you can change this!
max_height = np.max(dz)   # get range of colorbars so we can normalize
min_height = np.min(dz)
# scale each z to [0,1], and get their rgb values
rgba = [cmap((k-min_height)/max_height) for k in dz]

ax.bar3d(xpos, ypos, zpos, dx, dy, dz, color=rgba, zsort='average')

#ax.autoscale(enable=True, axis='both', tight=False)
#ax.set_zlabel('Counts', fontsize=15)

plt.show()

'''
------------------------------------------------------ Builder time -------------------------------------------------
'''

def nucleide_data(number):
    print('Name: ', El[number])
    print('Atomic mass: ', A[number])
    if Decay_Channel[number] == 'Bminus': color_print = 'red'
    elif Decay_Channel[number] == 'Bplus': color_print = 'blue'
    elif Decay_Channel[number] == 'N': color_print = 'violet'
    elif Decay_Channel[number] == 'P': color_print = 'orange'
    elif Decay_Channel[number] == 'SF': color_print = 'green'
    elif Decay_Channel[number] == 'Stable': color_print = 'black'
    elif Decay_Channel[number] == 'alpha': color_print = 'yellow'
    else:
        print('Warning, problem with decay')
        color_print = 'Warning¡'

    print('Decay channel: ', Decay_Channel[number], ' --> Color: ', color_print)
    print('Bricks --> [Big, Small] ', Bricks_nucleo[number])

    return None
