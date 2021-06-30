#Snake-Water-Gun-Problem
import random

def game(comp,you):
  if comp=='s' and you=='g':
    print("You Win!")
  elif comp=='w' and you=='s':
    print("You Win!")
  elif comp=='g' and you=='w':
    print("You Win!")
  elif comp=='s'and you=='w':
    print("Comp Win")
  elif comp=='w'and you=='g':
    print("Comp Win")
  elif comp=='g'and you=='s':
    print("Comp Win")
  else:
    print("Game draw")

print("Computer's Turn: Snake(1), Water(2), Gun(3)?")
randNo=random.randint(1,3)
if randNo == 1:
  comp='s'
elif randNo == 2:
  comp='w'
elif randNo == 3:
  comp='g'

you=input("Your Turn: Snake(s), Water(w), Gun(g)?")

game(comp,you)
print(f'Comp chose {comp}, you chose {you}')
