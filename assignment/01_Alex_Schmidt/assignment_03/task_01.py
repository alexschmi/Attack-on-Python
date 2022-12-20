# initial list of customers
customers = ['alice','bob','cecile', 'john', 'tom']

# function to set the default balance to 0 for each customer
def set_default_balance(customers_list):
  default_balance = {c: 0 for c in customers_list}
  return default_balance

balance = set_default_balance(customers)

# testing
print(balance)

#-----

# add single
balance['david'] = 0
print(balance)

# remove single
balance.pop('david', "User did not exist")
print(balance)

# add multiple
new_users = ['david', 'ethan', 'fiona'] # add new customers
balance.update({c:0 for c in new_users}) # set default balance for each customer to 0
print(balance)

# remove multiple
[balance.pop(user,f'Warning: user {user} did not exist') for user in new_users] # remove multiple users including their balances
print(balance)

#-----

# function to deposit money for a specific user
def deposit_money(accounts, user, amount):
    if user not in accounts:  # prevents non-existing accounts
        print(f'error: user {user} not found')
    elif type(amount) != int and type(amount) != float: # prevents non-numeric input
        print('error: non-numeric input')
    elif amount < 0: # prevents adding negative money
        print('error: cannot add negative money')
    else:
        print('transaction successful!')
        accounts[user] += amount
    return accounts

# function to withdraw mony from a specific user
def withdraw_money(accounts, user, amount):
    if user not in accounts: # prevents non-existing accounts
        print(f'error: user {user} not found')
    elif type(amount) != int and type(amount) != float: # prevents non-numeric ipnut
        print('error: non-numeric input')
    elif amount > accounts[user]: # prevents overdrawing the account
        print('error: overdrawing not permitted!')
    else:
        print('transaction successful')
        accounts[user] -= amount
    return accounts
  
# testing
balance = deposit_money(balance, 'alice', 50)
balance = deposit_money(balance, 'cecile', -5)
balance = deposit_money(balance, 'anna', 5)

balance = withdraw_money(balance, 'alice', 15)
balance = withdraw_money(balance, 'bob', 15)
balance = withdraw_money(balance, 'felix', 15)

print(f'\n{balance}')


