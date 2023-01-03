# Task 02: Classes
# ======================================================================================================================
# ----------------------------------------------------------------------------------------------------------------------
# 1. Write a simple class with appropriate constructor *\_\_init\_\_* that initializes an object of class *Customer*
# tracking the same information as in Task 01.
# ----------------------------------------------------------------------------------------------------------------------

class Customer(object):
    def __init__(self, name, balance = 0):
        self.name = name
        self.balance = balance

# ----------------------------------------------------------------------------------------------------------------------
# 2. Now write two simple methods for class *Customer* that allow you to deposit and withdraw money for a given customer object.
# 3. Include error messages for inputs that are not permissible, e.g., withdrawing negative amounts or overdrawing the account.
# ----------------------------------------------------------------------------------------------------------------------
    def perform_deposit(self, amount):
        if amount < 0:
            corr = input("Value to be deposited is a negative number. Please enter a valid amount or enter '+' " +
                         "if you want to deposit the positive value of the previously entered amount:")
            if corr == "+":
                amount = abs(amount)
            else:
                amount = corr
        self.balance = self.balance + amount
        print("Deposit was successful. " + self.name + "'s updated bank status is: " + str(self.balance))


    def perform_withdraw(self, amount):
        if amount < 0:
            corr = input("Value to be deposited is a negative number. Please enter a valid amount or enter '+' " +
                         "if you want to deposit the positive value of the previously entered amount:")
            if corr == "+":
                amount = abs(amount)
            else:
                amount = corr
        if (self.balance - amount) == 0:
            self.balance = self.balance - amount
            print("You account is now empty.")
        elif (self.balance - amount) < 0:
            print("!!! Warning: " + self.name + " is overdrawing their account !!! \nThere is only " +
                  str(self.balance) + " left in the account. \nPlease try again.")
        else:
            self.balance = self.balance - amount
            print("Withdraw was successful. " + self.name + "'s updated bank status is: " + str(self.balance))

# ----------------------------------------------------------------------------------------------------------------------
# 4. (Inheritance) Write a child class *SavingsCustomer* that inherits its features from the parent class *Customer*.
# A savings customer has an extra savings balance for receiving extra interest. The class should have a method to transfer
# money back and forth between the accounts' main balance as well as the savings balance. Do not forget to add reasonable error messages.
# ----------------------------------------------------------------------------------------------------------------------
class SavingsCustomer(Customer):

    def __init__(self, name, savings= 0, balance = 0):
        Customer.__init__(self, name, balance)
        self.savings = savings
        self.balance = balance - savings

    def transfer_savings(self, amount, saving=True):
        if amount < 0:
            corr = input("Value to be deposited is a negative number. Please enter a valid amount or enter '+' " +
                         "if you want to deposit the positive value of the previously entered amount:")
            if corr == "+":
                amount = abs(amount)
            else:
                amount = corr

        if saving:
            if amount > self.balance:
                print("!!! Warning: " + self.name + " is overdrawing their account !!! \nThere is only " +
                      str(self.balance) + " left in the account to transfer to savings. \nPlease try again.")
            else:
                self.savings = self.savings + amount
                self.balance = self.balance - amount
                print("Transfer to savings was successful. " + self.name + "'s updated savings status is: " + str(self.savings))

        else:
            if amount > self.savings:
                print("!!! Warning: " + self.name + " is trying to transfer more money than is currently in their savings !!! \nThere is only " +
                      str(self.savings) + " left to transfer from savings. \nPlease try again.")
            else:
                self.savings = self.savings - amount
                self.balance = self.balance + amount
                print("Transfer from savings was successful. " + self.name + "'s updated savings status is: " + str(self.savings))

        if self.savings == 0:
            print("There is no money left in savings.")
        if self.balance == 0:
            print("There is no money left in the normal bank account.")

# ----------------------------------------------------------------------------------------------------------------------
# main
# ----------------------------------------------------------------------------------------------------------------------

me = Customer("Carlotta")
me.perform_deposit(125)

my_savings = SavingsCustomer("Me")
my_savings.perform_deposit(345)
my_savings.transfer_savings(58,True)
my_savings.transfer_savings(59,False)
my_savings.transfer_savings(50,False)


