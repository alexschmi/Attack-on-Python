#Task 2: Reversed Words
yourword1 = input("This program reverses a word of your choice. Enter a word: ")
rev = ''
for i in range(0, (len(yourword1))):
    rev = yourword1[i] + rev
print(yourword1 + ' reversed is: ' + rev)
# Using only String indices:
yourword2 = input('Reverse the following word using String-Indices: ')
print(yourword2 + ' reversed is: ' + yourword2[::-1])