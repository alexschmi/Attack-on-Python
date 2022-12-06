from random import seed
from random import randint

def take_third(x):
    return x[2]

mytuple = (random.randint(1, 100), random.randint(1, 100), random.randint(1, 100))

list = []
for _ in range(10):
 mytuple = (random.randint(1, 100), random.randint(1, 100), random.randint(1, 100))
 list.append(mytuple)

sorted_list = sorted(list, key=take_third)
print(list)
print(sorted_list)
