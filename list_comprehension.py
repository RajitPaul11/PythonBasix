#Create list from existing list in an elegant way

list1 = [1,7,8,3,5,7,89,34]
#b = []
#for item in list1:
#	if item%2==0:
#		b.append(item)
#print(b)

#Shortcut to write the same:
b = [i for i in list1 if i%2==0]
print(b)



t = [1,3,4,5,6,6,7,7]
s ={i for i in t}
print(s)
