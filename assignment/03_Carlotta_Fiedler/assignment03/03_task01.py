# Task 01: Dictionary
# ======================================================================================================================

# ----------------------------------------------------------------------------------------------------------------------
# 1. Function that spans a dictionary holding a default balance of 0 for an initial list of customers, or adds the given
# customer (single/multiple) to an existing dictionary.
# ----------------------------------------------------------------------------------------------------------------------
def initialize_customer(customer, d={}, balance=0):
    if bool(d):
        dict = d
    else:
        dict = {}

    if type(customer) is list:
        for i in range(0,len(customer)):
            dict[customer[i]]=balance
    elif type(customer) is str:
        dict[customer]=balance
    else:
        return print("Error: invalid type of entered variable")
    return dict

# ----------------------------------------------------------------------------------------------------------------------
# 2. Function that removes single and multiple customers using the functionality of dict?
# ----------------------------------------------------------------------------------------------------------------------
def remove_customer(customer, dict):
    if type(customer) is list:
        for i in range(0, len(customer)):
            del dict[customer[i]]
    elif type(customer) is str:
        del dict[customer]
    else:
        return print("Error: invalid type of entered variable")
    return dict

# ----------------------------------------------------------------------------------------------------------------------
# 3. Now write two simple functions that allow you to deposit and withdraw money for a given bank customer.
# 4. Include error messages for inputs that are not permissible, e.g., withdrawing negative amounts or overdrawing the account, etc.
# ----------------------------------------------------------------------------------------------------------------------
def deposit(dict, customer, amount):
    if amount < 0:
        corr = input("Value to be deposit is a negative number. Please enter a valid amount or enter '+' " +
                       "if you want to deposit the positive value of the previously entered amount:")
        if corr == "+":
            amount = abs(amount)
        else:
            amount = corr
    dict[customer] = dict[customer] + amount
    print("Deposit was successful. " + customer + "'s updated bank status is: " + str(dict[customer]))
    return dict

def withdraw(dict, customer, amount):
    if amount < 0:
        corr = input("Value to be deposit is a negative number. Please enter a valid amount or enter '+' " +
                       "if you want to deposit the positive value of the previously entered amount:")
        if corr == "+":
            amount = abs(amount)
        else:
            amount = corr
    if (dict[customer] - amount) == 0:
        dict[customer] = dict[customer] - amount
        print("You account is now empty.")
    elif (dict[customer] - amount) < 0:
        print("!!! Warning: " + customer + " is overdrawing their account !!! \nThere is only " + str(dict[customer]) + " left in the account. \nPlease try again.")
    else:
        dict[customer] = dict[customer] - amount
        print("Withdraw was successful. " + customer + "'s updated bank status is: " + str(dict[customer]))
    return dict

# ----------------------------------------------------------------------------------------------------------------------
# main
# ----------------------------------------------------------------------------------------------------------------------
# Test 1:
test  = initialize_customer("Otto")
print(test)

# Test 2:
names = ["Carlo", "Lotta", "Carlotta"]
bank = initialize_customer(names)
print(bank)
initialize_customer("Carl", bank)
print(bank)
initialize_customer("Schlotta", bank, 100)
print(bank)

# Test 3:
remove_customer("Carlo", bank)
print(bank)
bank = remove_customer(["Lotta","Carl"], bank)
print(bank)
initialize_customer("Lotti", bank)
print(bank)

# Test 4:
print(bank)
deposit(bank, "Carlotta", 300)
withdraw(bank, "Carlotta", 234)
deposit(bank, "Lotti", 261)
withdraw(bank, "Schlotta", 101)
print(bank)
