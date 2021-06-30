dict = {}
print("Enter your favourite country")
a=input("Favourite Country of Aman: ")
b=input("Favourite Country of Vishal: ")
c=input("Favourite Country of Mukesh: ")
d=input("Favourite country of Pratham: ")
country={
    "Aman":a,
    "Vishal":b,
    "Mukesh":c,
    "Pratham":d,
    }
dict.update(country)
dict.update({"Samar":"ZBW"})
print(dict.items())

#Another Approach
#dict['Aman'] = a
#dict['Vishal'] = b
#dict['Mukesh'] = c
#dict['Pratham'] = d
