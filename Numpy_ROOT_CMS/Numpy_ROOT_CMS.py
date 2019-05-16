#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 15 15:31:01 2019

@author: Daniel Fernandez Fernandez
daniel.fernandez.fernandez.94@gmail.com

Example with numpy_root with CMS data
"""
#import numpy as np
#import root_numpy as rn
from ROOT import TFile

file_data = TFile('files/data.root')
file_dy = TFile('files/dy.root')
file_qcd = TFile('files/qcd.root')
file_singletop = TFile('files/single_top.root')
file_ttbar = TFile('files/ttbar.root')
file_wjets = TFile('files/wjets.root')
file_ww = TFile('files/ww.root')
file_wz = TFile('files/wz.root')
file_zz = TFile('files/zz.root')
'''
tree_data = file_data.Get('events')
tree_dy = file_dy.Get('events')
tree_qcd = file_qcd.Get('events')
tree_singletop = file_singletop.Get('events')
tree_ttbar = file_ttbar.Get('events')
tree_wjets = file_wjets.Get('events')
tree_ww = file_ww.Get('events')
tree_wz = file_wz.Get('events')
tree_zz = file_zz.Gte('events')

array_data = rn.tree2array(tree_data)           
array_dy = rn.tree2array(tree_dy)
array_qcd = rn.tree2array(tree_qcd)
array_singletop = rn.tree2array(tree_singletop)
array_ttbar = rn.tree2array(tree_ttbar)
array_wjets = rn.tree2array(tree_wjets)
array_ww = rn.tree2array(tree_ww)
array_wz = rn.tree2array(tree_wz)
array_zz = rn.tree2array(tree_zz)
'''
#print(array_data)