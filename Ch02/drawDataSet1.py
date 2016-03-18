
# Draw the data set from dating test data set.
# So the axis of x and y are predefined.

import os
import sys
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

def drawNow(dataSet):
	ic = [-1]
	def genColor():
		ic[0] += 1
		clrs = ['lightgreen', 'orange', 'red']   #purple, grey
		return clrs[ic[0]]
	fig = plt.figure()
	ax = fig.add_subplot(111)
	types, titles = [], []
	for kind in dataSet:
		types.append(ax.scatter(dataSet[kind][:,0], dataSet[kind][:,1], c=genColor(), s=40))
		titles.append(kind)
	ax.legend(types, titles, loc=2)
	ax.axis([0,1,0,1])
	plt.xlabel('Frequent Flyier Miles Earned Per Year')
	plt.ylabel('Percentage of Time Spent Playing Video Games')
	plt.show()

# In this case
# :Flyer per year
# :Video game hours
# :Liters of icecream

def loadData(filename):
	with open(filename, 'r') as fin:
		lines = fin.readlines()
		dataSet = {}
		for i, line in enumerate(lines):
			ls = line.strip().split('\t')
			# Assign a numpy array from a python array
			# They must have the same column.
			# (Or exception occurs)
			kind = ls[3]
			if not kind in dataSet:
				dataSet[kind] = []
			dataSet[kind].append([float(i) for i in ls[:3]])    # Flyer
	# And finally.
	for label in dataSet:
		dataSet[label] = np.array(dataSet[label])
	return dataSet

def doNormalize(dataSet):
	minVal = []
	maxVal = []
	for kind in dataSet:
		ds = dataSet[kind]
		minVal.append(ds.min(0))
		maxVal.append(ds.max(0))
		#print "maxVal = ", maxVal
		#rangeVal = maxVal - minVal
	minVal = np.array(minVal).min(0)
	maxVal = np.array(maxVal).max(0)
	#print(minVal)
	#print(maxVal)
	for kind in dataSet:
		ds = dataSet[kind]
		mini = np.tile(minVal, (ds.shape[0],1))
		maxi = np.tile(maxVal, (ds.shape[0],1))
		rang = maxi - mini
		ds = (ds-mini)/rang  #And this is new
		dataSet[kind] = ds   #Write back


#		dataSet[kind] = (ds-minVal) / rangeVal

if '__main__' == __name__:
	name = 'datingTestSet.txt'   # The default input(file path)
	if len(sys.argv) >= 2:
		name = sys.argv[1]
	print 'reading from %s' % name
	ds = loadData(name)
	doNormalize(ds)
	drawNow(ds)	
