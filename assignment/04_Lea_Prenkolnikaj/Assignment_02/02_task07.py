#Task 07: Queue

queue = []
empty = False
while empty == False:
    arriving_person = input("The arriving person is: ")
    if arriving_person == "next" or arriving_person == "Next":
        print(queue[0])
        queue.pop(0)
    else:
        queue.append(arriving_person)
    if queue == []:
        empty = True