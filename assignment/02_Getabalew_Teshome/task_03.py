Bound_term = int(input("Please give the maximum number of terms to be sequenced: "))
# initializing the first two terms
F_0 = 0 
F_1 = 1 
count = 0

# an if else sequence can be used to verify the given number
if Bound_term <= 0:
   print("Please enter a positive integer")
# since a single term upper bound returns the first term of the Fibonnacci sequence
elif Bound_term == 1: 
   print("Fibonacci sequence upto",Bound_term,"is:")
   print(F_0)
else:
   print("Fibonacci sequence:")
   while count < Bound_term:
       print(F_0)
       F_n = F_0 + F_1
       # We then update the values until count >= Bound_term
       F_0 = F_1
       F_1 = F_n
       count += 1
