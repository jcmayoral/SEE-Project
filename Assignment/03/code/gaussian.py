# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 19:53:15 2016

@author: chaitanya
"""

import numpy as np
from matplotlib import pyplot as plt
from pyexcel_ods import get_data
from scipy.stats import norm
from matplotlib.mlab import PCA

def gaussian(x, mu, sig):
    return np.exp(-np.power(x - mu, 2.) / (2 * np.power(sig, 2.)))


                                 
def plot_hist(data,nbins):
    #plot the gaussian
    mu, std = norm.fit(data)
   
    # Plot the histogram.
    plt.hist(data, bins=nbins, normed=True, alpha=0.8, color='g')
    
    # Plot the PDF.
    #xmin, xmax = plt.xlim()
    val_min = np.min(data)
    val_max = np.max(data)
    x = np.linspace(val_min, val_max, 400)
    p = norm.pdf(x, mu, std)
    plt.plot(x, p, 'k', linewidth=2)
    #plt.plot(gaussian(np.linspace(val_min, val_max, 200),mu,std),'k',linewidth=2)
    title = "Fit results for steep left motion angular: mu = %.2f,  std = %.2f" % (mu, std)
    plt.title(title)
    plt.xlabel("Data")
    plt.ylabel("Density")
    #plt.show()
    #plt.savefig(path)

def do_pca(data):
    pcaObject = PCA(data)
    #centered_data = pcaObject.center(data)
    projected_data = pcaObject.project(data)
    #print projected_data
    plot_hist(projected_data[:,1],8)
    plt.show()
    

#convert from ordered dict to lists
straight_motion_data =  get_data("../measurements2/second_see_data_original.ods",start_row=5,
                                 row_limit=40,start_column=21,column_limit=4)
                                 
data = straight_motion_data.get("Sheet1")
#dataMatrix = np.array(data)

data_front_x = list()
data_front_y = list()
data_back_x = list()
data_back_y = list()
for x in range(0,40):
    temp = data[x]
    data_front_x.append(temp[0])
    data_front_y.append(temp[1])
    data_back_x.append(temp[2])
    data_back_y.append(temp[3])

robot_center_x = np.asarray(data_back_x) + (( np.asarray(data_front_x) -  np.asarray(data_back_x))/2)
robot_center_y = np.asarray(data_back_y) + (( np.asarray(data_front_y) -  np.asarray(data_back_y))/2)
robot_pose_angular = np.round(np.degrees(np.arctan2(robot_center_x,robot_center_y)),2)
robot_pose_linear = np.round(np.sqrt(robot_center_x*robot_center_x + robot_center_y*robot_center_y),2)

data = np.c_[robot_pose_linear,robot_pose_angular]
do_pca(data)

#path = "/home/chaitanya/MAS3/SEE-Project/Assignment/03/diagrams"
#plot_hist(robot_center_y,4)
#plt.show()
#plt.savefig(path)



    
