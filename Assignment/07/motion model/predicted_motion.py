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
 

def sample_motion_model_velocity(ut,x_prevt,alphas,delta_t):
    var1 = alphas[0]*(ut[0]*ut[0]) + alphas[1]*(ut[1]*ut[1])
    var2 = alphas[2]*(ut[0]*ut[0]) + alphas[3]*(ut[1]*ut[1])
    var3 = alphas[4]*(ut[0]*ut[0]) + alphas[5]*(ut[1]*ut[1])
    v_hat = ut[0] + np.random.normal(0,var1)
    omega_hat = ut[1] + np.random.normal(0,var2)
    gamma_hat = np.random.normal(0,var3)
    
    xt = x_prevt[0] - (v_hat/omega_hat)*np.sin(x_prevt[2]) + (v_hat/omega_hat)*np.sin(x_prevt[2] + (omega_hat*delta_t))
    yt = x_prevt[1] + (v_hat/omega_hat)*np.cos(x_prevt[2]) - (v_hat/omega_hat)*np.cos(x_prevt[2] + (omega_hat*delta_t))
    theta = x_prevt[2] + (omega_hat*delta_t) +(gamma_hat*delta_t)
    
    return np.array([xt,yt,theta])     

def get_sampled_data():
    directory_names = ['straight', 'slightleft', 'slightright', 'steepleft', 'steepright']
#    v = [-22., -24., -17., -18., -17.]
#    omega = [ 0., np.radians(-48.), np.radians(-24.), np.radians(48.), np.radians(24.)]
    v = [-10., -10., -10., -10., -10.]
    omega = [0., np.radians(10/120), np.radians(-10/120), np.radians(10/40), np.radians(-10/40)]
    
    data = calculate_alphas.read_data(directory_names)
    alphas = calculate_alphas.estimate_alphas(data)
    print alphas
    pose = np.array([0.,0.,0.])
    newdata = list()
    for i, trajectories in enumerate(data.trajectories):
        motion_model_data = list()
        for j, trajectory in enumerate(trajectories):
            temp = list()
            temp.append(pose)
            for k in xrange(len(trajectory)-1):
                    delta_t = data.time_deltas[i][j][k]
                    mmv = sample_motion_model_velocity((v[i], omega[i]), temp[k],alphas,delta_t)
                    temp.append(mmv)
            motion_model_data.append(temp)
        newdata.append(motion_model_data)
        
                #print i,j,k
    newdata = np.array(newdata)
    return newdata      

if __name__ == "__main__":
    motion_model_data = get_sampled_data()
    directory_names = ['straight', 'slightleft', 'slightright', 'steepleft', 'steepright']
    colors=['r','b','y','c','g']
    
    for i,trajectories in enumerate(motion_model_data):
        x = []
        y = []
        theta = []
        endpose = []
        for j,trajectory in enumerate(trajectories):
            for k,pose in enumerate(trajectory):
                x.append(pose[0])
                y.append(pose[1])
                theta.append(pose[2])
            endpose.append(pose)
        
        #plot the data
        plt.scatter(x,y,color=colors[i],s=4)
    #print len(motion_model_data)
  

    #process the data
    
    
    #plot the sampled data
    
    #plt.scatter(motion_model_data[:,0],motion_model_data[:,1])
#    motion_times = []
#    for i,val in enumerate(duration):
#        time = []
#        for j,temp in enumerate(val):
#            for k,tempval in enumerate(temp):
#                time.append(tempval)
#        if( (i+1) %40 == 0):
#            motion_times.append(time)
##    motion_times = observed_motion.processdata(duration)
#    predicted_data = []
#    for i,trajectorytime in enumerate(motion_times):    
#        posex = [0.]
#        posey = [0.]
#        posetheta = [0.]
#        
#        tempx = 0.
#        tempy = 0.
#        temptheta = 0.
#        for j,temp in enumerate(trajectorytime):
#            tempx,tempy,temptheta = find_pose(v[i],omega[i],temp,
#                                             tempx,tempy,temptheta)
#            
#            posex.append(tempx)
#            posey.append(tempy)
#            posetheta.append(temptheta)
#        
#        data = np.c_[posex,posey,posetheta]
#        predicted_data.append(data)
#        plt.scatter(posex,posey,color=colors[i],s=4)
    
    
    
    
    
     
    
    
    