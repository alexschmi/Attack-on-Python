x = int(input("input: "))
s = ""
i = 0
y = 0
a = 1
while i < x/2 :
   s = s + str(y) + ", " + str(a) + ", "
   y = y + a
   a = a + y
   i = i + 1

print(s)
