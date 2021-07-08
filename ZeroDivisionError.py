a=int(input("Enter 1st number: "))
b=int(input("Enter 2nd number: "))

try:
	num=a/b
except ZeroDivisionError as z:
	print("Cannot divide by zero")
	print(z)

print(num)
