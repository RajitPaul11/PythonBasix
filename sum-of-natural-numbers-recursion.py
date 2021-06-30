def addnumber(num):
    if num!=0:
        return num+addnumber(num-1)
    else:
        return num
num=int(input("Enter the number: "))
sum=addnumber(num)
print(f"The sum is {sum}")

