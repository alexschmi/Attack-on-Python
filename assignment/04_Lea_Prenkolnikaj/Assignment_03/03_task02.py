#Task 02: Classes


class costumer:
    def __init__(self, name, balance = 0):
        self.name = name
        self.balance = balance
    def deposit(self, amount):
        if amount < 0:
            print("Error. Something did not work.")
        else:
            self.balance += amount
            print("Your new balance is %d" % self.balance)
    def withdraw(self, amount):
        if amount > self.balance:
            print("Error. You cannot overdraw your account.")
        else:
            self.balance -= amount
            print("Your new balance is: %d" % self.balance)