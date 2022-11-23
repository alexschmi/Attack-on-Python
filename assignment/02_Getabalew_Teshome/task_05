# Task 05 - Triangle Checking 
def valid_triangle(x,y,z):  # here we create a function which checks the traingle inequality
    if x+y>=z and y+z>=y and z+y>=x:
        return True
    else:
        return False

# here we read the three sides from the user
print("Input lengths of the triangle sides: ")
x = float(input("x: ")) 
y = float(input("y: "))
z = float(input("z: "))

# since a triangle can't have a negative side and a zero side means either its a line(straight or angled)
if x <= 0 or y <= 0 or z <= 0 : 
  print('please enter positive number values')

#function is called up to make a decision and catagorize into Triangle group if accepted
elif (valid_triangle(x, y, z)) & (x == y == z):
  print('Triangle is Valid and is an equilateral')
elif (valid_triangle(x, y, z)) & (x==y or y==z or z==x):
  print('Triangle is Valid and is an isosceles Triangle')
elif (valid_triangle(x, y, z)) & (x != y != z):
	print("Triangle is Valid and is a Scalene triangle")
else:
    print('Triangle is Invalid.')
