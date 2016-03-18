
import os
import sys
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

# In this case
# :Flyer per year
# :Video game hours
# :Liters of icecream

def loadData(filename):
	with open(filename, 'r') as fin:
		lines = fin.readlines()
		dataSet = np.zeros((len(lines), 3))
		labels  = []
		for i, line in enumerate(lines):
			ls = line.strip().split('\t')
			dataSet[i][0] = ls[0]    # Flyer
			dataSet[i][1] = ls[1]    # Video game
			dataSet[i][2] = ls[2]    # Liters of ice-cream
			labels.append(ls[3])
	return dataSet, labels

def drawDataSet(dataSet, labels):
	ic = [-1]
	def genColor():
		ic[0] += 1
		clrs = ['lightgreen', 'orange', 'red']   #purple, grey
		return clrs[ic[0]]
	dcMap = {}
	# On such a dimension...>>>>> 
	# 
	minVal = dataSet.min(0)     #All min value in their separate column
	maxVal = dataSet.max(0)     #All max value in their separate column
	rangeVal= maxVal - minVal   #The range
	dataSet = (dataSet - minVal) / rangeVal
	fig = plt.figure()
	ax = fig.add_subplot(111)
	xc, yc = {}, {}
	for i in range(dataSet.shape[0]):
		label = labels[i]
		if not label in dcMap:
			dcMap[label] = genColor()
		if not label in xc:
			xc[label], yc[label] = [], []
		xc[label].append(dataSet[i][0])
		yc[label].append(dataSet[i][1])

	print "###################"
	print "xc.keys = ", xc.keys()
	print "dcMap = ", dcMap

	types, titles  = [], []
	for label in dcMap.keys():
		color = dcMap[label]
		print label, color
		print 'count = %d, %d' % (len(xc[label]), len(yc[label]))
		types.append(ax.scatter(xc[label], yc[label], c = color, backgroundcolor="grey"))
		titles.append(label)
	
	ax.legend(types, titles, loc=2)
	ax.axis([0,1,0,1])
	plt.show()
	
if '__main__' == __name__:
	name = 'datingTestSet.txt'   # The default input(file path)
	if len(sys.argv) >= 2:
		name = sys.argv[1]
	print 'reading from %s' % name
	ds, ls = loadData(name)
	drawDataSet(ds, ls)
	
