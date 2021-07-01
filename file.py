#Using open method to read a file
f=open('sample-text.txt','r')
#data=f.read()
data=f.read(5) #Read first 5 characters from a file
print(data)
f.close()
