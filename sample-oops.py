class RailwayForm:
	formType= "RailwayForm"
	def printData(self):
		print(f"Name of the passenger is {self.name}")
		print(f"Name of the train is {self.train}")

newApplication = RailwayForm()
newApplication.name="Akash"
newApplication.train="Kathmandu Express"
newApplication.printData()

