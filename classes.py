# Make a class that represents a bank account.
# Create four methods named set_details, display,
# withdraw and deposit.
#
# In the set_details method, create two instance variables :
# name and balance. The default value for balance should be zero.
# In the display method, display the values of these two instance variables.
#
# Both the methods withdraw and deposit have amount as parameter.
# Inside withdraw, subtract the amount from balance and inside deposit,
# add the amount to the balance.
#
# Create two instances of this class and call the methods on
# those instances.


class BankAccount:
    def set_details(self, name, balance=0):
        self.name = name
        self.balance = balance

    def display(self):
        print(f'Bank Account Name: {self.name} \nBalance: {self.balance}')

    def withdraw(self,amount):
        self.balance -= amount

    def deposit(self,amount):
        self.balance += amount


ba1 = BankAccount()
ba2 = BankAccount()

ba1.set_details('Citi')
ba1.display()
ba1.deposit(150)
ba1.display()
ba1.withdraw(50)
ba1.display()

ba2.set_details('FP')
ba2.display()
ba2.deposit(100)
ba2.display()
ba2.withdraw(35)
ba2.display()

