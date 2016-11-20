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

name = ['straight','slightleft','slightright','steepleft','steepright']
colors=['r','b','y','c','g']
extension = '.log'
figs = []

for i,n in enumerate(name):
    x,y,theta,samples = extract(n)
    x = np.asarray(x,dtype=np.double)
    x = np.reshape(x,(samples,40))
    y = np.reshape(y,(samples,40))
    y = np.asarray(y,dtype=np.double)
    theta = np.asarray(y,dtype=np.double)
    figs.append(plt.scatter(y,x,color=colors[i],s=4))
    
    #print n,
#    for i in range(samples):
#        data = np.c_[x[i,:,],y[i,:]]
#        pcaObject = PCA(data)
#        projected_data = pcaObject.project(data)
#        print i, " of " , samples
#        print "mean", pcaObject.mu, " standard deviation" ,pcaObject.sigma
    #print n, projected_data[:][1]
    #figs.append(plt.scatter(projected_data[:][0],projected_data[:][1],color=colors[i]))


ax = plt.gca()
plt.xlim(1000,-1000)
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

