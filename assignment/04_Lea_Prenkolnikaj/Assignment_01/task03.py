#Task 3: Fibonacci Numbers
print("Upper bound: ")
ub = int(input())
x = 0
y = 1
print(0, end = " ")
while ub>1:
    print (y, end = " ")
    x, y = y, x + y
    ub -= 1