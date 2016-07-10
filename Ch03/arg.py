def f(a, b, c):
	print("a = %d" % a)
	print("b = %d" % b)
	print("c = %d" % c)
	print("")
	
def test_f():
	d = (5, 7, 11)
	f(*d)
	
if '__main__' == __name__:
	test_f()
	


	
	
	