

import trees_a
import treePlotter_a
#import treePlotter_a

if '__main__' == __name__:
    ds, ls = trees_a.createDataSet()
    mytree = trees_a.createTree(ds, ls); 
    tp = treePlotter_a.TreePlotter()
    tp.startPlot(mytree)


	

