class Programmer:
	def __init__(self,name,branch,company):
		self.name=name
		self.branch=branch
		self.company=company
	def getDetails(self):
		print(f"The programmer name is {self.name}")
		print(f"The programmer branch is {self.branch}")
		print(f"The programmer company is {self.company}")
Neo=Programmer("Neo","Florida","Microsoft")
Neo.getDetails()
Jupiter=Programmer("Jupiter","California","Expedia")
Jupiter.getDetails()
