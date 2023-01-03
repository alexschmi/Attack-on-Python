class Customer:
  
  # constructor
  def __init__(self, name, balance=0):
    self.name = name
    self.balance = balance

  # function to deposit money on a account
  def deposit_money(self, value):
    if type(value) != int and type(value) != float: # prevents non-numeric input
      print('error: non-numeric input!')
    elif value < 0: # prevents adding negative money
      print('error: cannot add negative money!')
    else:
      self.balance += value
      print('transaction successful!\nnew balance: ' + str(self.balance))

  # function to withdraw money from a account
  def withdraw_money(self, value):
    if type(value) != int and type(value) != float: # prevents non-numeric input
      print('error: non-numeric input!')
    elif value < 0: # prevents withdrawing negative money
      print('error: cannot withdraw negative money!')
    elif value > self.balance:
      print('error: overdrawing the account!') # prevents overdrawing the account
    else:
      self.balance -= value
      print('transaction successful!\nnew balance: ' + str(self.balance))

# testing
c = Customer('john', 50)
c.deposit_money(5)
c.withdraw_money(10)

#-----

class SavingsCustomer(Customer):

  # constructor
  def __init__(self, name, balance=0, savings=0):
    super().__init__(name, balance) # inherit constructor from Customer class
    self.savings = savings # add savings attribute to constructor

  # function to transfer money from balance to savings
  def transfer_to_savings(self, value):
    if type(value) != int and type(value) != float: # prevents non-numeric input
      print('error: non-numeric input!')
    elif value < 0: # prevents withdrawing negative money
      print('error: cannot withdraw negative money!')
    elif value > self.balance:
      print('error: overdrawing the account!') # prevents overdrawing the account
    else:
      self.balance -= value # withdraw value from balance
      self.savings += value # add value to savings
      print('transaction successful!\nnew balance: ' + str(self.balance) + '\nnew savings: ' + str(self.savings))

  # function to transfer money from savings to balance
  def transfer_to_balance(self, value):
    if type(value) != int and type(value) != float: # prevents non-numeric input
      print('error: non-numeric input!')
    elif value < 0: # prevents withdrawing negative money
      print('error: cannot withdraw negative money!')
    elif value > self.balance:
      print('error: overdrawing the account!') # prevents overdrawing the account
    else:
      self.balance += value # add value to balance
      self.savings -= value # withdraw value from savings
      print('transaction successful!\nnew balance: ' + str(self.balance) + '\nnew savings: ' + str(self.savings))

# testing
d = SavingsCustomer('michael', 100)
d.transfer_to_savings(50)
d.transfer_to_balance(20)
