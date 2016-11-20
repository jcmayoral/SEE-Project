# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 14:22:21 2016

@author: chaitanya
"""

import numpy as np
import calculate_alphas
import gaussian

from matplotlib import pyplot as plt



"""
Processing part
"""
def processdata(end_pose):
    trajectories = []
    temp = []
    for i,motion in enumerate(end_pose):
        if((i+1) % 40 == 0):
            temp.append(motion)
            trajectories.append(temp)
            temp = list()
        else:
            temp.append(motion)
    return trajectories

"""
Fit multi-variate gaussian 
"""
def fit_gaussian(trajectories,motions):
    for i,trajectory in enumerate(trajectories):
        datax = []
        datay = []
        datatheta = []
        for j,temp in enumerate(trajectory):
            #print temp[j][0]
            datax.append(temp[j][0])
            datay.append(temp[j][1])
            datatheta.append(temp[j][2])
        dataposition = np.c_[datax,datay]
        dataorientation = np.array(datatheta)
        projected_data_position = gaussian.do_pca(dataposition)
        #projected_data_theta = gaussian.do_pca(dataorientation)
        gaussian.plot_hist(projected_data_position,0,4,motions[i]+" motion along x-axis")
        gaussian.plot_hist(projected_data_position,1,4,motions[i]+" motion along y-axis")    



if __name__ == "__main__":
    directory_names = ['straight', 'slightleft', 'slightright', 'steepleft', 'steepright']

    data = calculate_alphas.read_data(directory_names)
    end_pose =  data.trajectories_end
    trajectories = processdata(end_pose)
    fit_gaussian(trajectories,directory_names)
        
#for i, trajectories in enumerate(data.trajectories):
#    for j, trajectory in enumerate(trajectories):
#        for k in xrange(len(trajectory)-1):
#            if(i<5):
#                delta_t = data.time_deltas[i][j][k]
                

