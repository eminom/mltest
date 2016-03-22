


import matplotlib.pyplot as plt

decisionNode = dict(boxstyle="sawtooth", fc = "0.8")
leafNode = dict(boxstyle="round4", fc = "0.8")
arrow_args = dict(arrowstyle="<-")

def plotNode(nodeTxt, centerPt, parentPt, nodeType):
	createPlot.ax1.annotate(nodeTxt
		, xy = parentPt
	  , xycoords = "axes fraction"
		, xytext = centerPt
		, textcoords = 'axes fraction'
		,	va = "center"
		, ha = "center"
		, bbox = nodeType,  # decision-node or leaf-node
		arrowprops=arrow_args
	)

"""
def createPlot():
	fig = plt.figure(1, facecolor='white')
	fig.clf()
	createPlot.ax1 = plt.subplot(111, frameon=False)
	plotNode('a decision node', (0.5, 0.1), (0.1, 0.5), decisionNode)
	plotNode('a leaf node', (0.8, 0.1), (0.3, 0.8), leafNode)
	plt.show()
"""


#Easy
def getNumLeafs(myTree):
	numLeafs = 0
	firstStr = myTree.keys()[0]
	secondDict = myTree[firstStr]
	for key in secondDict.keys():
		if type(secondDict[key]).__name__ == 'dict':
			numLeafs += getNumLeafs(secondDict[key])
		else:
			numLeafs += 1
	return numLeafs

#Easy
def getTreeDepth(myTree):
	maxDepth = 0
	firstStr = myTree.keys()[0]
	secondDict = myTree[firstStr]
	for key in secondDict.keys():
		if type(secondDict[key]).__name__ == 'dict':
			thisDepth = 1 + getTreeDepth(secondDict[key])
		else:
			thisDepth = 1
		maxDepth = max(maxDepth, thisDepth)
	return maxDepth

#cp: center point
#pp: point, just point
def plotMidText(cp, pp, txt):
	xm = (cp[0] - pp[0])/2.0 + pp[0]
	ym = (cp[1] - pp[1])/2.0 + pp[1]
	createPlot.ax1.text(xm, ym, txt)

def plotTree(myTree, parentPt, nodeTxt):
	numLeafs = getNumLeafs(myTree)
	#getTreeDepth(myTree)   # What's the use of this line.
	firstStr = myTree.keys()[0]

	cntrPt = (
	  plotTree.xOff + (1.0 + float(numLeafs)) * (1.0 / plotTree.totalW) / 2.0,
		plotTree.yOff
	)

	plotMidText(cntrPt, parentPt, nodeTxt)
	plotNode(firstStr, cntrPt, parentPt, decisionNode)
	secondDict = myTree[firstStr]

	yStep = 1.0 / plotTree.totalD
	xStep = 1.0 / plotTree.totalW

	plotTree.yOff = plotTree.yOff - yStep

	for key in secondDict.keys():
		if type(secondDict[key]).__name__ == 'dict':
			plotTree(secondDict[key], cntrPt, str(key))
		else:
			plotTree.xOff = plotTree.xOff + xStep
			#@ 
			plotNode(secondDict[key], (plotTree.xOff, plotTree.yOff),
				cntrPt, leafNode)
			plotMidText( (plotTree.xOff, plotTree.yOff), cntrPt, str(key))

	plotTree.yOff = plotTree.yOff + yStep
	# y-step
	# OK. You are good to go

def createPlot(inTree):
	fig = plt.figure(1, facecolor = 'white')
	#fig.clf()
	axprops         = dict(xticks=[], yticks=[])
	createPlot.ax1  = plt.subplot(111, frameon = False, **axprops)
	plotTree.totalW = float(getNumLeafs(inTree))
	plotTree.totalD = float(getTreeDepth(inTree))
	plotTree.xOff   = -0.5/plotTree.totalW
	plotTree.yOff   = 1.0
	plotTree(inTree, (0.5, 1.0), '')
	plt.show()
