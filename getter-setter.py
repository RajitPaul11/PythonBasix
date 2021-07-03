class Employee:
	company: "Bharat Gas"
	salary = 4600
	salaryBonus = 400

	@property
	def totalSalary(self):
		return self.salary + self.salaryBonus
	
	@totalSalary.setter
	def totalSalary(self,val):
		self.salaryBonus = val - self.salary

E = Employee()
print(E.totalSalary)
E.totalSalary=6000
print(E.salary)
print(E.salaryBonus)
