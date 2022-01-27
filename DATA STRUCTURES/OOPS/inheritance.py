# SINGLE LEVEL INHERITANCE

class A:
	def feature1(self):
		print("feature 1 is working...")
	def feature2(self):
		print("feature 2 is working...")
class B(A):
	def feature3(self):
		print("feature 3 is working...")
	def feature4(self):
		print("feature 4 is working...")


# MULTI LEVEL INHERITANCE


class A:
	def feature1(self):
		print("feature 1 is working...")
	def feature2(self):
		print("feature 2 is working...")
class B(A):
	def feature3(self):
		print("feature 3 is working...")
	def feature4(self):
		print("feature 4 is working...")
class C(B):
	def feature5(self):
		print("feature 5 is working...")
	def feature6(self):
		print("feature 6 is working...")


# MULTIPLE INHERITANCE

class A:
	def feature1(self):
		print("feature 1 is working...")
	def feature2(self):
		print("feature 2 is working...")
class B:
	def feature3(self):
		print("feature 3 is working...")
	def feature4(self):
		print("feature 4 is working...")
class C(A,B):
	def feature5(self):
		print("feature 5 is working...")
	def feature6(self):
		print("feature 6 is working...")

x=B()
x.feature3()






