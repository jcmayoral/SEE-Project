# -*- coding: utf-8 -*-
"""
Created on Sun Nov  6 21:22:10 2016

@author: jose
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.mlab import PCA

def extract (name):
    x,y,theta = [],[],[]

    for i in range(1,41):
        with open(name + '/' + name + str(i) + extension ,'r') as f:
            for l in f:
                a = l.split(' ')
                x.append(a[2])
                y.append(a[3])
                theta.append(a[4])
    return x,y,theta

def process(data,mean):

    newdata = np.ndarray(len(data))
    for index,val in enumerate(data):
        newdata[index] = val-mean
        
    return newdata

plt.grid('on')
plt.title('Centering to Zero Calculated Initial Pose')
plt.xlabel('Y World Axis (in mm)')
plt.ylabel('X World Axis (in mm)')
plt.gca().set_aspect('equal', adjustable='box')
#plt.draw()
#plt.gca().set_aspect('equal', adjustable='box')
print "done all"

name = ['straight','slightleft','slightright','left','right']
colors=['r','b','y','c','g']
extension = '.log'
figs = []

x,y,theta =[],[],[]

for i,n in enumerate(name):
    for i in range(1,41):
        with open(n + '/' + n + str(i) + extension ,'r') as f:
            for l in f:
                a = l.split(' ')
                x.append(a[2])
                y.append(a[3])
                theta.append(a[4])
                
x = np.asarray(x,np.double)
y = np.asarray(y,np.double)
theta = np.asarray(theta,np.double)
data = np.c_[np.hypot(y,x),theta]
print data.shape
pcaObject = PCA(data)

projected_data = pcaObject.project(data)
projected_data = np.array(projected_data)
print projected_data
print projected_data[-1]
#plt.scatter(projected_data)
plt.scatter(projected_data[:][1],projected_data[:][0],color='r')
 
plt.xlim(2,-2)
plt.ylim(2,-2)

#ax.set_xticks(np.arange(0,7000,500))
#ax.set_yticks(np.arange(7000,0,-500))
plt.show()