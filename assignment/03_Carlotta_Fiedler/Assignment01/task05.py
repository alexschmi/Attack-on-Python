# Task 05 - Triangle Checking
# Identification of the Type
def triangle_type(a, b, c):
    if a == b and a == c:
        return 'equilateral'
    elif a == b or a == c or c == b:
        return 'isosceles'
    else:
        return 'scalene'


# Test for Triangle Inequality
def triangle_inequality(a, b, c):
    if (c < a + b) or (a < c + b) or (b < a + c):
        return True
    else:
        return False


# Prompt
print('Lengths of triangle sides:')
a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))
print('The given Triangle is ' + triangle_type(a, b, c))
if triangle_inequality(a, b, c):
    print('The Triangle Inequality Rule applies.')
else:
    print('The Triangle Inequality Rule does not apply with the given values.')
