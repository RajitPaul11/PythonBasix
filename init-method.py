class Employee:
	company="Google"
	
	def __init__(self,name,salary,unit):
		print("Employee is created!")
		self.name=name
		self.salary=salary
		self.unit=unit

	def getDetails(self):
		print(f"The name of the employee is {self.name} with salary {self.salary} and unit as {self.unit}")
Neo=Employee("Neo",200000,"TestEngineer")
Neo.getDetails()
