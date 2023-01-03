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
    def __init__(self, name, balance, savings):
        super().__init__(name, balance)
        self.savings = savings

    def s_tracking(self):
        Customer.tracking(self)
        print("savings: ", self.savings)

    def transfer_main2sav(self, amount):
        if amount < 0:
            print(">>cannot transfer negative amount<<")
        elif self.balance - amount < 0:
            print(">>insufficient balance<<")
        self.balance = self.balance - amount
        self.savings = self.savings + amount

    def transfer_sav2main(self, amount):
        if amount < 0:
            print(">>cannot transfer negative amount<<")
        elif self.savings - amount < 0:
            print(">>insufficient savings<<")
        else:
            self.balance = self.balance + amount
            self.savings = self.savings - amount


bob = Customer('bob', 0)
print(bob.tracking())
bob.deposit(100)
bob.withdraw(50)
print("")

bob = CustomerSavings(bob.name, bob.balance, 50)
print(bob.s_tracking())

print("")

bob.transfer_main2sav(50)
print(bob.s_tracking())

print("")

bob.transfer_sav2main(100)
print(bob.s_tracking())

print("")

bob.transfer_main2sav(200)

