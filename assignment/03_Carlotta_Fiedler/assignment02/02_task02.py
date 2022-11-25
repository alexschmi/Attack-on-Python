# Task 02 – Largest List Element
def my_largest_element(list):
    max = list[0]
    for i in range(0,len(list)):
        if (list[i] >= max):
            max = list[i]
    return max

# create list with 10 random integers
import random
list = [random.randint(0,100) for i in range(10)]
print(list)
print(my_largest_element(list))
