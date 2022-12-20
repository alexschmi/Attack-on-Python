class Customer():
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def tracking(self):
        print("name:", self.name)
        print("balance:", self.balance)

    def deposit(self, amount):
        if amount < 0:
            print("cannot deposit negative amount")
        else:
            self.balance = self.balance + amount
            print(">>deposit success<<")
            print("new balance:", self.balance)

    def withdraw(self, amount):
        if amount < 0:
            print(">>cannot withdraw negative amount<<")
        elif self.balance - amount < 0:
            print(">>insufficient balance<<")
        else:
            self.balance = self.balance - amount
            print(">>withdrawal success<<")
            print("new balance:", self.balance)


class CustomerSavings(Customer):
    def __init__(self, name, balance):
        super().__init__(name, balance)

bob = Customer('bob', 0)
print(bob.tracking())
bob.deposit(100)
bob.withdraw(50)
