#Task 2: Largest List Element

# Creating a list with 10 random integers in a list of 0-100:
import random
random_list = [random.randint(0,100) for i in range(10)]
print(random_list)

# Get largest element of the list:
random_list.sort()
print("The largest element in the list is: ", random_list[-1])