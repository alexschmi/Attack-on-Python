def recursive_func(x, n):
    if n == 0:
        return 1
    if n >= 1:
        return x * recursive_func(x, n - 1)

print(recursive_func(2, 2))
print(recursive_func(3, 3))
