'''
Created on Oct 6, 2010

@author: Peter
'''

import os
import sys
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
#from matplotlib.patches import Rectangle

s1, s2, s3, s4 = 20, 30, 50, 120
c1, c2, c3, c4 = 'red', 'yellow', 'lightgreen', 'purple'

def GenData(n, fout):
	xcord1, ycord1 = [], []
	xcord2, ycord2 = [], []
	xcord3, ycord3 = [], []
	markers = []
	colors  = []
	classT  = 0
	for i in range(n):
		del classT
		[r0, r1] = np.random.standard_normal(2)
		cr = np.random.uniform(0, 1)
		if cr <= 0.16:
			flyer = np.random.uniform(22000, 60000)
			tat   = 3 + 1.6 * r1
			markers.append(s1)
			colors.append(c1)
			xcord1.append(max(flyer,0))
			ycord1.append(max(tat,0))
			classT = 1

		elif cr <= 0.33:
			flyer = 6000 * r0 + 70000
			tat   = 10 + 3 * r1 + 2 * r0
			markers.append(s1)
			colors.append(c2)
			xcord1.append(max(flyer,0))
			ycord1.append(max(tat,0))
			classT = 2

		elif cr <= 0.66:
			flyer = 5000 * r0 + 10000
			tat   = 3 + 2.8 * r1
			markers.append(s2)
			colors.append(c2)
			xcord2.append(max(flyer,0))
			ycord2.append(max(tat,0))
			classT = 2

		else:
			flyer = 10000 * r0 + 35000
			tat   = 10 + 2.0 * r1
			markers.append(s3)
			colors.append(c3)
			xcord3.append(max(flyer,0))
			ycord3.append(max(tat,  0))
			classT = 3
		fout.write('%d\t%f\t%d\n' % ( flyer, tat, classT))
	return xcord1, ycord1, xcord2, ycord2, xcord3, ycord3, markers, colors

def makeArrayNorm(arr, lo, hi):
	for i, e in enumerate(arr):
		arr[i] =  (arr[i]-lo)/(hi-lo)
	return arr

if '__main__' == __name__:
	#print len(sys.argv)
	#sys.exit()
	if len(sys.argv) < 2:
		#print "Need to know the output file name"
		#sys.exit()
		filepath = 'ds1.txt'
	else:
		#print "getting file name from sys.argv"
		filepath = sys.argv[1]
		try:
			if os.stat(filepath):
				print "File already exists"
				sys.exit()
			#print "write to %s" % filepath
		except OSError:
			print "File not exists"
			pass
	
	with open(filepath, 'w') as fout:
		xv1, yv1, xv2, yv2, xv3, yv3, markers, colors = GenData(10000, fout)

	fig = plt.figure()
	ax = fig.add_subplot(111)

	x_lo = min(min(xv1), min(xv2), min(xv3))
	x_hi = max(max(xv1), max(xv2), max(xv3))

	y_lo = min(min(yv1), min(yv2), min(yv3))
	y_hi = max(max(yv1), max(yv2), max(yv3))

	showMe = False
	showInNorm = True

	if showInNorm:
		makeArrayNorm(xv1, x_lo, x_hi)
		makeArrayNorm(xv2, x_lo, x_hi)
		makeArrayNorm(xv3, x_lo, x_hi)
		makeArrayNorm(yv1, y_lo, y_hi)
		makeArrayNorm(yv2, y_lo, y_hi)
		makeArrayNorm(yv3, y_lo, y_hi)

	#OK, here I come.
	xm = np.random.uniform(x_lo, x_hi)
	ym = np.random.uniform(y_lo, y_hi)

	type1 = ax.scatter(xv1, yv1, s=s1, c=c1)
	type2 = ax.scatter(xv2, yv2, s=s2, c=c2)
	type3 = ax.scatter(xv3, yv3, s=s3, c=c3)
	types = [type1, type2, type3]
	labels= ['Did Not Like', 'Liked in Small Doses', 'Liked in Large Doses']
	
	if showMe:
		type_me = ax.scatter([xm], [ym], s=s4, c=c4)
		types.append(type_me)
		labels.append('Me')

	# And now here I come
	#type4 = ax.scatter(
	ax.legend(types, labels, loc=2)

	if not showInNorm:
		#ax.axis([-5000,100000,-2,25])
		#ax.axis([x_lo, x_hi, y_lo, y_hi])
		pass
	else:
		ax.axis([0,1,0,1])

	plt.xlabel('Frequent Flyier Miles Earned Per Year')
	plt.ylabel('Percentage of Time Spent Playing Video Games')
	plt.show()
