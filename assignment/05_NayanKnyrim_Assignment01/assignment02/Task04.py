import random
import numpy as np

l = []
for x in range(10):
  n = np.random.randint(1, 100, size=3)
  t = tuple(n)
  l.append(t)
 # print(t)
print(l)
l.sort(key=lambda x: x[2])
print(l)
