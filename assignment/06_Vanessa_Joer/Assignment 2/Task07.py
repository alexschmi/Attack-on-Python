queue = ['1','Clara', 'Thomas', 'Vanessa']

while True:
    nxt = raw_input('Next please: ')

    if nxt != "next":
        print('I did not quite catch that')
    else:
        queue.pop(0)
        print('In the queue: ', queue[0])
    if len(queue) == 0:
        print('There is no one waiting')
        break
