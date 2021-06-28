spanish_dict = {
        "hola": "hello",
        "padre": "father",
        "madre": "mother"
        }

print("Options are:",spanish_dict.keys())
key=input("Enter the key you want value for: ")
#print(spanish_dict[key]) #This will throw error if the word is not present

#Below line would not throw error if key is not present
print(spanish_dict.get(key))

