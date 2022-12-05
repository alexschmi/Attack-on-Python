import math

print("Input x value")
x = int(input())
print("Input accuracy factor between 1-100")
a = int(input())

def power(x, n): # See task 08
    if n == 0:
        return 1 

    if n >= 1:
        return x * power(x, n - 1) 

def eToPowerOfX(x, a): # Calculates e to the power of x with the Taylor Series
  sum = 0 # To store the sums
  for i in range(a):
    sum += power(x, i) / math.factorial(i) # Taylor Series
  return sum
    
print(eToPowerOfX(x, a))
