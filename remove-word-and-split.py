def remove_and_split(string,word):
    newStr= string.replace(word,"")
    return newStr.strip()

this="   Take a walk on the wild side  "
n=remove_and_split(this,"Take")
print(n)
