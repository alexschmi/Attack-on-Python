def p(x, n):
  if n == 0:
    return 1
  if n == 1:
    return x
  else:
    return x * p(x, n-1)

x = input("Base: ")
n = input("Power: ")
print(p(int(x), int(n)))
