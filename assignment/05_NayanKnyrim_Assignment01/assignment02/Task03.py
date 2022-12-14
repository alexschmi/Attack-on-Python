x = input("Input: ")
wb = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
e = {}
x = x.replace(" ", "")
print(x)
#print("a:", x.count('a'))

i = 0
while i < len(wb):
  if wb[i] in x:
    e[wb[i]] = x.count(wb[i])
    # print(wb[i], x.count(wb[i]))
  i = i + 1

print(e.items())
