'''
Created on Oct 6, 2010
@author: Peter
'''

import os, sys
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

scalar1, scalar2, scalar3 = 30,  30,  30
color1 , color2,  color3  = 'red','green','blue'

def GenData(n, fout):
	markers = []
	colors = []
	xcord, ycord = np.zeros(n), np.zeros(n)
	for i in range(n):
		[r0, r1] = np.random.standard_normal(2)
		r = np.random.uniform(0, 1)
		if r <= 0.16:
			fFlyer = np.random.uniform(22000, 60000)
			tats = 3 + 1.6 * r1
			markers.append(scalar1)
			colors.append(color1)
			classLabel = 1
			#print "%d, %f, class1" % (fFlyer, tats)

		elif r <= 0.33:
			fFlyer = 6000 * r0 + 70000
			tats = 10 + 3 * r1 + 2 * r0
			markers.append(scalar2)
			colors.append(color2)
			classLabel = 1
			#print '%d, %f, class1' % (fFlyer, tats)

		elif r <= 0.66:
			fFlyer = 5000 * r0 + 10000
			tats = 3 + 2.8 * r1
			markers.append(scalar2)
			colors.append(color2)
			classLabel = 2
			#print '%d, %f, class' % (fFlyer, tats)
		
		else:
			fFlyer = 10000 * r0 + 35000
			tats = 10 + 2.0 * r1
			markers.append(scalar3)
			colors.append(color3)
			classLabel = 3 # 'largeDoses'
			#print ('%d, %f, class3') % (fFlyer, tats)
		xcord[i], ycord[i] = max(fFlyer, 0), max(tats, 0)
		fout.write('%d\t%f\t%f\t%d\n' % (fFlyer, tats, np.random.uniform(0.0, 1.7), classLabel))

	return xcord, ycord, markers, colors

if '__main__' == __name__:
	cnt = 100
	with open('testSet.txt', 'w') as fw:
		xcord, ycord, markers, colors = GenData(cnt, fw)
	fig = plt.figure()
	ax = fig.add_subplot(111, axisbg='grey')
	#print(markers)
	#print(colors)
	#print 'len of markers is %d' % len(markers)
	#print 'len of colors  is %d' % len(colors)
	#print 'len of xcord   is %d' % len(xcord)
	#print 'len of ycord   is %d' % len(ycord)
	#print(markers)
	#sys.exit()

	ax.scatter(xcord, ycord, c = colors, s = markers)
	type1 = ax.scatter([-10], [-10], s=scalar1, c='red')
	type2 = ax.scatter([-10], [-15], s=scalar2, c='blue')
	type3 = ax.scatter([-10], [-20], s=scalar3, c='green')
	ax.legend([type1, type2, type3], ["Class 1", "Class 2", "Class 3"], loc=2)
	ax.axis([-5000,100000,-2,25])
	#ax.axis([-50000,100000, 0,25])    #Exactly the range of what you specify

	plt.xlabel('Frequent Flyier Miles Earned Per Year')
	plt.ylabel('Percentage of Body Covered By Tatoos')
	plt.show()
