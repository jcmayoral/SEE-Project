import matplotlib.pyplot as plt
import numpy as np
from matplotlib.mlab import PCA

def extract (name):
    x,y,theta,sizes = [],[],[],[]
    x0,y0,th0 =  [],[],[]

    for i in range(1,41):
        size = 0;
        with open(name + '/' + name + str(i) + extension ,'r') as f:
            for l in f:
                size = size+1
        sizes.append(size)             
    samples = min(sizes)

    for i in range(1,41):
        with open(name + '/' + name + str(i) + extension ,'r') as f:
            for l in range(0,samples):
                a = f.readline().split(' ')
                x.append(a[2])
                y.append(a[3])
                theta.append(a[4])
    for z in xrange(0,len(x),samples):
        x0.append(x[z])
        y0.append(y[z])
        th0.append(theta[z])

    x0 = map(np.double,x0)
    y0 = map(np.double,y0)
    th0 = map(np.double,th0)
    x0 = np.mean(x0)
    y0 = np.mean(y0)
    th0 = np.mean(th0)
    
    x = process(map(np.double,x),x0)
    y = process(map(np.double,y),y0)
    theta = process(map(np.double,theta),th0)
    
    return x,y,theta,samples

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

for i,n in enumerate(name):
    x,y,theta,samples = extract(n)
    x = np.asarray(x,dtype=np.double)
    x = x-x[0]
    y = np.asarray(y,dtype=np.double)
    y = y - y[0]
    theta = np.asarray(y,dtype=np.double)
    #figs.append(plt.scatter(y,x,color=colors[i],s=1))    
    plt.plot(y,x,color=colors[i])
    plt.hold
    
    """    
    x = np.resize(x,(samples,40))
    y = np.resize(y,(samples,40))
    
    x_,y_ = [],[]

    for j in range(samples):
        data = np.c_[x[j,:],y[j,:]]
        #x1 = np.mean(x[j,:])
        #y1 = np.mean(y[j,:])
        pcaObject = PCA(data)
        projected_data = pcaObject.project(data)
        x1 = np.mean(x[j,:])
        y1 = np.mean(y[j,:])
        #x_.append(projected_data[0])
        #y_.append(projected_data[1])
        #plt.scatter(y1,x1,color=colors[i])
        plt.plot(projected_data[1],projected_data[0],color=colors[i])
        #plt.plot(pcaObject.mu[1],pcaObject.mu[0],color=colors[i])
    """
ax = plt.gca()
plt.xlim(3000,-3000)
plt.ylim(200,-3000)
#plt.xlim(100,-1000)
#plt.ylim(500,-500)

#ax.set_xticks(np.arange(0,7000,500))
#ax.set_yticks(np.arange(7000,0,-500))
plt.legend((figs),          
           (name),
           scatterpoints=1,
           loc='upper left',
           ncol=1,
           fontsize=16)
plt.show()

