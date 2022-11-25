# Task 06 – Check Brackets II
def only_brackets(term):
    only = ""
    l = {'}','{', ')','(', ']', '['}
    for i in range(len(term)):
        if term[i:i+1] in l:
            only = only + term[i:i+1]
        else:
            continue
    print("Brackets without other operators: " + only)
    return only

# Checks balance of different types of brackets
def balanced_brackets(s):
    stack = []
    dict = {'}': '{', ')': '(', ']': '['}
    for i in s:
        if i in '}])':
            if not stack or stack[-1] != dict[i]:
                return False
            stack.pop()
        else:
            stack.append(i)
    return not stack

term = input("Check composition of brackets in the following mathematical expression:\n")
term = only_brackets(term)
if (balanced_brackets(term)):
    print("Composition of brackets is CORRECT")
else:
    print("Composition of brackets is INCORRECT")
