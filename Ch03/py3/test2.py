

import trees
import treePlotter

if '__main__' == __name__:
	with open('lenses.txt') as fin:
		lenses = [inst.strip().split('\t') for inst in fin.readlines()]
	labels = ['age', 'prescript', 'astigmatic', 'tear-rate']
	decisionTree = trees.createTree(lenses, labels)
	treePlotter.createPlot(decisionTree)
