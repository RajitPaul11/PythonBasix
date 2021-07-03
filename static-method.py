class Employee:
	company="Google"
	signature="Best Wishes"
	def getSalary(self):
		print(f"Your Salary is {self.salary},{self.signature}")
	@staticmethod
	def greet():
		print("Good morning sir!")
samir=Employee()
samir.showGreetings()
samir.greet()
samir.salary=200000
samir.getSalary()

