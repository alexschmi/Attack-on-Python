# Task 03 – Character Frequency
def letter_count(s):
    dict = {}
    for letter in s:
        if letter not in dict:
            key, value = letter, s.count(letter)
            dict[key]=value
    return dict

s = input('Commit a String:')
s = s.replace(" ", "") # removes whitespaces
print(letter_count(s))
