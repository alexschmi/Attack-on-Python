x = int(input("input: "))
i = 0
s = 0
while i < x:

    i = i + 1
    if i % 3 == 0:
        continue
    s = str(s) + ", " + str(i)
print(s)
