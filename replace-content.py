words=["abuse","illegal","spam"]
with open("sample-text.txt") as f:
	content = f.read()

for word in words:
	content = content.replace(word,"$#####")

with open("sample-text.txt","w") as f:
	f.write(content)

