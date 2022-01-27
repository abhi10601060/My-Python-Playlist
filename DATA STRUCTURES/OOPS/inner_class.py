class Student:
	school="pvg"
	def __init__(self,name,rno):
		self.name=name
		self.rollno=rno
		self.laptop=self.Laptop()
	def show(self):
		print(self.name , self.rollno)

	class Laptop:
		def __init__(self):
			self.model="hp"
			self.ram=2

		def show(self):
			print(self.model, self.ram)

a=Student("abhi",9108)
print(a.laptop.model)


# class Human:
# 	population=0
# 	def __init__(self):
# 		print("Human is craeted...")
# 		self.population+=1


# a=Human()
# b=Human()
# print(b.population)

