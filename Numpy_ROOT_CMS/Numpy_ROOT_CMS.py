#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 15 15:31:01 2019

@author: Daniel Fernandez Fernandez
daniel.fernandez.fernandez.94@gmail.com

Example with numpy_root with CMS data to analyze the Z boson peak decaying two muons (Z->Mu+Mu-)
"""
import numpy as np
import root_numpy as rn
from ROOT import TFile, TLorentzVector
import matplotlib
import matplotlib.pyplot as plt

#Define constants
Path_to_tree = 'files/'


'''
------------------------------- Load the .root files -----------------------------------
'''
'''
file_data = TFile(Path_to_tree + 'data.root')
file_dy = TFile(Path_to_tree + 'dy.root')
file_qcd = TFile(Path_to_tree + 'qcd.root')
file_singletop = TFile(Path_to_tree + 'single_top.root')
file_ttbar = TFile(Path_to_tree + 'ttbar.root')
file_wjets = TFile(Path_to_tree + 'wjets.root')
file_ww = TFile(Path_to_tree + 'ww.root')
file_wz = TFile(Path_to_tree + 'wz.root')
file_zz = TFile (Path_to_tree +'zz.root')

#Load the events
tree_data = file_data.Get('events')
tree_dy = file_dy.Get('events')
tree_qcd = file_qcd.Get('events')
tree_singletop = file_singletop.Get('events')
tree_ttbar = file_ttbar.Get('events')
tree_wjets = file_wjets.Get('events')
tree_ww = file_ww.Get('events')
tree_wz = file_wz.Get('events')
tree_zz = file_zz.Get('events')
'''

'''
------------------------------ Define Branches, select the candidates and do cuts over the branches -----------------------
'''

SamplesList = ['data', 'dy', 'qcd', 'singletop', 'ttbar', 'wjets', 'ww', 'wz', 'zz']

#Tree branches by hand or all directly:
#Tree_Branches = ['Muon_Px', 'Muon_Py', 'Muon_Pz', 'Muon_E', 'Muon_Charge', 'Muon_Iso'] #for example
Tree_Branches = rn.list_branches('files/data.root')

#Select the candidates, two muons, zero electrons and zero photons with some requirements
Candidates_Selection = 'NMuon == 2 & NElectron == 0 & NPhoton == 0 & NJet == 0'
IsoTrigger_Selection = 'triggerIsoMu24 == 1.0'
HadroMC_Selection = 'MChadronicWDecayQuark_px == 0.0'

#Combine all the cuts in the selection:
Tree_Selection = [Candidates_Selection, IsoTrigger_Selection, HadroMC_Selection]
Tree_Selection = '&'.join(Tree_Selection)


print('Choosing candidates ...')
#array_data = rn.root2array(filenames = Path_to_tree + 'data.root', treename = 'events', branches = ['Muon_Px' , 'NMuon'], selection = 'NMuon == 2.0' , object_selection = {'Muon_Px == 0.0' : 'Muon_Px'})

array_data = rn.root2array(filenames = Path_to_tree + 'data.root', treename = 'events', branches = Tree_Branches, selection = Tree_Selection)
array_dy = rn.root2array(filenames = Path_to_tree + 'dy.root', treename = 'events', branches = Tree_Branches, selection = Tree_Selection)
array_qcd = rn.root2array(filenames = Path_to_tree + 'qcd.root', treename = 'events', branches = Tree_Branches, selection = Tree_Selection)
array_singletop = rn.root2array(filenames = Path_to_tree + 'single_top.root', treename = 'events', branches = Tree_Branches, selection = Tree_Selection)
array_ttbar = rn.root2array(filenames = Path_to_tree + 'ttbar.root', treename = 'events', branches = Tree_Branches, selection = Tree_Selection)
array_wjets = rn.root2array(filenames = Path_to_tree + 'wjets.root', treename = 'events', branches = Tree_Branches, selection = Tree_Selection)
array_ww = rn.root2array(filenames = Path_to_tree + 'ww.root', treename = 'events', branches = Tree_Branches, selection = Tree_Selection)
array_wz = rn.root2array(filenames = Path_to_tree + 'wz.root', treename = 'events', branches = Tree_Branches, selection = Tree_Selection)
array_zz = rn.root2array(filenames = Path_to_tree + 'zz.root', treename = 'events', branches = Tree_Branches, selection = Tree_Selection)

'''
#in data cuts
data_muon_px = [[]]
for i in range(0, len(array_data['NMuon'])):
        if (array_data['Muon_Charge'][i][0] * array_data['Muon_Charge'][i][1] == -1):
                aux = array_data['Muon_Px'][i]
                data_muon_px = np.append(data_muon_px, aux)




#Define the cuts over the branches:
PT_Selection = 'Muon_Px > 50.0 & Muon_Py > 50.0' #momentum selection
E_Selection = 'Muon_E > 50.0'

#Combine all the cuts in the selection:
Tree_Selection = [PT_Selection, E_Selection]
Tree_Selection = '&'.join(Tree_Selection)

#pasando de tree a array
#tree_array_data = rn.tree2array(tree_data, Tree_Branches, Tree_Selection)
'''
'''
------------------------------ Using the tree directly --------------------------------
'''
'''
print('Analyzing the trees ...')
#root2array(filenames, treename, branches, selection, object_selection, start, stop, step, include_weight, weight_name, cache_size, warn_missing_tree)
array_data = rn.root2array(filenames = Path_to_tree + 'data.root', treename = 'events', branches = Tree_Branches, selection = Tree_Selection)
array_dy = rn.root2array(filenames = Path_to_tree + 'dy.root', treename = 'events', branches = Tree_Branches, selection = Tree_Selection)
array_qcd = rn.root2array(filenames = Path_to_tree + 'qcd.root', treename = 'events', branches = Tree_Branches, selection = Tree_Selection)
array_singletop = rn.root2array(filenames = Path_to_tree + 'single_top.root', treename = 'events', branches = Tree_Branches, selection = Tree_Selection)
array_ttbar = rn.root2array(filenames = Path_to_tree + 'ttbar.root', treename = 'events', branches = Tree_Branches, selection = Tree_Selection)
array_wjets = rn.root2array(filenames = Path_to_tree + 'wjets.root', treename = 'events', branches = Tree_Branches, selection = Tree_Selection)
array_ww = rn.root2array(filenames = Path_to_tree + 'ww.root', treename = 'events', branches = Tree_Branches, selection = Tree_Selection)
array_wz = rn.root2array(filenames = Path_to_tree + 'wz.root', treename = 'events', branches = Tree_Branches, selection = Tree_Selection)
array_zz = rn.root2array(filenames = Path_to_tree + 'zz.root', treename = 'events', branches = Tree_Branches, selection = Tree_Selection)
'''


'''
---------------------------- Making the arrays ------------------------------------------
'''

Muon_1_E_array_data = np.array([]); Muon_2_E_array_data = np.array([]); Muon_1_Px_array_data = np.array([]); Muon_2_Px_array_data = np.array([]);
Muon_1_Py_array_data = np.array([]); Muon_2_Py_array_data = np.array([]); Muon_1_Pz_array_data = np.array([]); Muon_2_Pz_array_data = np.array([])
Muon_1_E_array_dy = np.array([]); Muon_2_E_array_dy = np.array([]); Muon_1_Px_array_dy = np.array([]); Muon_2_Px_array_dy = np.array([]);
Muon_1_Py_array_dy = np.array([]); Muon_2_Py_array_dy = np.array([]); Muon_1_Pz_array_dy = np.array([]); Muon_2_Pz_array_dy = np.array([])
Muon_1_E_array_qcd = np.array([]); Muon_2_E_array_qcd = np.array([]); Muon_1_Px_array_qcd = np.array([]); Muon_2_Px_array_qcd = np.array([]);
Muon_1_Py_array_qcd = np.array([]); Muon_2_Py_array_qcd = np.array([]); Muon_1_Pz_array_qcd = np.array([]); Muon_2_Pz_array_qcd = np.array([])
Muon_1_E_array_singletop = np.array([]); Muon_2_E_array_singletop = np.array([]); Muon_1_Px_array_singletop = np.array([]); Muon_2_Px_array_singletop = np.array([]);
Muon_1_Py_array_singletop = np.array([]); Muon_2_Py_array_singletop = np.array([]); Muon_1_Pz_array_singletop = np.array([]); Muon_2_Pz_array_singletop = np.array([])
Muon_1_E_array_ttbar = np.array([]); Muon_2_E_array_ttbar = np.array([]); Muon_1_Px_array_ttbar = np.array([]); Muon_2_Px_array_ttbar = np.array([]);
Muon_1_Py_array_ttbar = np.array([]); Muon_2_Py_array_ttbar = np.array([]); Muon_1_Pz_array_ttbar = np.array([]); Muon_2_Pz_array_ttbar = np.array([])
Muon_1_E_array_wjets = np.array([]); Muon_2_E_array_wjets = np.array([]); Muon_1_Px_array_wjets = np.array([]); Muon_2_Px_array_wjets = np.array([]);
Muon_1_Py_array_wjets = np.array([]); Muon_2_Py_array_wjets = np.array([]); Muon_1_Pz_array_wjets = np.array([]); Muon_2_Pz_array_wjets = np.array([])
Muon_1_E_array_ww = np.array([]); Muon_2_E_array_ww = np.array([]); Muon_1_Px_array_ww = np.array([]); Muon_2_Px_array_ww = np.array([]);
Muon_1_Py_array_ww = np.array([]); Muon_2_Py_array_ww = np.array([]); Muon_1_Pz_array_ww = np.array([]); Muon_2_Pz_array_ww = np.array([])
Muon_1_E_array_wz = np.array([]); Muon_2_E_array_wz = np.array([]); Muon_1_Px_array_wz = np.array([]); Muon_2_Px_array_wz = np.array([]);
Muon_1_Py_array_wz = np.array([]); Muon_2_Py_array_wz = np.array([]); Muon_1_Pz_array_wz = np.array([]); Muon_2_Pz_array_wz = np.array([])
Muon_1_E_array_zz = np.array([]); Muon_2_E_array_zz = np.array([]); Muon_1_Px_array_zz = np.array([]); Muon_2_Px_array_zz = np.array([]);
Muon_1_Py_array_zz = np.array([]); Muon_2_Py_array_zz = np.array([]); Muon_1_Pz_array_zz = np.array([]); Muon_2_Pz_array_zz = np.array([])

#building the TLorentzVector and the mass arrays
mu1 = TLorentzVector()
mu2 = TLorentzVector()

mu1_mass_data = np.array([]); mu2_mass_data = np.array([]); Mll_data = np.array([])
mu1_mass_dy = np.array([]); mu2_mass_dy = np.array([]); Mll_dy = np.array([])
mu1_mass_qcd = np.array([]); mu2_mass_qcd = np.array([]); Mll_qcd = np.array([])
mu1_mass_singletop = np.array([]); mu2_mass_singletop = np.array([]); Mll_singletop = np.array([])
mu1_mass_ttbar = np.array([]); mu2_mass_ttbar = np.array([]); Mll_ttbar = np.array([])
mu1_mass_wjets = np.array([]); mu2_mass_wjets = np.array([]); Mll_wjets = np.array([])
mu1_mass_ww = np.array([]); mu2_mass_ww = np.array([]); Mll_ww = np.array([])
mu1_mass_wz = np.array([]); mu2_mass_wz = np.array([]); Mll_wz = np.array([])
mu1_mass_zz = np.array([]); mu2_mass_zz = np.array([]); Mll_zz = np.array([])

'''
------------------------- Making the loops -----------------------------------------------
'''

Lenghts = [len(array_data['Muon_E']), len(array_dy['Muon_E']), len(array_qcd['Muon_E']), len(array_singletop['Muon_E']),
            len(array_ttbar['Muon_E']), len(array_wjets['Muon_E']), len(array_ww['Muon_E']), len(array_wz['Muon_E']), len(array_zz['Muon_E'])]

print('Making the arrays for ...')

print('data.root')
for i in range(0, Lenghts[0]):
    #Conditiones over the isolation and we want 2 muons with opposite charge
    if (array_data['Muon_Iso'][i][0] <= 5.2 and array_data['Muon_Iso'][i][1] <= 5.2 and array_data['Muon_Charge'][i][0] * array_data['Muon_Charge'][i][1] == -1):
        Muon_1_E_array_data  = np.append(Muon_1_E_array_data, array_data['Muon_E'][i][0])
        Muon_2_E_array_data  = np.append(Muon_2_E_array_data, array_data['Muon_E'][i][1])
        Muon_1_Px_array_data = np.append(Muon_1_Px_array_data, array_data['Muon_Px'][i][0])
        Muon_2_Px_array_data = np.append(Muon_2_Px_array_data, array_data['Muon_Px'][i][1])
        Muon_1_Py_array_data = np.append(Muon_1_Py_array_data, array_data['Muon_Py'][i][0])
        Muon_2_Py_array_data = np.append(Muon_2_Py_array_data, array_data['Muon_Py'][i][1])
        Muon_1_Pz_array_data = np.append(Muon_1_Pz_array_data, array_data['Muon_Pz'][i][0])
        Muon_2_Pz_array_data = np.append(Muon_2_Pz_array_data, array_data['Muon_Pz'][i][1])

        #evaluate the Z mass with the two muons
        mu1.SetPxPyPzE(array_data['Muon_Px'][i][0], array_data['Muon_Py'][i][0], array_data['Muon_Pz'][i][0], array_data['Muon_E'][i][0])
        mu2.SetPxPyPzE(array_data['Muon_Px'][i][1], array_data['Muon_Py'][i][1], array_data['Muon_Pz'][i][1], array_data['Muon_E'][i][1])
        mu1_mass_data = np.append(mu1_mass_data, mu1.M())
        mu2_mass_data = np.append(mu2_mass_data, mu2.M())
        Mll_data = np.append(Mll_data, (mu1+mu2).M())

print('dy.root')
for i in range(0, Lenghts[1]):
    if (array_dy['Muon_Iso'][i][0] <= 5.2 and array_dy['Muon_Iso'][i][1] <= 5.2 and array_dy['Muon_Charge'][i][0] * array_dy['Muon_Charge'][i][1] == -1):
        Muon_1_E_array_dy  = np.append(Muon_1_E_array_dy, array_dy['Muon_E'][i][0])
        Muon_2_E_array_dy  = np.append(Muon_2_E_array_dy, array_dy['Muon_E'][i][1])
        Muon_1_Px_array_dy = np.append(Muon_1_Px_array_dy, array_dy['Muon_Px'][i][0])
        Muon_2_Px_array_dy = np.append(Muon_2_Px_array_dy, array_dy['Muon_Px'][i][1])
        Muon_1_Py_array_dy = np.append(Muon_1_Py_array_dy, array_dy['Muon_Py'][i][0])
        Muon_2_Py_array_dy = np.append(Muon_2_Py_array_dy, array_dy['Muon_Py'][i][1])
        Muon_1_Pz_array_dy = np.append(Muon_1_Pz_array_dy, array_dy['Muon_Pz'][i][0])
        Muon_2_Pz_array_dy = np.append(Muon_2_Pz_array_dy, array_dy['Muon_Pz'][i][1])

        #evaluate the Z mass with the two muons
        mu1.SetPxPyPzE(array_dy['Muon_Px'][i][0], array_dy['Muon_Py'][i][0], array_dy['Muon_Pz'][i][0], array_dy['Muon_E'][i][0])
        mu2.SetPxPyPzE(array_dy['Muon_Px'][i][1], array_dy['Muon_Py'][i][1], array_dy['Muon_Pz'][i][1], array_dy['Muon_E'][i][1])
        mu1_mass_dy = np.append(mu1_mass_dy, mu1.M())
        mu2_mass_dy = np.append(mu2_mass_dy, mu2.M())
        Mll_dy = np.append(Mll_dy, (mu1+mu2).M())

print('qcd.root')
for i in range(0, Lenghts[2]):
    if (array_qcd['Muon_Iso'][i][0] <= 5.2 and array_qcd['Muon_Iso'][i][1] <= 5.2 and array_qcd['Muon_Charge'][i][0] * array_qcd['Muon_Charge'][i][1] == -1):
        Muon_1_E_array_qcd  = np.append(Muon_1_E_array_qcd, array_qcd['Muon_E'][i][0])
        Muon_2_E_array_qcd  = np.append(Muon_2_E_array_qcd, array_qcd['Muon_E'][i][1])
        Muon_1_Px_array_qcd = np.append(Muon_1_Px_array_qcd, array_qcd['Muon_Px'][i][0])
        Muon_2_Px_array_qcd = np.append(Muon_2_Px_array_qcd, array_qcd['Muon_Px'][i][1])
        Muon_1_Py_array_qcd = np.append(Muon_1_Py_array_qcd, array_qcd['Muon_Py'][i][0])
        Muon_2_Py_array_qcd = np.append(Muon_2_Py_array_qcd, array_qcd['Muon_Py'][i][1])
        Muon_1_Pz_array_qcd = np.append(Muon_1_Pz_array_qcd, array_qcd['Muon_Pz'][i][0])
        Muon_2_Pz_array_qcd = np.append(Muon_2_Pz_array_qcd, array_qcd['Muon_Pz'][i][1])

        #evaluate the Z mass with the two muons
        mu1.SetPxPyPzE(array_qcd['Muon_Px'][i][0], array_qcd['Muon_Py'][i][0], array_qcd['Muon_Pz'][i][0], array_qcd['Muon_E'][i][0])
        mu2.SetPxPyPzE(array_qcd['Muon_Px'][i][1], array_qcd['Muon_Py'][i][1], array_qcd['Muon_Pz'][i][1], array_qcd['Muon_E'][i][1])
        mu1_mass_qcd = np.append(mu1_mass_qcd, mu1.M())
        mu2_mass_qcd = np.append(mu2_mass_qcd, mu2.M())
        Mll_qcd = np.append(Mll_qcd, (mu1+mu2).M())

print('singletop.root')
for i in range(0, Lenghts[3]):
    if (array_singletop['Muon_Iso'][i][0] <= 5.2 and array_singletop['Muon_Iso'][i][1] <= 5.2 and array_singletop['Muon_Charge'][i][0] * array_singletop['Muon_Charge'][i][1] == -1):
        Muon_1_E_array_singletop  = np.append(Muon_1_E_array_singletop, array_singletop['Muon_E'][i][0])
        Muon_2_E_array_singletop  = np.append(Muon_2_E_array_singletop, array_singletop['Muon_E'][i][1])
        Muon_1_Px_array_singletop = np.append(Muon_1_Px_array_singletop, array_singletop['Muon_Px'][i][0])
        Muon_2_Px_array_singletop = np.append(Muon_2_Px_array_singletop, array_singletop['Muon_Px'][i][1])
        Muon_1_Py_array_singletop = np.append(Muon_1_Py_array_singletop, array_singletop['Muon_Py'][i][0])
        Muon_2_Py_array_singletop = np.append(Muon_2_Py_array_singletop, array_singletop['Muon_Py'][i][1])
        Muon_1_Pz_array_singletop = np.append(Muon_1_Pz_array_singletop, array_singletop['Muon_Pz'][i][0])
        Muon_2_Pz_array_singletop = np.append(Muon_2_Pz_array_singletop, array_singletop['Muon_Pz'][i][1])

        #evaluate the Z mass with the two muons
        mu1.SetPxPyPzE(array_singletop['Muon_Px'][i][0], array_singletop['Muon_Py'][i][0], array_singletop['Muon_Pz'][i][0], array_singletop['Muon_E'][i][0])
        mu2.SetPxPyPzE(array_singletop['Muon_Px'][i][1], array_singletop['Muon_Py'][i][1], array_singletop['Muon_Pz'][i][1], array_singletop['Muon_E'][i][1])
        mu1_mass_singletop = np.append(mu1_mass_singletop, mu1.M())
        mu2_mass_singletop = np.append(mu2_mass_singletop, mu2.M())
        Mll_singletop = np.append(Mll_singletop, (mu1+mu2).M())

print('ttbar.root')
for i in range(0, Lenghts[4]):
    if (array_ttbar['Muon_Iso'][i][0] <= 5.2 and array_ttbar['Muon_Iso'][i][1] <= 5.2 and array_ttbar['Muon_Charge'][i][0] * array_ttbar['Muon_Charge'][i][1] == -1):
        Muon_1_E_array_ttbar  = np.append(Muon_1_E_array_ttbar, array_ttbar['Muon_E'][i][0])
        Muon_2_E_array_ttbar  = np.append(Muon_2_E_array_ttbar, array_ttbar['Muon_E'][i][1])
        Muon_1_Px_array_ttbar = np.append(Muon_1_Px_array_ttbar, array_ttbar['Muon_Px'][i][0])
        Muon_2_Px_array_ttbar = np.append(Muon_2_Px_array_ttbar, array_ttbar['Muon_Px'][i][1])
        Muon_1_Py_array_ttbar = np.append(Muon_1_Py_array_ttbar, array_ttbar['Muon_Py'][i][0])
        Muon_2_Py_array_ttbar = np.append(Muon_2_Py_array_ttbar, array_ttbar['Muon_Py'][i][1])
        Muon_1_Pz_array_ttbar = np.append(Muon_1_Pz_array_ttbar, array_ttbar['Muon_Pz'][i][0])
        Muon_2_Pz_array_ttbar = np.append(Muon_2_Pz_array_ttbar, array_ttbar['Muon_Pz'][i][1])

        #evaluate the Z mass with the two muons
        mu1.SetPxPyPzE(array_ttbar['Muon_Px'][i][0], array_ttbar['Muon_Py'][i][0], array_ttbar['Muon_Pz'][i][0], array_ttbar['Muon_E'][i][0])
        mu2.SetPxPyPzE(array_ttbar['Muon_Px'][i][1], array_ttbar['Muon_Py'][i][1], array_ttbar['Muon_Pz'][i][1], array_ttbar['Muon_E'][i][1])
        mu1_mass_ttbar = np.append(mu1_mass_ttbar, mu1.M())
        mu2_mass_ttbar = np.append(mu2_mass_ttbar, mu2.M())
        Mll_ttbar = np.append(Mll_ttbar, (mu1+mu2).M())

print('wjets.root')
for i in range(0, Lenghts[5]):
    if (array_wjets['Muon_Iso'][i][0] <= 5.2 and array_wjets['Muon_Iso'][i][1] <= 5.2 and array_wjets['Muon_Charge'][i][0] * array_wjets['Muon_Charge'][i][1] == -1):
        Muon_1_E_array_wjets  = np.append(Muon_1_E_array_wjets, array_wjets['Muon_E'][i][0])
        Muon_2_E_array_wjets  = np.append(Muon_2_E_array_wjets, array_wjets['Muon_E'][i][1])
        Muon_1_Px_array_wjets = np.append(Muon_1_Px_array_wjets, array_wjets['Muon_Px'][i][0])
        Muon_2_Px_array_wjets = np.append(Muon_2_Px_array_wjets, array_wjets['Muon_Px'][i][1])
        Muon_1_Py_array_wjets = np.append(Muon_1_Py_array_wjets, array_wjets['Muon_Py'][i][0])
        Muon_2_Py_array_wjets = np.append(Muon_2_Py_array_wjets, array_wjets['Muon_Py'][i][1])
        Muon_1_Pz_array_wjets = np.append(Muon_1_Pz_array_wjets, array_wjets['Muon_Pz'][i][0])
        Muon_2_Pz_array_wjets = np.append(Muon_2_Pz_array_wjets, array_wjets['Muon_Pz'][i][1])

        #evaluate the Z mass with the two muons
        mu1.SetPxPyPzE(array_wjets['Muon_Px'][i][0], array_wjets['Muon_Py'][i][0], array_wjets['Muon_Pz'][i][0], array_wjets['Muon_E'][i][0])
        mu2.SetPxPyPzE(array_wjets['Muon_Px'][i][1], array_wjets['Muon_Py'][i][1], array_wjets['Muon_Pz'][i][1], array_wjets['Muon_E'][i][1])
        mu1_mass_wjets = np.append(mu1_mass_wjets, mu1.M())
        mu2_mass_wjets = np.append(mu2_mass_wjets, mu2.M())
        Mll_wjets = np.append(Mll_wjets, (mu1+mu2).M())

print('ww.root')
for i in range(0, Lenghts[6]):
    if (array_ww['Muon_Iso'][i][0] <= 5.2 and array_ww['Muon_Iso'][i][1] <= 5.2 and array_ww['Muon_Charge'][i][0] * array_ww['Muon_Charge'][i][1] == -1):
        Muon_1_E_array_ww  = np.append(Muon_1_E_array_ww, array_ww['Muon_E'][i][0])
        Muon_2_E_array_ww  = np.append(Muon_2_E_array_ww, array_ww['Muon_E'][i][1])
        Muon_1_Px_array_ww = np.append(Muon_1_Px_array_ww, array_ww['Muon_Px'][i][0])
        Muon_2_Px_array_ww = np.append(Muon_2_Px_array_ww, array_ww['Muon_Px'][i][1])
        Muon_1_Py_array_ww = np.append(Muon_1_Py_array_ww, array_ww['Muon_Py'][i][0])
        Muon_2_Py_array_ww = np.append(Muon_2_Py_array_ww, array_ww['Muon_Py'][i][1])
        Muon_1_Pz_array_ww = np.append(Muon_1_Pz_array_ww, array_ww['Muon_Pz'][i][0])
        Muon_2_Pz_array_ww = np.append(Muon_2_Pz_array_ww, array_ww['Muon_Pz'][i][1])

        #evaluate the Z mass with the two muons
        mu1.SetPxPyPzE(array_ww['Muon_Px'][i][0], array_ww['Muon_Py'][i][0], array_ww['Muon_Pz'][i][0], array_ww['Muon_E'][i][0])
        mu2.SetPxPyPzE(array_ww['Muon_Px'][i][1], array_ww['Muon_Py'][i][1], array_ww['Muon_Pz'][i][1], array_ww['Muon_E'][i][1])
        mu1_mass_ww = np.append(mu1_mass_ww, mu1.M())
        mu2_mass_ww = np.append(mu2_mass_ww, mu2.M())
        Mll_ww = np.append(Mll_ww, (mu1+mu2).M())

print('wz.root')
for i in range(0, Lenghts[7]):
    if (array_wz['Muon_Iso'][i][0] <= 5.2 and array_wz['Muon_Iso'][i][1] <= 5.2 and array_wz['Muon_Charge'][i][0] * array_wz['Muon_Charge'][i][1] == -1):
        Muon_1_E_array_wz  = np.append(Muon_1_E_array_wz, array_wz['Muon_E'][i][0])
        Muon_2_E_array_wz  = np.append(Muon_2_E_array_wz, array_wz['Muon_E'][i][1])
        Muon_1_Px_array_wz = np.append(Muon_1_Px_array_wz, array_wz['Muon_Px'][i][0])
        Muon_2_Px_array_wz = np.append(Muon_2_Px_array_wz, array_wz['Muon_Px'][i][1])
        Muon_1_Py_array_wz = np.append(Muon_1_Py_array_wz, array_wz['Muon_Py'][i][0])
        Muon_2_Py_array_wz = np.append(Muon_2_Py_array_wz, array_wz['Muon_Py'][i][1])
        Muon_1_Pz_array_wz = np.append(Muon_1_Pz_array_wz, array_wz['Muon_Pz'][i][0])
        Muon_2_Pz_array_wz = np.append(Muon_2_Pz_array_wz, array_wz['Muon_Pz'][i][1])

        #evaluate the Z mass with the two muons
        mu1.SetPxPyPzE(array_wz['Muon_Px'][i][0], array_wz['Muon_Py'][i][0], array_wz['Muon_Pz'][i][0], array_wz['Muon_E'][i][0])
        mu2.SetPxPyPzE(array_wz['Muon_Px'][i][1], array_wz['Muon_Py'][i][1], array_wz['Muon_Pz'][i][1], array_wz['Muon_E'][i][1])
        mu1_mass_wz = np.append(mu1_mass_wz, mu1.M())
        mu2_mass_wz = np.append(mu2_mass_wz, mu2.M())
        Mll_wz = np.append(Mll_wz, (mu1+mu2).M())

print('zz.root')
for i in range(0, Lenghts[8]):
    if (array_zz['Muon_Iso'][i][0] <= 5.2 and array_zz['Muon_Iso'][i][1] <= 5.2 and array_zz['Muon_Charge'][i][0] * array_zz['Muon_Charge'][i][1] == -1):
        Muon_1_E_array_zz  = np.append(Muon_1_E_array_zz, array_zz['Muon_E'][i][0])
        Muon_2_E_array_zz  = np.append(Muon_2_E_array_zz, array_zz['Muon_E'][i][1])
        Muon_1_Px_array_zz = np.append(Muon_1_Px_array_zz, array_zz['Muon_Px'][i][0])
        Muon_2_Px_array_zz = np.append(Muon_2_Px_array_zz, array_zz['Muon_Px'][i][1])
        Muon_1_Py_array_zz = np.append(Muon_1_Py_array_zz, array_zz['Muon_Py'][i][0])
        Muon_2_Py_array_zz = np.append(Muon_2_Py_array_zz, array_zz['Muon_Py'][i][1])
        Muon_1_Pz_array_zz = np.append(Muon_1_Pz_array_zz, array_zz['Muon_Pz'][i][0])
        Muon_2_Pz_array_zz = np.append(Muon_2_Pz_array_zz, array_zz['Muon_Pz'][i][1])

        #evaluate the Z mass with the two muons
        mu1.SetPxPyPzE(array_zz['Muon_Px'][i][0], array_zz['Muon_Py'][i][0], array_zz['Muon_Pz'][i][0], array_zz['Muon_E'][i][0])
        mu2.SetPxPyPzE(array_zz['Muon_Px'][i][1], array_zz['Muon_Py'][i][1], array_zz['Muon_Pz'][i][1], array_zz['Muon_E'][i][1])
        mu1_mass_zz = np.append(mu1_mass_zz, mu1.M())
        mu2_mass_zz = np.append(mu2_mass_zz, mu2.M())
        Mll_zz = np.append(Mll_zz, (mu1+mu2).M())



'''
--------------------------- Making the plots ------------------------------------------
'''

fig=plt.figure(figsize=(20,10))
fig.subplots_adjust(top=0.90, bottom=0.10, hspace=0.2, wspace=0.2)
ax1 = fig.add_subplot(1,2,1)
plt.hist(Mll_dy, bins = 250, stacked=True, normed = False)
plt.hist(Mll_qcd, bins = 250, stacked=True, normed = False)
plt.hist(Mll_singletop, bins = 250, stacked=True, normed = False)
plt.hist(Mll_ttbar, bins = 250, stacked=True, normed = False)
plt.hist(Mll_wjets, bins = 250, stacked=True, normed = False)
plt.hist(Mll_ww, bins = 250, stacked=True, normed = False)
plt.hist(Mll_wz, bins = 250, stacked=True, normed = False)
plt.hist(Mll_zz, bins = 250, stacked=True, normed = False)

#plt.hist(Mll_data, bins = 250.0, stacked=False, normed = False)

ax1.set_title(r'$Z \to \mu^{+}\mu^{-}$', fontsize=16)
ax1.set_xlabel(r'$M_{ll}$ [GeV]', fontsize=14)
ax1.set_ylabel(r'counts', fontsize=14)
#ax1.set_yscale('log')
#ax1.set_xscale('log')
ax1.set_xlim([0, 200])
plt.grid(True)
#plt.legend()

ax2 = fig.add_subplot(1,2,2)
plt.hist(Mll_dy, bins = 50, stacked=True, normed = False)
plt.hist(Mll_qcd, bins = 50, stacked=True, normed = False)
plt.hist(Mll_singletop, bins = 50, stacked=True, normed = False)
plt.hist(Mll_ttbar, bins = 50, stacked=True, normed = False)
plt.hist(Mll_wjets, bins = 50, stacked=True, normed = False)
plt.hist(Mll_ww, bins = 50, stacked=True, normed = False)
plt.hist(Mll_wz, bins = 50, stacked=True, normed = False)
plt.hist(Mll_zz, bins = 50, stacked=True, normed = False)

#plt.hist(Mll_data, bins = 20.0, stacked=False, normed = False)

ax2.set_title(r'$Z \to \mu^{+}\mu^{-}$', fontsize=16)
ax2.set_xlabel(r'$M_{ll}$ [GeV]', fontsize=14)
ax2.set_ylabel(r'counts', fontsize=14)
ax2.set_yscale('log')
#ax.set_xscale('log')
ax2.set_xlim([0, 200])
plt.grid(True)
#plt.legend()


plt.show();
#plt.savefig('figura_test.png')
