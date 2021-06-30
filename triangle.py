n=int(input("Enter the level of triangle: "))
star=1
space=n-1
for i in range(1,n+1):
  print((" "*space),"*"*star)
  space-=1
  star+=2
