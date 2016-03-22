
from math import log

def calcShannonEnt(dataSet):
	numEntries = len(dataSet)
	labelCounts = {}
	for featVec in dataSet:
		currentLabel = featVec[-1]
		labelCounts[currentLabel] = labelCounts.get(currentLabel,0) + 1
	shannonEnt = 0.0
	for key in labelCounts:
		prob = float(labelCounts[key])/numEntries
		shannonEnt -= prob * log(prob, 2)
	return shannonEnt

def splitDataSet(dataSet, axis, value):
	retDataSet = []
	for featVec in dataSet:
		if featVec[axis] == value:
			reducedFeatVec = featVec[:axis]
			reducedFeatVec.extend(featVec[axis+1:])
			retDataSet.append(reducedFeatVec)
	return retDataSet
	
def chooseBestFeatureToSplit(dataSet):
	numFeatures = len(dataSet[0]) - 1     #The last column is the `label'
	baseEntropy = calcShannonEnt(dataSet)
	bestInfoGain = 0.0
	bestFeature = -1
	for i in range(numFeatures):
		featList = [example[i] for example in dataSet]
		uniqueVals = set(featList)
		newEntropy = 0.0
		pa = 0.0
		for value in uniqueVals:
			subDataSet =  splitDataSet(dataSet, i, value)
			prob = len(subDataSet) / float(len(dataSet))
			pa += prob
			newEntropy += prob * calcShannonEnt(subDataSet)
		assert pa == 1.0, "Must be equal to 1"
		infoGain = baseEntropy - newEntropy
		if (infoGain > bestInfoGain):
			bestInfoGain = infoGain
			bestFeature  = i
	return bestFeature

def majorityCnt(classList):
	classCount = {}
	for vote in classList:
		if vote not in classCount.keys(): classCount[vote] = 0
		classCount[vote] += 1
	sortedClasssCount = sorted(classCount.iteritems(),
		key = operator.itemgetter(1), reverse = True)
	return sortedClassCount[0][0]

# data-set is an array
# labels: name for each attributes (column)
# 
def createTree(dataSet, labels):
	classList = [example[-1] for example in dataSet]
	if classList.count(classList[0]) == len(classList):
		return classList[0]
	if len(dataSet[0]) == 1:
		return majorityCnt(classList)
	# Return value is an index(for the column of the attribute)
	bestFeat = chooseBestFeatureToSplit(dataSet)
	bestFeatLabel = labels[bestFeat]
	myTree = {bestFeatLabel:{}}
	del labels[bestFeat]
	featValues = [example[bestFeat] for example in dataSet]
	uniqueVals = set(featValues)
	for value in uniqueVals:
		subLabels = labels[:]
		myTree[bestFeatLabel][value] = createTree(splitDataSet(dataSet,\
			bestFeat, value), subLabels)
	return myTree

def createDataSet():
	dataSet = [[1, 1, 'yes'],
		[1, 1, 'yes'],
		[1, 0, 'no'],
		[0, 1, 'no'],
		[0, 1, 'no']]
	labels = ['no surfacing', 'flippers']
	return dataSet, labels

if '__main__' == __name__:
	ds, ls = createDataSet()
	print "Ent is %f" % calcShannonEnt(ds)
