#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sunday Aug 11 11:35:00 2019

@author: Daniel Fernandez Fernandez
dani.fernandez@usc.es

Geiger Counter Analysis

Example: (1.8 in [VAR10]) Data of radioactive decay measured by a Geiger counter in which measurements have been made every 30 seconds.

"""

import numpy as np
import matplotlib
import matplotlib.pyplot as plt

'''
-------------------------------------------- Read the data -----------------------------------------------------------------------
'''

Geiger_counts = np.array([7, 5, 3, 6, 8, 4, 5, 7, 6, 4, 6, 3, 4, 4, 5, 7, 5, 4, 3, 4, 9, 8, 9, 7, 0, 3, 5, 8, 7, 8, 4, 6, 5, 5, 7, 4, 7, 3, 5, 2,
3, 5, 3, 8, 4, 9, 4, 10, 3, 5, 5, 8, 6, 7, 6, 5, 6, 6, 2, 9, 8, 9, 5, 9, 6, 5, 5, 7, 3, 7, 6, 4, 6, 9, 4, 5, 7, 6, 5, 8,
4, 8, 4, 5, 7, 8, 7, 6, 5, 4, 5, 7, 8, 3, 9, 6, 1, 6, 1, 5, 7, 5, 3, 9, 8, 1, 6, 4, 7, 8, 5, 6, 11, 9, 7, 4, 5, 10, 7, 4,
6, 4, 6, 10, 7, 6, 2, 13, 3, 6, 0, 8, 1, 6, 8, 1, 11, 6, 8, 3, 5, 6, 9, 4, 10, 7, 6, 7, 9, 6, 3, 7, 5, 12, 7, 8, 6, 3, 5, 6,
2, 7, 5, 6, 7, 5, 5, 2, 4, 6, 9, 2, 5, 10, 2, 9, 5, 5, 7, 4, 2, 6, 7, 8, 4, 5, 7, 6, 6, 7, 5, 4, 3, 2, 6, 8, 7, 1, 6, 5,
10, 8, 3, 2, 8, 4, 6, 3, 3, 8, 4, 5, 6, 7, 8, 6, 9, 8, 3, 2, 11, 2, 6, 5, 5, 7, 9, 8, 5, 2, 4, 6, 6, 3, 5, 4, 6, 4, 4, 5,
7, 5, 6, 7, 4, 10, 6, 7, 4, 5, 8, 7, 5, 5, 4, 6, 3, 8, 6, 6, 12, 10, 5, 6, 12, 3, 11, 4, 10, 4, 5, 4, 9, 8, 3, 6, 8, 7, 5, 2,
3, 5, 10, 7, 9, 6, 7, 4, 11, 7, 6, 1, 11, 2, 5, 9, 4, 8, 5, 6])

'''
------------------------------ Data frequency analysis table (only numpy without pandas) ------------------------------------------
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

Xi, ni = np.unique(Geiger_counts, return_counts=True)

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

'''
------------------------------------------ Figures and representation --------------------------------------------------------------
'''

# Define the work-figure space
fig = plt.figure(figsize=(12,5))

# Plot the bar-histogram (Xi, ni)
ax1 = fig.add_subplot(121)
plt.bar(Xi, ni, edgecolor='k')
ax1.xaxis.set_ticks(Xi)
ax1.set_title('Absolute frequency', fontsize=16)
ax1.set_xlabel(r'$X_i$', fontsize=14)
ax1.set_ylabel(r'$n_i$', fontsize=14)

# Plot the bar-histogram (Xi, Ni)
ax2 = fig.add_subplot(122)
plt.bar(Xi, Ni, edgecolor='k')
ax2.xaxis.set_ticks(Xi)
ax2.set_title('Absolute cumulative frequency', fontsize=16)
ax2.set_xlabel(r'$X_i$', fontsize=14)
ax2.set_ylabel(r'$N_i$', fontsize=14)

plt.show()
