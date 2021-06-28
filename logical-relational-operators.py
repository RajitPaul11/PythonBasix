a=input("Enter a number: ")
b=input("Enter a number to compare to: ")
if a!=b and a>=b:
    print(a," equals to or greater than ", b)
elif a!=b and a<=b:
    print(a," not equal to and less than ",b)
else:
    print(a," equals to ", b)

