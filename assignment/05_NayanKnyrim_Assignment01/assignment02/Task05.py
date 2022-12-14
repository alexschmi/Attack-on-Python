s = "(4+4))("
t = "(5+6))"
c = 0
c2 = 0
i = 0
while i < len(s):
  if "(" in s:
    c = s.count("(")
  if ")" in s:
    c2 = s.count(")")
  i = i + 1
print(c, c2)
if (c-c2 != 0):
  print("incorrect")
else:
  print("ok")
