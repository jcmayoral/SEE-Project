# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 15:20:21 2016

@author: jose
"""

import matplotlib.pyplot as plt
import numpy as np

x,y,theta = [],[],[]

with open('data','r') as f:
    for l in f:
        a = l.split('\t')
        x.append(a[0])
        y.append(a[1].rstrip())

plt.grid('on')
plt.title('Experiment Results')
plt.xlabel('Y World Axis (in cm)')
plt.ylabel('X World Axis (in cm)')
plt.axes().set_aspect('equal')
dt = plt.scatter(y,x,color='b')
print "done all"

x,y,theta = [],[],[]

with open('initPose','r') as f:
    for l in f:
        a = l.split('\t')
        x.append(a[0])
        y.append(a[1].r strip())

dt = plt.scatter(y,x,color='y')

x,y,theta = [],[],[]
with open('center','r') as f:
    for l in f:
        a = l.split('\t')
        x.append(a[0])
        y.append(a[1].rstrip())
  
#plt.grid('on')
#plt.title('ALL Coordinates')
#plt.xlabel('Y World Axis')
#plt.ylabel('X World Axis')
ct = plt.scatter(y,x,color='r')
plt.autoscale()
plt.legend((dt,ct),
           ('Sensors Poses', 'Center pose'),
           scatterpoints=1,
           #loc='lower right',
           ncol=2,
           fontsize=8)
plt.xlim(-30,30)
plt.ylim(-10,80)



"""
with open('sharp_left','r') as f:
    for l in f:
        a = l.split('\t')
        x.append(a[0])
        y.append(a[1])
        theta.append(a[2].rstrip())

x = np.asarray(x, dtype=np.double)
y = np.asarray(y, dtype=np.double)
theta = np.asarray(theta, dtype=np.double)
#plt.title("Histograms Straight")
#plt.hist(x, 10)
#plt.hist(y, 10)
#plt.hist(theta, 10)
"""
"""
x = np.asarray(x[0:40], dtype=np.double)
y = np.asarray(y[0:40], dtype=np.double)
theta = np.asarray(theta, dtype=np.double)
"""
"""
fig = plt.figure()
plt.title('Histogram')
ax = fig.add_subplot(131)
ax.hist(x,9,color='blue',alpha=0.8)
ax = fig.add_subplot(132)
ax.hist(y,8,color='red',alpha=0.8)
ax = fig.add_subplot(133)
ax.hist(theta,8,color='green',alpha=0.8)
plt.show()

print "done all"
"""