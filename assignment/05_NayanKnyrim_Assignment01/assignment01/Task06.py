x = int(input("input "))
s = ""
r = x
while r > 0:
  r = x%8
  s = str(s) + str(r)
  #print(r)
  x = int((x - r)/8)
print(s[::-1])
