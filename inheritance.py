class Employee:
	company="Google"
	def empFunction(self):
		print("Welcome to Google")
class Programmer(Employee):
	def showInfo(self):
		print(f"Name: {self.name}\nJobRole: {self.role}")

class Tester(Employee):
	def showInfor(self):
		print(f"Name: {self.name}\nJobRole: {self.role}")

p=Programmer()
t=Tester()
p.name="Raj"
p.role="JDev"
p.showInfo()
t.name="Ritam"
t.role="JTest"
t.showInfor()

