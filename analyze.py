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

print 'test'

csvfile = csv.reader( open(filename,'r'), delimiter='\t')
csvfile.next()
for row in csvfile:
    x.append( float(row[0]) )
    y.append( float(row[1]) )
#for row in datafile.readlines():
        #row = row.strio().split('\t') # does this go here? My friend suggested it
	#x.append(float(row[1]))
	#y.append(-float(row[0]))
print row
print len(x)


# Smooth The data
binsize = 64
x2 = []
y2 = []
for i in range(binsize//2,len(x)-binsize//2):
	xtemp = x[i-binsize//2:i+binsize//2]
	ytemp = y[i-binsize//2:i+binsize//2]
	x2.append(sum(xtemp)/len(xtemp))
	y2.append(sum(ytemp)/len(ytemp))
print len(x2)

#Find Maximums
maxx = []
maxy = []
for n in range(1,len(x2)-1):
	if y2[n-1]<y2[n] and y2[n+1]<y2[n]:
		maxx.append(x2[n])
		maxy.append(y2[n])
print len(maxx)
#plt.figure(1, figsize=(5,4))
diffx = []
diffy = []
for n in range(2,len(maxx)):
    if math.fabs(maxx[n]-maxx[n-1]) > .1:
        ytemp = math.fabs(maxy[n] -maxy[n-1])
        xtemp = math.fabs(maxx[n] -maxx[n-1])
        diffx.append(xtemp)
        diffy.append(ytemp)
plt.scatter(maxx,maxy)
#plt.plot(x,y)
#plt.axis( (theta_exp[0],theta_exp[-1],0,1.1) )
plt.show()
print 'test'
