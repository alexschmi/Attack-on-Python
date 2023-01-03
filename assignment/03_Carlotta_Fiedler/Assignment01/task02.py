# Task 02 - Reversed Words
# Using a Loop-Structure:
word1 = input('Reverse the following word with a Loop-Programm: ')
rev = ''
for i in range(0, (len(word1))):
    rev = word1[i] + rev
print(word1 + ' reversed is: ' + rev)
# Using only String indices:
word2 = input('Reverse the following word using String-Indices: ')
print(word2 + ' reversed is: ' + word2[::-1])
