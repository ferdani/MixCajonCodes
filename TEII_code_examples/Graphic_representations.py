#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Monday Sept 2 15:43:00 2019

@author: Daniel Fernandez Fernandez
dani.fernandez@usc.es

DIFFERENT WAYS TO DO A GRAPHIC DATA REPRESENTATION

"""
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from matplotlib import ticker
from scipy import stats

'''---------------------- Data random variables will be used in the plots-------------------------'''
x = np.array(['Class 1', 'Class 2', 'Class 3', 'Class 4', 'Class 5', 'Class 6', 'Class 7', 'Class 8', 'Class 9', 'Class 10'])
y = np.random.randint(low=0, high=10, size=10) #10 random numbers between 0 and 9 inclusive
z = np.random.randint(low=0, high=10, size=10)*10 #Generate 20 random numbers between 0 and 100
"""Create the frequency data"""
Xi, ni = x, y


"""more data random"""
X1 = np.random.normal(loc=20, scale=10, size=1000) #100 random numbers entre 0 y 10
X2 = np.random.normal(loc=-20, scale=10, size=1000) #100 random numbers entre 0 y 10
XX = np.concatenate((X1, X2), axis=None)
Y1 = np.random.normal(loc=20, scale=10, size=1000) #100 random numbers entre 0 y 10
Y2 = np.random.normal(loc=-20, scale=10, size=1000) #100 random numbers entre 0 y 10
YY = np.concatenate((Y1, Y2), axis=None)

xmin = min(XX)
xmax = max(XX)
ymin = min(YY)
ymax = max(YY)

#function to stimate the density of the points, a gaussian type is used.
def density_estimation(m1, m2):
    X, Y = np.mgrid[xmin:xmax:100j, ymin:ymax:100j]
    positions = np.vstack([X.ravel(), Y.ravel()])
    values = np.vstack([m1, m2])
    kernel = stats.gaussian_kde(values)
    Z = np.reshape(kernel(positions).T, X.shape)
    return X, Y, Z


X, Y, Z = density_estimation(XX, YY)

'''##########################################################################################################################################'''

'''---------------------- Define the first work plot space --------------------'''
# Define the work-figure space
fig = plt.figure(figsize=(12,12))
fig.subplots_adjust(top=0.92, bottom=0.05, hspace=0.25, wspace=0.25)


'''---------------------- Bar diagram -----------------------------------'''
# Plot the bar diagram (Xi, ni)
ax1 = fig.add_subplot(221)
plt.bar(Xi, ni, edgecolor='k')
ax1.set_xticklabels(Xi, rotation=45)
ax1.set_title('Bar diagram', fontsize=16)
ax1.set_ylabel(r'$n_i$', fontsize=14)
ax1.grid(which='major', axis='y', linestyle='--')

'''---------------------- Histogram -----------------------------------'''
# Plot the histogram
ax2 = fig.add_subplot(222)
plt.hist(ni, edgecolor='k')
ax2.set_title('Histogram', fontsize=16)
ax2.set_xlabel(r'$n_i$', fontsize=14)
ax2.grid(which='major', axis='y', linestyle='--')

'''---------------------- Pie Diagram -----------------------------------'''
# Plot a cake
ax3 = fig.add_subplot(223)
sizes = z #percentages (10 in total one per each class Xi)
explode = (0, 0.1, 0, 0, 0, 0, 0, 0, 0, 0)  # only "explode" the 2nd slice (i.e. 'Class 2')

ax3.pie(sizes, explode=explode, labels=Xi, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax3.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

'''---------------------- Scatter dispersion diagram -----------------------------------'''
race = ['Americans', 'European']
money = [[1.0, 2.0, 3.0, 4.0, 5.0],[1.0,2.0,3.0,4.0,5.0]]
people = [[55.0, 25.5, 15.0, 1.5, 1.0],[60.0,45.0,10.0,0.5, 0.2]]

# Plot a scatter representation
ax4 = fig.add_subplot(2,2,4)
plt.scatter(money[0], people[0], marker='o', color='r', label=race[0])
plt.scatter(money[1], people[1], label=race[1])
ax4.set_title('Number of persons vs money per capita', fontsize=16)
ax4.set_xlabel(r'Money (in thousands dollars)', fontsize=14)
ax4.set_ylabel(r'People (in millions)', fontsize=14)
plt.grid()
plt.legend()


'''##########################################################################################################################################'''

'''---------------------- Define the second work plot space --------------------'''
# Define the work-figure space
fig1 = plt.figure(figsize=(12,12))
fig1.subplots_adjust(top=0.92, bottom=0.05, hspace=0.25, wspace=0.25)

'''---------------------- Countour Plot Diagram 2D-----------------------------------'''
# Plot a contour in 2D
ax5 = fig1.add_subplot(221)

# Show density
ax5.imshow(np.rot90(Z), cmap=plt.cm.gist_earth_r, extent=[xmin, xmax, ymin, ymax])
# Add contour lines
plt.contour(X, Y, Z, cmap='jet')
ax5.plot(XX, YY, 'r.', markersize=3)
ax5.set_xlim([xmin, xmax])
ax5.set_ylim([ymin, ymax])

'''---------------------- Contour Plot Diagram 3D -----------------------------------'''
# Plot a density contour plot in three dimensions
ax6=fig1.add_subplot(2,2,2, projection='3d')
ax6.contour(X, Y, Z, 50, cmap='jet') #with 50 level lines
ax6.plot(XX, YY, 'r.', markersize=3)

ax6.set_xlim([xmin, xmax])
ax6.set_ylim([ymin, ymax])
ax6.set_xlabel('X random', fontsize=12)
ax6.set_ylabel('Y random', fontsize=12)
ax6.set_zlabel('\n density value', fontsize=12, rotation=45)
ax6.ticklabel_format(axis="z", style="plain", scilimits=(0,0), useOffset=False)

'''---------------------- Scatter dispersion plot in 3D -----------------------------------'''
#Particle potential function
def potential_shape(x, y):
    return np.sin(np.sqrt(x ** 2 + y ** 2))

theta = 2 * np.pi * np.random.random(2000)
r = 6 * np.random.random(2000)
A = np.ravel(r * np.sin(theta))
B = np.ravel(r * np.cos(theta))
C = potential_shape(A, B)

# Plot a scatter in three dimensions
ax7=fig1.add_subplot(2,2,3, projection='3d')
ax7.scatter(A, B, C, c=C, cmap='viridis', linewidth=0.5)
ax7.set_title('particle potential shape', fontsize=12)


'''---------------------- Multiple variable representation in 2D -----------------------------------'''

Variable_one = [25, 40, 55, 70, 80, 100]
Variable_two = [14, 15, 20, 22, 24, 26]
Variable_three = [1820, 1860, 1880, 1920, 1940, 1980]

ax8=fig1.add_subplot(2,2,4)
plt.plot(Variable_one, Variable_two, color='green', marker='o', linestyle='dashed', linewidth=2, markersize=12)

for i,label in enumerate(Variable_three):
    plt.text(Variable_one[i]+0.5, Variable_two[i]+0.2,label)

ax8.set_xlabel('Variable_one', fontsize=12)
ax8.set_ylabel('Variable_two', fontsize=12)
ax8.set_title('Multiple variable representation', fontsize=12)
ax8.set_xlim([20,105])
ax8.set_ylim([10,30])

plt.grid()
plt.show()
