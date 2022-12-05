#Task 08: Unlimited Power

x = int(input("Input your x value (integer): "))
n = int(input("Input your n value (integer): "))

def unlimited_power(x, n):
    if n == 0:
        return 1

    if n >= 1:
        return x * unlimited_power(x, n-1)

print("The result is: " + str(unlimited_power(x, n)))