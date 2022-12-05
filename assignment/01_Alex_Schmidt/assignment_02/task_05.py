expression = input()

def checkBrackets(expression): # The function checks if the amount of opening and closing brackets is equal
  counter = 0 # For storing the amount of brackets
  for i in expression:
    if i == '(':
      counter += 1 # For every opening bracket the counter goes up
    elif i == ')':
      counter -= 1 # For every closing bracket the counter goes down
  
  if counter == 0: # If the amount of opening and closing brackets is equal, the expression is correct
    return True
  else: 
    return False

print(checkBrackets(expression))
