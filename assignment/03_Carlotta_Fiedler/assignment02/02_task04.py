# Task 04 – Sorted List of Tuples
import random
list = [(random.randint(0,100),random.randint(0,100),random.randint(0,100)) for i in range(10)]
print("Random list of tuples:")
print(list)

# bubble sort for list of tuples
hi = len(list)-1
while (hi >= 0):
    for i in range(len(list)):
        if (i<hi and list[i][2] > list[i+1][2]):
            # vertausche list[i] und list[i+1]
            tmp = list[i]
            list[i] = list[i+1]
            list[i+1] = tmp
    hi = hi-1

print("Sorted list of random tuples:")
print(list)
