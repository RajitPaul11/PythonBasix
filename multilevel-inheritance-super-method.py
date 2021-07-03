#Example of MultiLevel Inheritance and Super Class
class FirstClass:
	def sampleMethod(self):
		print("Hello from FirstClass")
	def superMethod(self):
		print("Super Method called")
class SecondClass(FirstClass):
	def sampleMethod(self):
		print("Hello from SecondClass")
class ThirdClass(SecondClass):
	def sampleMethod(self):
		super().superMethod() 	#This will call the method of BaseClass
		print("Hello from ThirdClass")

first=FirstClass()
second=SecondClass()
third=ThirdClass()

first.sampleMethod()
second.sampleMethod()
third.sampleMethod()
