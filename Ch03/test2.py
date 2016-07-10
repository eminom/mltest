
import treePlotter_a as treePlotter
#import treePlotter
import trees_a as tree

if '__main__' == __name__:
	tp = treePlotter.TreePlotter()
	with open('lenses.txt') as fin:
		dataSet = [inst.strip().split('\t') for inst in fin.readlines()]
	labels = ['age', 'prescript', 'astigmatic', 'tearRate']
	decT = tree.createTree(dataSet, labels)
	createPlot = tp.startPlot
	#createPlot = treePlotter.createPlot
	createPlot(decT)