#!/usr/bin/env python2
import csv
import matplotlib.pyplot as plt
from matplotlib import rc
from pylab import *
from numpy import *

rc('font', **{'family':'sans-serif', 'sans-serif':['Helvetica']})
rc('text', usetex=True)
print 'test'

# Open the data
filename = 'gas 10.txt'
#datafile = open(filename, 'r')
#datafile.readline()
x = []
y = []

print 'test'

csvfile = csv.reader( open(filename,'r'), delimiter='\t')
csvfile.next()
for row in csvfile:
    xtemp = float(row[0]) + float(row[1])/60
    x.append( xtemp )
    y.append( float(row[2]) )
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
# print 'test'

#Find Maximums
maxx = []
maxy = []
for n in range(1,len(x2)-1):
	if y2[n-1]<y2[n] and y2[n+1]<y2[n]:
		maxx.append(x2[n])
		maxy.append(y2[n])

plt.figure(1, figsize=(5,4))
#plt.scatter(x,y, linestyle='-'
plt.plot(x,y,marker='o',ls='-')
plt.plot(x2,y2,ls='-',c='red')
plt.xlabel('Measured Time (s)')
plt.ylabel('Detected Interference Intensity (V)')
plt.title('Interometry plot (fringes as arm pathlength changes)')



#plt.axis( (theta_exp[0],theta_exp[-1],0,1.1) )
plt.show()
print 'test'
