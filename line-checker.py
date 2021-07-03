content=True
i=0
with open("log-file.txt","r") as f:
    while content:
        content=f.readline()
        if 'python' in content.lower():
            print(content.strip())
            print('Python is present')
            print(i)
        i+=1
