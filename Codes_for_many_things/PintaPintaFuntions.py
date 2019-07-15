#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 12:45:20 2019

@author: macbookpro
"""
import numpy as np
import matplotlib.pyplot as plt



a = np.array([])
b = np.array([])
c = np.array([])

x = np.linspace(0, 240, 240)

def B(x):
    return (1.0/2)*x*(x-1.0)


for i in range(0, len(x)):
    point = B(x[i])
    b = np.append(b, point)
    point = 0.0
    
ratio = b/x
  
plt.plot(x, ratio)

