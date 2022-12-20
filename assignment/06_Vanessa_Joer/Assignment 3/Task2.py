class Costumer:
    def __init__(self, name, balance = 0): #making a class Costumer that can be given a name and sets the balance to zero
        self.name = name
        self.balance = balance


    def deposit(self, amount): #the function takes the amount of money the costumer wants to add and either shows an error if the amount is in the negative, or displays the new balance
        if amount < 0:
            print('ERROR: You Can Not Withdraw A Negative Amount Of Money')
        else:
            self.balance += amount 
            print('Your New Balance Is: %d' % self.balance)

    def withdraw(self, amount): #this function checks wether or not the amount the costumer wants to withdraw is higher than the amount in the bank, if yes, it displays an error, if no, it takes the amount and shows the new balance
        if amount > self.balance:
            print('ERROR: You Can Not Overdraw Your Account')
        else:
            self.balance -= amount
            print('Your New Balance Is: %d' % self.balance)

            
