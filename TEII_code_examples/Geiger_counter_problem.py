#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sunday Aug 11 11:35:00 2019

@author: Daniel Fernandez Fernandez
dani.fernandez@usc.es

Geiger Counter Analysis

Ejemplo: (1.8 en [VAR10]) Datos de una desintegración radiactiva medidas por un contador Geiger
en el que se han efectuado medidas cada 30 segundos.
"""

import numpy as np

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
ni -- Absolute frecuency
fi -- Relative frequency
Ni -- Absolute cumulative frequency
Fi -- Relative cumulative frequency
"""

Xi, ni = np.unique(Geiger_counts, return_counts=True)
