# 1. This is a function to find the highest common
# factor of two numbers
# Make it a static method in the Fraction class that you had written in earlier exercise.

class Fraction:
    def __init__(self, nr, dr=1):
        self.nr = nr
        self.dr = dr
        if self.dr < 0:
            self.nr *= -1
            self.dr *= -1

    def show(self):
        print(f'{self.nr} / {self.dr}')

    def multiply(self,other_fraction):
        if isinstance(other_fraction, int):
            other_fraction = Fraction(other_fraction)
        return Fraction(self.nr * other_fraction.nr, self.dr * other_fraction.dr)

    def add(self, other_franction):
        if isinstance(other_franction, int):
            other_franction = Fraction(other_franction)
        return Fraction(self.nr*other_franction.dr + other_franction.nr*self.dr,self.dr*other_franction.dr)

    @staticmethod
    def hcf(x, y):
        x = abs(x)
        y = abs(y)
        smaller = y if x > y else x
        s = smaller
        while s > 0:
            if x % s == 0 and y % s == 0:
                break
            s -= 1
        return s


# 2. In your Fraction class, write a private instance method _reduce that reduces a fraction to
# its lowest terms. To reduce a Fraction to its lowest terms you have to divide the numerator and
# denominator by the highest common factor. Call this method in __init__and also call it on the resultant
# fraction in methods multiply and add.

class Fraction:
    def __init__(self, nr, dr=1):
        self.nr = nr
        self.dr = dr
        if self.dr < 0:
            self.nr *= -1
            self.dr *= -1
        self._reduce()

    def show(self):
        print(f'{self.nr} / {self.dr}')

    def multiply(self,other_fraction):
        if isinstance(other_fraction, int):
            other_fraction = Fraction(other_fraction)
        f = Fraction(self.nr * other_fraction.nr, self.dr * other_fraction.dr)
        f._reduce()
        return f

    def add(self, other_franction):
        if isinstance(other_franction, int):
            other_franction = Fraction(other_franction)
        f = Fraction(self.nr*other_franction.dr + other_franction.nr*self.dr,self.dr*other_franction.dr)
        f._reduce()
        return f

    def _reduce(self):
        common_factor = Fraction.hcf(self.nr, self.dr)
        if common_factor == 0:
            return

        self.nr //= common_factor
        self.dr //= common_factor

    @staticmethod
    def hcf(x, y):
        x = abs(x)
        y = abs(y)
        smaller = y if x > y else x
        s = smaller
        while s > 0:
            if x % s == 0 and y % s == 0:
                break
            s -= 1
        return s



f1 = Fraction(12,9)
f1.show()
f2 = Fraction(4,-16)
f2.show()
f3 = f1.multiply(f2)
f3.show()
f3 = f1.add(f2)
f3.show()
f3 = f1.add(5)
f3.show()
f3 = f1.multiply(5)
f3.show()



# 3. In the following class SalesPerson, add two class variables named total_revenue and names.
# The variable names should be a list that contains names of all salespersons and total_revenue
# should contain the total sales amount of all the salespersons.

class SalesPerson:

    total_revenue = 0
    names = []

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.sales_amount = 0
        SalesPerson.names.append(name)

    def make_sale(self, money):
        self.sales_amount += money
        SalesPerson.total_revenue += money

    def show(self):
        print(self.name, self.age, self.sales_amount)


s1 = SalesPerson('Joe', 50)
s2 = SalesPerson('Ann', 35)
s3 = SalesPerson('Mary', 20)

s1.make_sale(2000)
s1.make_sale(2500)
s2.make_sale(10000)
s2.make_sale(500)
s3.make_sale(5000)
s3.make_sale(150)

s1.show()
s2.show()
s3.show()

s1.total_revenue
s2.total_revenue
s3.total_revenue

s1.names
s2.names
s3.names
SalesPerson.names


# 4. Add a class variable named domains to the following Employee class.
# Make this class variable a set and it should store all domain names
# used by employees.

class Employee:

    domains = set()

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Employee.domains.add(email.split('@')[1])

    def display(self):
        print(self.name, self.email)


e1 = Employee('John', 'john@gmail.com')
e2 = Employee('Jack', 'jack@yahoo.com')
e3 = Employee('Jill', 'jill@outlook.com')
e4 = Employee('Ted', 'ted@yahoo.com')
e5 = Employee('Tim', 'tim@gmail.com')
e6 = Employee('Mike', 'mike@yahoo.com')

Employee.domains

# 5. In the following Employee class, add a class variable named allowed_domains.
# allowed_domains = {'yahoo.com', 'gmail.com', 'outlook.com'}
# Whenever an email is assigned, if the domain named is not in allowed_domains,
# raise a RuntimeError.


class Employee:

    allowed_domains = {'yahoo.com', 'gmail.com', 'outlook.com'}

    def __init__(self, name, email):
        self.name = name
        self.email = email

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, new_email):
        domain = new_email.split('@')[1]
        if domain in Employee.allowed_domains:
            self._email = new_email
        else:
            raise RuntimeError(f'Domain {domain} is not allowed.')

    def display(self):
        print(self.name, self.email)


e1 = Employee('Mark', 'mark@gmail.com')
e2 = Employee('Tim', 'tim@xmail.com')

e1.display()
e2.display()

e1.email = 'mark@ymil.com'
e1.display()

e2.email = 'tim@gmail.com'
e2.display()

# 6. The following program shows implementation of Stack Abstract data type using list. In a stack,
# elements are pushed and popped from one end of the stack which is called the top of the stack.
# This implementation has no maximum limit on the size of the stack. You have to introduce a maximum
# limit by adding a class variable named MAX_SIZE. In the push method, before inserting a new element,
# check the size of the stack and raise a RuntimeError if the stack is full.


class Stack:

    MAX_SIZE = 3

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def push(self, item):
        if Stack.MAX_SIZE == self.size():
            raise RuntimeError('Stack is full.')
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise RuntimeError("Stack is empty")
        return self.items.pop()

    def display(self):
        print(self.items)


# Test

if __name__ == "__main__":
    st = Stack()

    while True:
        print("1.Push")
        print("2.Pop")
        print("3.Peek")
        print("4.Size")
        print("5.Display")
        print("6.Quit")

        choice = int(input("Enter your choice : "))

        if choice == 1:
            x = int(input("Enter the element to be pushed : "))
            st.push(x)
        elif choice == 2:
            x = st.pop()
            print("Popped element is : ", x)
        elif choice == 3:
            print("Element at the top is : ", st.peek())
        elif choice == 4:
            print("Size of stack ", st.size())
        elif choice == 5:
            st.display()
        elif choice == 6:
            break;
        else:
            print("Wrong choice")
        print()


# 7. Class variables with immutable values can be used as defaults for instance variables.
# In the following BankAccount class, add an instance variable named bank in the __init__method.
# Add a class variable bank_name that will be used as default argument in the __init__
# method for bank parameter.


class BankAccount:
    bank_name = 'Citi'

    def __init__(self, name, balance=0, bank = bank_name):
        self.name = name
        self.balance = balance
        self.bank = bank

    def display(self):
        print(self.name, self.balance, self.bank)

    def withdraw(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount


a1 = BankAccount('John', 500, 'BOA')
a2 = BankAccount('Ann')

a1.display()
a2.display()