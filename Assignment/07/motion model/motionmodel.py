# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 16:24:29 2016

@author: chaitanya
"""

import numpy as np
import glob
import os
import matplotlib.pyplot as plt

directory_names = ['straight', 'slightleft', 'slightright', 'steepleft', 'steepright']
colors=['r','b','y','c','g']
figs = []
#data = read_data(directory_names)
posesx = []
posesy = []
for directory_name in directory_names:
    os.chdir(directory_name)
    
    #list the files
    files = list()
    for f in glob.glob("*.log"):
        files.append(f)
    
    posex = []
    posey = []
    #read the data
    for f in files:
        data = np.loadtxt(f,delimiter=' ',usecols = (0,2,3,4))
        posex.append(data[:,1])
        posey.append(data[:,2])
    posesx.append(posex)
    posesy.append(posey)
    os.chdir('..')

for x in range(0,len(posesx)):
    posex = posesx[x]
    posey = posesy[x]
    
    for y in range(0,len(posex)):
        tempx = posex[y]
        tempy = posey[y]
        meanx = np.mean(tempx)
        stdx = np.std(tempx)
        #centeredx = tempx - np.mean(tempx)
        #centeredy = tempy - np.mean(tempy)
        
        it = plt.scatter(tempx,tempy,color=colors[x],s=8)
    figs.append(it)

print figs
plt.autoscale()
plt.grid('on')
plt.axis('equal')
#ax = plt.gca()
#plt.xlim(1000,-1000)
#plt.ylim(200,-3000)
plt.xlabel('Y World Axis (in mm)')
plt.ylabel('X World Axis (in mm)')
#plt.gca().set_aspect('equal', adjustable='box')
plt.legend((figs), 
   (directory_names),
   scatterpoints=1,
   ncol=1,
   loc='lower left',
   fontsize=16)
plt.legend()
plt.show()