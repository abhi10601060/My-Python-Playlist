class Car:
	wheel=4
	name="audi"
	def __init__(self):
		self.model="Q5"
		self.engine="diesel"
		self.wheel=6
	def wheels(self):
		print(self.wheel)
	@classmethod
	def info(cls):
		print(cls.wheel)
	@staticmethod
	def class_info():
		print("this is Car class...")

c1=Car()
c1.wheel=5
c2=Car()
print(c1.wheel, c2.wheel)
c1.info()
c2.class_info()
c1.wheels()
c3=Car()
print(c3)