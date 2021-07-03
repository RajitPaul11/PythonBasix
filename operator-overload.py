class Test:
	def __init__(self,num):
		self.num=num
	def __add__(self,num2):
		print("Let's add")
		return self.num + num2.num
	def __mul__(self,num2):
		print("Let's Multiply")
		return self.num * num2.num
t1=Test(4)
t2=Test(5)
sum=t1+t2
print(sum)
mul=t1*t2
print(mul)
