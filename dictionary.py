spanish_dict = {

"amigo": "friend",
"casa": "house",
"gracias": "thankyou"
}

print("1. amigo, 2. casa, 3. gracias")
key = input("Enter the value you want to check?")
if int(key)==1:
  print(spanish_dict["amigo"])
elif int(key) == 2:
  print(spanish_dict["casa"])
elif int(key) == 3:
  print(spanish_dict["gracias"])
else:
  print("Enter a valid input")

