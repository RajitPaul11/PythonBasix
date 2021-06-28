text=input("Enter the text: ")
if "click this" in text:
    spam = True
elif "lucky winner" in text:
    spam = True
elif "super offer" in text:
    spam = True
else:
    spam = False

if spam == True:
    print("This text is spam")
else:
    print("This text is not spam")


