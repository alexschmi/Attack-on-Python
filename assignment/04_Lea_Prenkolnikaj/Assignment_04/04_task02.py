Task 02: List comprehensions

def remove_long_words(s, n):
    # Split the sentence into words and store them in a list
    words = s.split()

    # Use list comprehension to create a new list with only the words that are shorter than the given length
    short_words = [word for word in words if len(word) <= n]

    # Print the list of short words
    print(short_words)


# Test the function with a sentence and an integer value
remove_long_words("The quick brown fox jumps over the lazy dog", 3)
