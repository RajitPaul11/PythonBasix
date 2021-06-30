num=int(input("Enter the number you want to check: "))
prime=True
for i in range(2,num):
  if(num%i==0):
    prime=False

if prime==True:
  print("This number is a Prime number")
else:
  print("This number is not a Prime Number")

