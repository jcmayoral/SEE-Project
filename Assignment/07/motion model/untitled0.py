# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 12:01:50 2016

@author: chaitanya
"""

import numpy as np

path = "v2/"+"straight/"
data =  np.loadtxt(path+"straight24.log",delimiter=' ',usecols = (0,2,3,4))


px = []
py = []
p_omega = []
delta_t = []
for i in range(1,data.shape[0]):
    tempx = data[i][1] - data[i-1][1]
    tempy = data[i][2] - data[i-1][2]
    temp = data[i][3] - data[i-1][3]
    time = data[i][0] - data[i-1][0]
    px.append(tempx) 
    py.append(tempy)
    p_omega.append(temp)
    delta_t.append(time)



vx = np.asarray(px) / np.asarray(delta_t)
vy = np.asarray(py) / np.asarray(delta_t)
#omega = np.asarray(p_omega)/np.asarray(delta_t)

v = np.sqrt(vx*vx + vy*vy)

linear_v = np.max(v)
angular_w = np.max(omega)

print linear_v
print angular_w

    