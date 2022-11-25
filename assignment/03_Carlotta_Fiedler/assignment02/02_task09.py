# Task 09 – Unlimited Power II
import math

# Simple Solution using math.factorial()
def taylor_pow(x, e_to_x = 0):
    for i in range(15):
        e_to_x = e_to_x + x**i/math.factorial(i)
    return e_to_x

# Recursive Solution, independent of math.

def taylor_rec(x, n=10):
    global p, f
    p = 1
    f = 1
    if (n == 0):
        return 1
    r = taylor_rec(x, n - 1)
    p = p * x
    f = f * n
    return (r + p / f)

# Test
print("Calculation of e to the power of x:")
x = int(input("x: "))
print("Using math.exp(): " + str(math.exp(x)))
print("Using math.factorial(): " + str(taylor_pow(x)))
print("Using recursive function independent of math.: " + str(taylor_rec(x)))
