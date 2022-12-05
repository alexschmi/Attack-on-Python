word = input()

word = word.replace(" ", "") # Replaces whitespaces with empty strings -> no spaces

print(word)

wordSet = set(word) # Converts the word into set of characters

def countCharacterFrequency(word):
    frequency = {} # Dictionary to store the character occurence frequencies
    for i in wordSet:
       frequency[i] = word.count(i) # The count function counts the number of times each character appears in word
    return frequency

print(countCharacterFrequency(word))
