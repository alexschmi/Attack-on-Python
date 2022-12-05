import random

# Generates a list of 10 random integers between 1 and 100
randomList = [random.randint(1, 100), random.randint(1, 100), random.randint(1, 100), random.randint(1, 100), random.randint(1, 100), random.randint(1, 100), random.randint(1, 100), random.randint(1, 100), random.randint(1, 100), random.randint(1, 100)]

print(randomList)

def findLargestElement(randomList):
  element = 0 # In the first iteration the first list element is compared to zero
  for i in range(len(randomList)): 
    if randomList[i] > element: # Checks if the current list element is greater than the previous one
      element = randomList[i]   # If True, the list element is asigned to element
  return element  # In the end, element contains the largest list element

print("The largest element is " + str(findLargestElement(randomList)))
