# Task 03 - Fibonacci Numbers
print('Upper bound for Fibonacci Order: ')
upper_bound = int(input())
if upper_bound == 0:
    print([0])
elif upper_bound == 1:
    print([0, 1])
else:
    fib = [0] * upper_bound
    fib[0] = 0
    fib[1] = 1
    i = 2
    while i < upper_bound:
        fib[i] = fib[i - 1] + fib[i - 2]
        i = i + 1
    print(fib)
