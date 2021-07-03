class Employee:
	salary = 1000
	increment = 1.5
	@property
	def salaryAfterIncrement(self):
		return self.salary*self.increment
	@salaryAfterIncrement.setter
	def salaryAfterIncrement(self, val):
		self.increment = val/self.salary


E = Employee()
print(E.salaryAfterIncrement)
E.salaryAfterIncrement=2000
print(E.increment)

