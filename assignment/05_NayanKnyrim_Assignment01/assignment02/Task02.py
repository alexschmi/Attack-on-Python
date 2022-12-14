import random
x = []
for i in range(0, 10):
  n = random.randint(0, 100)
  x.append(n)
print(x)
x.sort()
print(x)
print(x[-1])
