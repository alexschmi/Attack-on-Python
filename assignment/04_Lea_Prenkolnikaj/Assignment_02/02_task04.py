#Task 4: Sorted list of tuples

# Creating the random list of tuples:
import random
list = [(random.randint(0,100),random.randint(0,100),random.randint(0,100)) for i in range(10)]
print(list)

# Sorting the list

result = sorted(list)
result = tuple(result)
print('Sorted Tuple :', result)