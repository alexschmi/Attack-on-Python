# Task 4: Selective Printing
print('Give an upper bound: ')
upperbound = int(input())
for i in range(upperbound):
    if (i % 3) != 0: #will only be printed if i is divisible by 3 or is 0
        print(i)