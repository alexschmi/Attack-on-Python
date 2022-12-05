#Task 05: Check Brackets

string = input("Enter a mathematical expression: ")


def bracket_checker(string):
    counter = 0
    for i in string:
        if i == '(':
            counter += 1
        elif i == ')':
            counter -= 1

    if counter == 0:
        return True
    else:
        return False


print(bracket_checker(string))