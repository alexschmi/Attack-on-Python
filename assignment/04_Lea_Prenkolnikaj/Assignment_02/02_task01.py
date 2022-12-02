#Task 1: String Length

def find_length(str):
    counter = 0
    while str[counter:]:
        counter += 1
    return counter


str = input("Enter a word. I will tell you its length. ")
print(find_length(str))