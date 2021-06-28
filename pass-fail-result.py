n1=int(input("Enter the marks for Maths: "))
n2=int(input("Enter the marks for Physics: "))
n3=int(input("Enter the marks for Chemistry: "))
tot_marks=n1+n2+n3
if tot_marks>120 and n1 >= 33 and n2>= 33 and n3>= 33:
    print("Pass")
else:
    print("Fail")
