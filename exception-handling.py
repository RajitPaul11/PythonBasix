with open("1.txt","r") as f:
	r=f.read()
	print(r)

try:
	with open("3.txt","r") as f:
		r=f.read()
		print(r)
except Exception as e:
	print("File does not exist")

with open("2.txt","r") as f:
        r=f.read()
        print(r)
