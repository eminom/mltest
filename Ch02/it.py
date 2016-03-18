

import numpy as np
a = np.array([[1.0, 1.1], [1.0, 1.0], [0,0], [0, 0.1]])
assert len(a.shape) == 2, "Length must be 2"

print a

for i in range(0, a.shape[0]):
	for j in range(0, a.shape[1]):
		print a[i,j]

