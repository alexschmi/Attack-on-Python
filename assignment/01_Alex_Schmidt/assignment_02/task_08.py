print("Input x value")
x = int(input())
print("Input n value")
n = int(input())

def power(x, n):
    if n == 0:
        return 1 # A number to the power of 0 always equals 1

    if n >= 1:
        return x * power(x, n - 1) # Multiplies the given x value to itself until the power n is zero

print("Result: " + str(power(x, n)))
