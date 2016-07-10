
#This test goes with Python3
import trees
import treePlotter

if '__main__' == __name__:
	dataSet, labels = trees.createDataSet()
	decisionTree = trees.createTree(dataSet, labels)
	treePlotter.createPlot(decisionTree)
