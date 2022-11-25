# Task 07 – Queue
queue = []
empty = False
while empty == False:
    person = input("Arriving person: ")
    if person == "next" or person == "Next":
        print(queue[0])
        queue.pop(0)
    else:
        queue.append(person)
    if queue == []:
        empty = True

