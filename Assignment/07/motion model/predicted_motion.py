# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 15:57:25 2016

@author: chaitanya
"""

import numpy as np
import calculate_alphas
import observed_motion

from matplotlib import pyplot as plt

def find_pose(linear_velocity,angular_velocity,delta_time,
              prev_posex,prev_posey,prev_posetheta):
    
    posex = prev_posex + linear_velocity * np.cos(prev_posetheta) * delta_time
    posey = prev_posey + linear_velocity * np.sin(prev_posetheta) * delta_time
    posetheta = prev_posetheta + angular_velocity * delta_time
    return posex,posey,np.radians(posetheta)
                

if __name__ == "__main__":
    directory_names = ['straight', 'slightleft', 'slightright', 'steepleft', 'steepright']
    v = [-22., -24., -17., -18., -17., -18.]
    omega = [0., 0., np.radians(-48.), np.radians(-24.), np.radians(48.), np.radians(24.)]
    colors=['r','b','y','c','g']
    
    data = calculate_alphas.read_data(directory_names)
    duration = data.time_deltas
    motion_times = []
    for i,val in enumerate(duration):
        time = []
        for j,temp in enumerate(val):
            for k,tempval in enumerate(temp):
                time.append(tempval)
        if( (i+1) %40 == 0):
            motion_times.append(time)
#    motion_times = observed_motion.processdata(duration)
    predicted_data = []
    for i,trajectorytime in enumerate(motion_times):    
        posex = [0.]
        posey = [0.]
        posetheta = [0.]
        
        tempx = 0.
        tempy = 0.
        temptheta = 0.
        for j,temp in enumerate(trajectorytime):
            tempx,tempy,temptheta = find_pose(v[i],omega[i],temp,
                                             tempx,tempy,temptheta)
            
            posex.append(tempx)
            posey.append(tempy)
            posetheta.append(temptheta)
        
        data = np.c_[posex,posey,posetheta]
        predicted_data.append(data)
        plt.scatter(posex,posey,color=colors[i],s=4)
    
    
    
    
    
     
    
    
    