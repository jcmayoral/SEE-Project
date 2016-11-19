# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 19:53:15 2016

@author: chaitanya
"""

import numpy as np
from matplotlib import pyplot as plt
#from pyexcel_ods import get_data
from scipy.stats import norm
from matplotlib.mlab import PCA
from scipy import optimize


def gaussian_func(height, center_x, center_y, width_x, width_y):
    """Returns a gaussian function with the given parameters"""
    width_x = float(width_x)
    width_y = float(width_y)
    return lambda x,y: height*np.exp(
                -(((center_x-x)/width_x)**2+((center_y-y)/width_y)**2)/2)

def moments(data):
    """Returns (height, x, y, width_x, width_y)
    the gaussian parameters of a 2D distribution by calculating its
    moments """
    total = data.sum()
    X, Y = np.indices(data.shape)
    x = (X*data).sum()/total
    y = (Y*data).sum()/total
    col = data[:, int(y)]
    width_x = np.sqrt(np.abs((np.arange(col.size)-y)**2*col).sum()/col.sum())
    row = data[int(x), :]
    width_y = np.sqrt(np.abs((np.arange(row.size)-x)**2*row).sum()/row.sum())
    height = data.max()
    return height, x, y, width_x, width_y

def fitgaussian(data):
    """Returns (height, x, y, width_x, width_y)
    the gaussian parameters of a 2D distribution found by a fit"""
    params = moments(data)
    errorfunction = lambda p: np.ravel(gaussian_func(*p)(*np.indices(data.shape)) -
                                 data)
    p, success = optimize.leastsq(errorfunction, params)
    return p


                                 
def plot_hist(data,index,nbins,motion):
    #plot the gaussian
    mu, std = norm.fit(data[:,index])
   
    # Plot the histogram.
    fig = plt.figure()
    plt.hist(data[:,index], bins=nbins, normed=True, alpha=0.8, color='g')
    
    # Plot the PDF.
    #xmin, xmax = plt.xlim()
    val_min = np.min(data[:,index])
    val_max = np.max(data[:,index])
    x = np.linspace(val_min, val_max, 800)
    p = norm.pdf(x, mu, std)
    
    
    plt.plot(x, p, 'k', linewidth=2)
    #plt.plot(gaussian(np.linspace(val_min, val_max, 200),mu,std),'k',linewidth=2)
    title = "Fit results for "+motion+" : mu = %.2f,  std = %.2f" % (mu, std)
    plt.title(title)
    plt.xlabel("Data")
    plt.ylabel("Density")
    plt.show()
    #plt.savefig(path)
    return fig

def do_pca(data):
    pcaObject = PCA(data)
    #centered_data = pcaObject.center(data)
    projected_data = pcaObject.project(data)
    #print projected_data
    #plot_hist(projected_data[:,index],4)
    #plt.show()
    return projected_data
    
if __name__ == "__main__":
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
    do_pca(data,0)

#path = "/home/chaitanya/MAS3/SEE-Project/Assignment/03/diagrams"
#plot_hist(robot_center_y,4)
#plt.show()
#plt.savefig(path)



    
