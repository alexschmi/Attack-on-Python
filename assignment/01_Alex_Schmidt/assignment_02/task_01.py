word = input() # Stores the input string

def stringLength(word):
  counter = 0 # For counting the 
  for i in word: # The function goes through every character of the input word
    counter += 1 # and increments the counter by 1 each time
  return counter

print(stringLength(word))
