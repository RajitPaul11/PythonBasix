num1=input("Enter 1st no: ")
num2=input("Enter 2nd no: ")
num3=input("Enter 3rd no: ")

def maximum(num1,num2,num3):
  if (num1>num2 and num1>num3):
     print(f"{num1} is the greatest number")
  elif (num2>num1 and num2>num3):
     print(f"{num2} is the greatest number")
  elif (num3>num1 and num3>num2):
     print(f"{num3} is the greatest number")
  else:
     print("Please don't enter matching numbers")

maximum(num1,num2,num3)

