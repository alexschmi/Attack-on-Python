class Costumer:
    def __init__(self, name, balance = 0):
        self.name = name
        self.balance = balance


    def deposit(self, amount):
        if amount < 0:
            print('ERROR: You Can Not Withdraw A Negative Amount Of Money')
        else:
            self.balance += amount
            print('Your New Balance Is: %d' % self.balance)

    def withdraw(self, amount):
        if amount > self.balance:
            print('ERROR: You Can Not Overdraw Your Account')
        else:
            self.balance -= amount
            print('Your New Balance Is: %d' % self.balance)



#--TEST--#
c = Costumer('Vanessa')
c.deposit(-10)
c.deposit(100)
c.withdraw(200)
c.withdraw(50)

class SavingsCostumer(Costumer):
    def __init__(self, name, balance = 100, savings = 0):
        self.name = name
        self.balance = balance - savings
        self.savings= savings

    def transfer(self, amount):
        if amount > self.balance:
            print('ERROR: There Is Not Enough Money In The Account')
        else:
            self.balance -= amount
            self.savings += amount
            print('Transfer Successfull!' + '\nYour New Balance Is: %d' % self.balance + '\nYour New Balance On Your Savings Account Is: %d' % self.savings)

    def take(self, amount):
        if amount > self.savings:
            print('ERROR: There Is Not Enough Money In The Savings Account')
        else:
            self.balance += amount
            self.savings -= amount
            print('Transfer Successfull!' + '\nYour New Balance Is: %d' % self.balance + '\nYour New Balance On Your Savings Account Is: %d' % self.savings)

#--TEST--#
s = SavingsCostumer('Sarah')

s.transfer(1000)
s.transfer (10)
s.take(50)
s.take(5)
