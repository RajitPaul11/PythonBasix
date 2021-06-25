letter='''Dear <|NAME|>,
You are  selected!

Date: <|DATE|>'''

name=input("Enter your name ")
date=input("Enter your date ")
letter=letter.replace("<|NAME|>", name)
letter=letter.replace("<|DATE|>", date)

letter=letter.replace("  "," ")
print(letter)
