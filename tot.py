#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 17:59:26 2020

@author: bruno menon

simple truth table

input : number of variable you want display (in this sample =4 )
output: array with all possible combination ( table of truth: tot)
"""


import numpy as np

#enter here the number of variable you want to display here it's 4
numberVariable= 4


# automatic define the number of possible combination
numberItems  = int(2**numberVariable)


def unique_rows(data):
    uniq = np.unique(data.view(data.dtype.descr * data.shape[1]))
    return uniq.view(data.dtype).reshape(-1, data.shape[1])

# initialisation zeros in the truth table arrays
tot = np.zeros((numberItems,numberVariable),dtype=bool)

stepMotif = 1
v = 0  
i = 0  
m = 0  

while v < numberVariable :
    while i < numberItems :
        while ( ( m < stepMotif) and (i < numberItems)):
            tot[i,v] = True
            i +=1
            m += 1
        i += stepMotif
        m =0  
    v +=1  
    stepMotif = stepMotif *2  
    i=0   

print('Table of Truth for {} variables'.format(numberVariable))
print(tot)
