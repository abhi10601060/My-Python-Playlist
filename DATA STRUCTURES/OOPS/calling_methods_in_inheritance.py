# class A:
# 	def __init__(self):
# 		print("init of A")
# 	def feature1(self):
# 		print("feature 1 is working...")
# 	def feature2(self):
# 		print("feature 2 is working...")
# class B(A):
# 	def __init__(self):
# 		super().__init__()
# 		print("init of B")
# 	def feature3(self):
# 		print("feature 3 is working...")
# 	def feature4(self):
# 		print("feature 4 is working...")
# class C(B):
# 	def __init__(self):
# 		self.feature1()
# 		print("init of C")
# 	def feature5(self):
# 		self.feature3()
# 		print("feature 5 is working...")
# 	def feature6(self):
# 		print("feature 6 is working...")
# x=C()
# x.feature5()


def many(**values):
	return values
a=many(a=5,b=9)
print( (a))