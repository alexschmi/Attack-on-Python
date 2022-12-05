import random

# Generates the a list of 10 tuples with each tuple consisting of 3 random integers between 1 and 100
randomList = [(random.randint(1, 100), random.randint(1, 100), random.randint(1, 100)),
              (random.randint(1, 100), random.randint(1, 100), random.randint(1, 100)),
              (random.randint(1, 100), random.randint(1, 100), random.randint(1, 100)),
              (random.randint(1, 100), random.randint(1, 100), random.randint(1, 100)),
              (random.randint(1, 100), random.randint(1, 100), random.randint(1, 100)),
              (random.randint(1, 100), random.randint(1, 100), random.randint(1, 100)),
              (random.randint(1, 100), random.randint(1, 100), random.randint(1, 100)),
              (random.randint(1, 100), random.randint(1, 100), random.randint(1, 100)),
              (random.randint(1, 100), random.randint(1, 100), random.randint(1, 100)),
              (random.randint(1, 100), random.randint(1, 100), random.randint(1, 100))]
          
print("unsorted list: \t" + str(randomList))

def sorter(randomList): # Returns the third element of each tuple
  return randomList[2]

sortedList = sorted(randomList, key = sorter) # Sorts the list by the third element

print("sorted list : \t" + str(sortedList))
