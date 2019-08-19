#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tuesday Aug 13 12:52:00 2019

@author: Daniel Fernandez Fernandez
dani.fernandez@usc.es

Problem 1.1: In a children's clinic they have been writing down the number of meters that their children
walk followed and without falling. For a month the first day the childrens begin to walk.
The table obtained was:
Number of children: 2 6 10 5 10 3 2 2
Number of meters:   1 2 3 4 5 6 7 8

"""

import numpy as np
from scipy import stats
import matplotlib
import matplotlib.pyplot as plt

'''
-------------------------------------------- Read the data -----------------------------------------------------------------------
'''

Number_children = np.array([2, 6, 10, 5, 10, 3, 2, 2])
Number_meters = np.array([1, 2, 3, 4, 5, 6, 7, 8])

'''
--------------- a) Frequency table and bar diagram for absolute and relative frequencies ----------------------------------------------
'''

"""
Variable legend:
Xi -- Results of the random variable x
ni -- Absolute frequency
fi -- Relative frequency
Ni -- Absolute cumulative frequency
N  -- Total sum of independents measurements
Fi -- Relative cumulative frequency
"""

# Translate
Xi, ni = Number_meters, Number_children

# The total number of children
N = np.sum(ni)

fi = ni/N

Ni = np.cumsum(ni)

Fi = np.cumsum(fi)

# Representation in a table:
print('--------------------------------------')
print('xi  |  ni  |   fi   |   Ni   |   Fi   ')
print('--------------------------------------')
for i in range(0, len(Xi)):
    print('%i   |  %i   |  %.3f  |  %i    |   %.3f' %(Xi[i], ni[i], fi[i], Ni[i], Fi[i]))


# Define the work-figure space
fig = plt.figure(figsize=(12,12))
fig.subplots_adjust(top=0.92, bottom=0.05, hspace=0.25, wspace=0.25)

# Plot the bar-histogram (Xi, ni)
ax1 = fig.add_subplot(221)
plt.bar(Xi, ni, edgecolor='k')
plt.plot(Xi, ni, 'o-', color='r')
ax1.xaxis.set_ticks(Xi)
ax1.set_title('Absolute frequency', fontsize=16)
ax1.set_xlabel(r'$X_i$', fontsize=14)
ax1.set_ylabel(r'$n_i$', fontsize=14)
ax1.grid(which='major', axis='y', linestyle='--')

# Plot the bar-histogram (Xi, Ni)
ax2 = fig.add_subplot(222)
plt.bar(Xi, Ni, edgecolor='k')
plt.plot(Xi, Ni, 'o-', color='r')
ax2.xaxis.set_ticks(Xi)
ax2.set_title('Absolute cumulative frequency', fontsize=16)
ax2.set_xlabel(r'$X_i$', fontsize=14)
ax2.set_ylabel(r'$N_i$', fontsize=14)
ax2.grid(which='major', axis='y', linestyle='--')

# Plot the bar-histogram (Xi, fi)
ax3 = fig.add_subplot(223)
plt.bar(Xi, fi, edgecolor='k')
plt.plot(Xi, fi, 'o-', color='r')
ax3.xaxis.set_ticks(Xi)
ax3.set_title('Relative frequency', fontsize=16)
ax3.set_xlabel(r'$X_i$', fontsize=14)
ax3.set_ylabel(r'$f_i$', fontsize=14)
ax3.grid(which='major', axis='y', linestyle='--')

# Plot the bar-histogram (Xi, fi)
ax4 = fig.add_subplot(224)
plt.bar(Xi, Fi, edgecolor='k')
plt.plot(Xi, Fi, 'o-', color='r')
ax4.xaxis.set_ticks(Xi)
ax4.set_title('Relative cumulative frequency', fontsize=16)
ax4.set_xlabel(r'$X_i$', fontsize=14)
ax4.set_ylabel(r'$F_i$', fontsize=14)
ax4.grid(which='major', axis='y', linestyle='--')

plt.show()


'''
------------------------ b) Mean, Mode, median, quartiles and deciles --------------------------------
'''
"""mean"""
Mean = np.mean(ni)

"""mode"""
Mode = stats.mode(ni)

"""median"""
Median = np.median(ni, axis=None, out=None)

"""percentiles"""
quartiles = np.percentile(ni, [25, 50, 75], interpolation = 'midpoint')
deciles = np.percentile(ni, [10, 20], interpolation = 'midpoint')

# Representation in a table:
print('\n')
print('---------------------------------------------------------------------------------')
print('Mean  |  Mode and counts |   Median   | Quartiles [25, 50, 75] | Deciles [10, 20]')
print('---------------------------------------------------------------------------------')
print('%.2f  |   %i       %i      |    %.2f    |       %s       |     %s        ' %(Mean, Mode[0], Mode[1], Median, quartiles, deciles))


'''
-----------------------  c) Interquartile range --------------------------------------------------------
'''

IR = quartiles[2] - quartiles[0] #IR = P(0.75) - P(0.25)

print('\n')
print('Interquartile range: ', IR)

for i in range(0, len(ni)):
    if ((ni[i] >= 1.5*IR) and (ni[i] < 3.0*IR)):
        print('Low atypical point-value: %i' %ni[i])
    elif (ni[i] >= 3.0*IR):
        print('Extreme atypical point-value: %i' %ni[i])


'''
------------- d) Arithmetic, geometric, quadratic and harmonic mean ------------------------------------
'''

"""Definition of each function"""
def Arit_mean(Xi,fi):
    return sum([X * f for X,f in zip(Xi,fi)])

def Geo_mean(Xi,ni):
    return np.prod((np.array([X**n for X,n in zip(Xi, ni)]))**(1./sum(ni)))

def Quad_mean(Xi,fi):
    return np.sqrt(sum([X**2 * f for X,f in zip(Xi,fi)]))

def Harmo_mean(Xi,fi):
    return 1./(sum([f/X for f,X in zip(fi,Xi)]))


Arit_mean_v = Arit_mean(Xi,fi)
Geo_mean_v = Geo_mean(Xi,ni)
Quad_mean_v = Quad_mean(Xi,fi)
Harmo_mean_v = Harmo_mean(Xi,fi)

# Representation in a table:
print('\n')
print('---------------------------------------------------------------------------------')
print('Arithmetic mean  |  Geometric mean |   Quadratic mean   |  Harmonic mean')
print('---------------------------------------------------------------------------------')
print('     %.4f      |      %.4f     |        %.4f      |       %.4f     ' %(Arit_mean_v, Geo_mean_v, Quad_mean_v, Harmo_mean_v))

'''
------------- e) Variance, the standard deviation and Pearson's variation coefficient -------------------------
'''

"""Definition of variance function"""
def Variance(Xi,fi):
    return sum([f*(X-Arit_mean(Xi,fi))**2 for X,f in zip(Xi,fi)])

Variance_v = Variance(Xi,fi)
Std_desviation = np.sqrt(Variance_v)
Pearson_CV = Std_desviation/Arit_mean_v

# Representation in a table:
print('\n')
print('---------------------------------------------------------------------------------')
print('Variance  |  Standard desviation |   Pearson_CV  ')
print('---------------------------------------------------------------------------------')
print(' %.4f   |       %.4f         |     %.4f    ' %(Variance_v, Std_desviation, Pearson_CV))

'''
------------- f) Moments, m, respect the origin of first, second and third order -------------------------
'''
"""Definition of moment function"""
def m_value_order(Xi, fi, value, order):
    return sum([f*(X-value)**order for X,f in zip(Xi,fi)])

m_0_1st = m_value_order(Xi, fi, 0, 1)
m_0_2sd = m_value_order(Xi, fi, 0, 2)
m_0_3th = m_value_order(Xi, fi, 0, 3)

# Representation in a table:
print('\n')
print('---------------------------------------------------------------------------------')
print('m(0)^1  |  m(0)^2 |   m(0)^3  ')
print('---------------------------------------------------------------------------------')
print(' %.2f   |  %.2f  |   %.2f  ' %(m_0_1st, m_0_2sd, m_0_3th))

'''
------------- g) Central moments respect the mean of first, second and third order -------------------------
'''

m_mean_1st = m_value_order(Xi, fi, Arit_mean(Xi,fi), 1)
m_mean_2sd = m_value_order(Xi, fi, Arit_mean(Xi,fi), 2)
m_mean_3th = m_value_order(Xi, fi, Arit_mean(Xi,fi), 3)

# Representation in a table:
print('\n')
print('---------------------------------------------------------------------------------')
print('m(mean)^1  |   m(mean)^2  |   m(mean)^3  ')
print('---------------------------------------------------------------------------------')
print(' %.1f       |    %.4f    |   %.4f  ' %(m_mean_1st, m_mean_2sd, m_mean_3th))

'''
------------- h) Asimetry and curtosis -------------------------
'''
"""Definition of each function"""
def asimetry(Xi, fi):
    return ((1./np.sqrt(Variance(Xi,fi))**(3))*sum([f*(X-Arit_mean(Xi,fi))**3 for X,f in zip(Xi, fi)]))

def curtosis(Xi,fi):
    return ((1./np.sqrt(Variance(Xi,fi))**(4))*sum([f*(X-Arit_mean(Xi,fi))**4 for X,f in zip(Xi, fi)]))


Asimetry_v = asimetry(Xi, fi)
Curtosis_v = curtosis(Xi, fi)

# Representation in a table:
print('\n')
print('---------------------------------------------------------------------------------')
print('Asimetry   |   Curtosis  ')
print('---------------------------------------------------------------------------------')
print(' %.4f    |    %.4f  ' %(Asimetry_v, Curtosis_v))
