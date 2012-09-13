#!/usr/bin/env python2
import csv
import matplotlib.pyplot as plt
import math
from matplotlib import rc
from pylab import *
from numpy import *

rc('font', **{'family':'sans-serif', 'sans-serif':['Helvetica']})
rc('text', usetex=True)
print 'test'

# Open the data
filename = 'Data1.txt'
#datafile = open(filename, 'r')
#datafile.readline()
x = []
y = []
csvfile = csv.reader( open(filename,'r'), delimiter='\t')
csvfile.next()
for row in csvfile:
    x.append( float(row[0]) )
    y.append( float(row[1]) )
print('length of x',len(x))


# Smooth The data
binsize = 8
x2 = []
y2 = []
for i in range(binsize//2,len(x)-binsize//2):
    xtemp = x[i-binsize//2:i+binsize//2]
    ytemp = y[i-binsize//2:i+binsize//2]
    x2.append(sum(xtemp)/len(xtemp))
    y2.append(sum(ytemp)/len(ytemp))
print len(x2)

#Find Maximums
maxx = [] #extrimums
maxy = []
minx = []
miny = []
for n in range(1,len(x2)-32):
    if y2[n-1]<y2[n] and y2[n+1]<y2[n] and y2[n-32]<y2[n] and y2[n+32]<y2[n]:
        maxx.append(x[n])
        maxy.append(y[n])
    if y2[n-1]>y2[n] and y2[n+1]>y2[n] and y2[n-32]>y2[n] and y2[n+32]>y2[n]:
        minx.append(x[n])
        miny.append(y[n])

print('maxx',len(maxx))
print('minx',len(minx))
timeofevent = x[-1] - x[1]
Peak = sum(maxy)/len(maxy) - sum(miny)/len(miny)
print('timeofevent =',timeofevent,'s')
print('Pk-Pk (V) =',Peak)
for i2 in range(1, len(maxx)):
    print repr(maxx[i2]).rjust(2), repr(maxy[i2]).rjust(3)
print '---------'
for n in range(1, len(minx)):
    print repr(minx[n]).rjust(2), repr(miny[n]).rjust(3)
plt.figure(1, figsize=(5,4))              
plt.xlabel('Measured Time (s)')
plt.ylabel('Detected Interference Intensity (V)')
plt.title('Interometry plot (fringes as arm pathlength changes)')
plt.scatter(maxx,maxy,color = 'r')
plt.scatter(minx,miny,color = 'g')
#plt.plot(x2,y2,ls='-',color = 'g')
#plt.plot(x,y,marker='o',ls='-')
plt.plot(x2,y2,ls='-')
#plt.scatter(x,y,marker='o', color ='b')
plt.show()
