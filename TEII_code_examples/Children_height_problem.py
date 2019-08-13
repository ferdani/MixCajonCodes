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
--------------- b)
'''
