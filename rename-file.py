import os
oldfile="file1.txt"
newfile="file2.txt"
with open(oldfile,"r") as f:
  content=f.read()

with open(newfile,"w") as f:
  f.write(content)

os.remove(oldfile)
