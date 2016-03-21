

import trees_a
import treePlotter_a


if '__main__' == __name__:
	ds, ls = trees_a.createDataSet()
	mytree = trees_a.createTree(ds, ls)
	treePlotter_a.createPlot(mytree)
	

