class Company:
	salary=500
	name="Google"
	def changeSalary(self,salary):
		self.__class__.salary=salary

C=Company()
C.changeSalary(300)
print(C.salary)
print(Company.salary)
