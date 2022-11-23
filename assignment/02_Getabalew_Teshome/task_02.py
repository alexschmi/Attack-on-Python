# Task 02 – Reversed Words

s = input('Please give any word:') #input function to get input from the user
def reversed_string(s): # this function then takes the input s 
  mystring = '' # this will just return nothing initially
  index = len(s) - 1 # this computes the last character in the input string
  while index >= 0: # this iterates index from its initial value(3) down to 0.
      mystring += s[index] # mystring will then have the index string values according to the iteration
      index -= 1   # which is decreasing till it reaches 0.
  return mystring   
reversed_string(s) # This then will output a reversed string of the input in the end 
