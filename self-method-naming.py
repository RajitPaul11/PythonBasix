class ABC:
	def check(var): #We can change the self keyword to a name of our choice
		print(f"Hello {var.name}")
User1=ABC()
User1.name="RAM"
User1.check()
