# Task 08 – Unlimited Power
def unlimited_pow(x,n):
    if n == 1:
        return x
    else:
        return x*(unlimited_pow(x,n-1))

# Test
print("Calculation of x to the power of n:")
x = int(input("x: "))
n = int(input("n: "))
print(unlimited_pow(x,n))
if unlimited_pow(x,n) == x**n:
    print("Correct")
