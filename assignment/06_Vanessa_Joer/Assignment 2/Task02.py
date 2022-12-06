from random import seed
from random import randint

seed(1)
list = []
for _ in range(10):
 zahl = randint(0, 100)
 list.append(zahl)
 print(list)

max = 0
for _ in list:
    if max < _:
         max =_

print(max)
