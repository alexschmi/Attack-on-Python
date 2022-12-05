print("Enter names seperated by space")
queue = input()

queue = queue.split(" ") # Splits the strings into words and creates a list

print("\n")
print("Queue: " + str(queue))

while len(queue) > 0: # Run the loop as long as the queue is not empty
  person = input()
  if person == "next": 
    print("It is your turn " + queue[0]) 
    queue.pop(0) # Removes the last element of the list
    print("Queue: " + str(queue))
  else:
    queue.append(person) # Appends the typed name to the end of the list/queue
    print("Queue: " + str(queue))
