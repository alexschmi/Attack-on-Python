#Task 3: Character Frequency

your_word = input("Enter your word here: ")

your_word = your_word.replace(" ", "")

print(your_word)

wordtoset = set(your_word)

def cf(your_word):
    frequency = {}
    for i in wordtoset:
       frequency[i] = your_word.count(i)
    return frequency

print(cf(your_word))