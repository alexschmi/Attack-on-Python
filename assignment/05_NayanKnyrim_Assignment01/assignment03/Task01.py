customers = ['alice', 'bob', 'cecile']

balance = {x: 0 for x in customers}

def add_customer():
    n = input("How many new customers?(number) ")
    i = 0
    newcus = []
    while i < int(n):
        newcus.append(input("new customer " + str(i + 1) + " name: "))
        i = i + 1
    balance.update({x: 0 for x in newcus})
    print("updated:", balance)
    terminal()

def deposit(b, customer, amount):
    if amount < 0:
        print("cannot deposit negative amount")
    else:
        b[customer] = b[customer] + amount
        print(">>success<<")
    terminal()

def withdraw(b, c, a):
    if a < 0:
        print("cannot withdraw negative amount")
    elif (b[c] - a) < 0:
        print(">>insufficient balance<<")
    else:
        b[c] = b[c] - a
        print(">>success<<")
    terminal()

def terminal():
    print("\nWhat would you like to do?\n for deposit type d \n for withdraw type w \n for add new customer type a\n to view balance type b ")
    x = input()
    if x == 'd':
        c = input("customer: ")
        a = int(input("amount: "))
        deposit(balance, c, a)
    elif x == 'w':
        c = input("customer: ")
        a = int(input("amount: "))
        withdraw(balance, c, a)
    elif x == 'a':
        add_customer()
    elif x == 'b':
        print("balances: ", balance)
        terminal()
    else:
        print("Error try again")
        terminal()

terminal()
