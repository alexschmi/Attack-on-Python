# Task 04 - Selective Printing
print('Upper bound: ')
upper_bound = int(input())
for i in range(upper_bound):
    if (i % 3) != 0:
        print(i)
