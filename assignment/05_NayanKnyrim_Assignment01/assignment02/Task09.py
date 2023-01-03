def f(x):
  if x == 0:
    return 1
  else:
    a = x * f(x-1)
    return a

def e(x, i):
  y = 1
  for a in range(i):
    y = y + p(x, i)/f(i)
    i = i - 1
  return y

z = e(5,700)
print(z)

#fak = f(5)
#print(fak)
