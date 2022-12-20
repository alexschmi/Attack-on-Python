#1.
def build_database(c):  # function to display the Accounts
    balance = {c: 0 for c in costumers}
    return balance


#---TEST---#
costumers = ['Clara', 'Sarah', 'Vanessa']
accounts = build_database(costumers)
print(build_database(costumers))

accounts['Clara'] = 10
print(accounts)


#2.
#adding a single new costumer:

accounts.setdefault('Thomas', 0 )
print(accounts)


#deleting a costumer:

accounts.pop('Sarah')
print(accounts)


#adding multiple costumers:
new_costumers = ['Lea', 'Florian']
accounts.update({c:0 for c in new_costumers})
print(accounts)

#3. Creating two simple functions to deposit and withdraw money:

def deposit(accounts, costumer, amount):
    if amount < 0:
        print('ERROR: You Can Not Deposit A Negative Amount of Money')
    else:
        accounts[costumer] += amount
        print('Your New Balance Is: ' + str(accounts[costumer]))

def withdraw(accounts, costumer, amount):
    if amount > accounts[costumer]:
        print('ERROR: You Can Not Overdraw Your Account ')
    else:
        accounts[costumer] -= amount
        print('Your New Balance Is: ' + str(accounts[costumer]))
        
#---TEST---#
print(deposit(accounts, 'Vanessa', 100))
print(deposit(accounts, 'Vanessa', -10))
print(withdraw(accounts, 'Vanessa', 200))
print(withdraw(accounts, 'Vanessa', 50))

print(accounts)
