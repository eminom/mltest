

def f1():
	b = [-1]
	def r():
		b[0] += 1
		return b[0]
	return r

f = f1()
print f()
print f()
