a=input("Enter a number: ")
try:
	b = 1/int(a)
	print(b)
except ValueError as e:
	print("Please enter a valid number")
except ZeroDivisionError as e:
	print("We cannot divide a number by zero, please enter something greater than zero!")

print("Thanks for using this code")




