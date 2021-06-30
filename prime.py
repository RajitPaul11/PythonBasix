num=int(input("Enter a number to check it is prime or not: "))
count=0
for i in range(1,11):
    if(num%i==0):
        count+=1

if num > 10:
    if count<2:
        print("Prime Number")
    else:
        print("Not a Prime Number")
elif num>1 and num <= 10:
    if count==2:
        print("Prime Number")
    else:
        print("Not a Prime Number")
else:
    print("1 is a composite number")

        
