

import matplotlib.pyplot as plt

decisionNode = dict(boxstyle="sawtooth", fc = "0.8")
leafNode     = dict(boxstyle="round4", fc = "0.8")
arrow_args   = dict(arrowstyle="<-")

def _firstKey(dc):
	for i in dc:
		return i
	raise RuntimeError("No hay lleva en el dict")


#Easy
def getNumLeafs(myTree):
	numLeafs = 0
	firstStr = _firstKey(myTree)
	secondDict = myTree[firstStr]
	for key in secondDict.keys():
		if type(secondDict[key]) == dict:
			numLeafs += getNumLeafs(secondDict[key])
		else:
			numLeafs += 1
	return numLeafs

def getBranches(myTree):
	numBranches = 0
	for k in myTree[_firstKey(myTree)]:
		numBranches += 1
	return numBranches

#Easy
def getTreeDepth(myTree):
	maxDepth = 0
	firstStr = _firstKey(myTree)
	secondDict = myTree[firstStr]
	for key in secondDict.keys():
		if type(secondDict[key]) == dict:
			thisDepth = 1 + getTreeDepth(secondDict[key])
		else:
			thisDepth = 1
		maxDepth = max(maxDepth, thisDepth)
	return maxDepth

class TreePlotter():
	def __init__(self):
		print("Initiation of TreePlotter")
		pass

	def startPlot(self, inTree):
		print("Drawing in TreePlotter!")
		self._fig = plt.figure(1, facecolor = 'white')
		#fig.clf()  # Don't know what it is.
		self.__ax1 = plt.subplot(111, **dict(frameon=False, xticks=[], yticks=[]))
		yInterv = 1.0 / getTreeDepth(inTree)   ## The span between two adjacent levels.
		xInterv = 0.5 / getNumLeafs(inTree)
		self.__plotTree(inTree
			, (0.5, 1.0)
			, ''
			, 1.0, yInterv
			, 0.5, xInterv
			, 1.0 # The full width (for you to split)
		)
		plt.show()  #And it is ready to show.

	def __plotMidText(self, cp, pp, txt):
		xm = (cp[0] - pp[0])/2.0 + pp[0]
		ym = (cp[1] - pp[1])/2.0 + pp[1]
		self.__ax1.text(xm, ym, txt)

	def __plotNode(self, nodeTxt, centerPt, parentPt, nodeType):
		self.__ax1.annotate(nodeTxt
			, xy = parentPt
		    , xycoords = "axes fraction"
			, xytext = centerPt
			, textcoords = 'axes fraction'
			, va = "center"
			, ha = "center"
			, bbox = nodeType  # decision-node or leaf-node
			, arrowprops=arrow_args
		)

	def __plotLeaf(self, nodeTxt, centerPt, parentPt, midText):
		self.__plotNode(nodeTxt, centerPt, parentPt, leafNode)
		self.__plotMidText( centerPt, parentPt, midText)

	def __plotTree(self, myTree, parentPt, nodeTxt, yCoord, yStep, xCoord, xStep, fullWidth):
		firstStr = _firstKey(myTree)   # Used to be
		cntrPt = (xCoord, yCoord)
		self.__plotMidText(cntrPt, parentPt, nodeTxt)
		self.__plotNode(firstStr, cntrPt, parentPt, decisionNode)
		secondDict = myTree[firstStr]
		
		leafsCount = getNumLeafs(myTree)
		xStart = xCoord - fullWidth * 0.5
		yStart = yCoord - yStep
		
		width = {}
		totWidth = 0
		for key, obj in secondDict.items():
			if type(obj) == dict:
				thisWidth  = getNumLeafs(obj)
				width[key] = thisWidth
				totWidth   += thisWidth
			else:
				totWidth += 1
				
		startWidth = 0
		for key, obj in secondDict.items():
			if type(obj) == dict:
				thisWidth = fullWidth * width[key] / totWidth
				self.__plotTree(secondDict[key], cntrPt, str(key)
					, yCoord - yStep, yStep
					, xStart + startWidth + thisWidth * 0.5, xStep
					, thisWidth
					)
			else:
				thisWidth = fullWidth / totWidth
				self.__plotLeaf(secondDict[key]
					, (xStart + startWidth + thisWidth * 0.5, yStart)
					, cntrPt
					, str(key)
				)
			startWidth += thisWidth

def grabTree(filepath):
	import pickle
	with open(filepath) as fin:
		return pickle.load(fin)