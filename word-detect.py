with open("log-file.txt","r") as f:
	content=f.read()

if 'python' in content.lower():
	print('Yes Python is present')
else:
	print('Python is not present')

