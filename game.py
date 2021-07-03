import random

def game():
  randNo = random.randint(1,10)
  return randNo

if __name__ == '__main__':
  num=game()
  num=str(num)
with open('hiscore.txt','r') as f:
  t=f.read()
if int(t) < int(num):
  with open('hiscore.txt','w') as f:
    f.write(num)
  print("The new High Score is",num)
else:
  print("High Score Not Crossed")

