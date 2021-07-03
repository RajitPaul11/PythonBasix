import math
class Calculator:
	def square(self,num):
		print(f"The square of {num} is {num*num}")
	def cube(self,num):
		print(f"The cube of {num} is {num*num*num}")
	def squareroot(self,num):
		print(f"The square root of {num} is {math.sqrt(num)}")
	@staticmethod
	def greet():
		print("Welcome")
mathProblem=Calculator()
mathProblem.greet()
mathProblem.square(2)
mathProblem.cube(3)
mathProblem.squareroot(4)

