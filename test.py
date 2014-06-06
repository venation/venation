def req(xx, yy):
	print xx, yy
	def func(args):
		print xx, yy
		return func
	return func
	
	
@req(5,6)
def a(x, y):
	return x, y
	
	
print a(1,2)
# 
# 
# 
# func(a)(1,2)