#Task 5: Triangle Checking
print("How long is side a? Please give a number: ")
a=int(input())
print("How long is side b? Please give a number: ")
b=int(input())
print("How long is side c? Please give a number: ")
c=int(input())

#Triangle type distinction
if c >= a+b:
    print("Please check for triangle inequality and give a valid input!")
elif a==b==c:
    print("equilateral")
elif a==b or a==c or c==b:
    print("isosceles")
else:
    print("scalene")
