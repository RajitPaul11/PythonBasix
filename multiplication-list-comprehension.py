num=int(input("Enter a number of your choice: "))
mylist=[num*i for i in range(1,11)]
print(mylist)
with open("tables.txt","a") as f:
	f.write(str(mylist))
	f.write('\n')
