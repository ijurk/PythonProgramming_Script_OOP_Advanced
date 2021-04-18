# 1. In the BankAccount class that you had created in the previous exercise,
# delete the set_details() method and create an __init__ method.


class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def display(self):
        print(f'Bank Account Name: {self.name} \nBalance: {self.balance}')

    def withdraw(self,amount):
        self.balance -= amount

    def deposit(self,amount):
        self.balance += amount


ba1 = BankAccount('Citi',200)
ba2 = BankAccount('FP',500)


ba1.display()
ba1.deposit(150)
ba1.display()
ba1.withdraw(50)
ba1.display()


ba2.display()
ba2.deposit(100)
ba2.display()
ba2.withdraw(35)
ba2.display()


# 2. Create a class named Book with an __init__ method. Inside the __init__
# method, create the instance variables isbn, title, author, publisher,
# pages, price, copies.


class Book:
    def __init__(self,isbn,title, author, publisher, pages, price, copies):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.publisher = publisher
        self.pages = pages
        self.price = price
        self.copies = copies

    def display(self):
        print(f'isbn: {self.isbn}, title: {self.title}, price: {self.price}, number of copies: {self.copies}')


book1 = Book('957-4-36-547417-1', 'Learn Physics','Stephen', 'CBC', 350, 200,10)
book2 = Book('652-6-86-748413-3', 'Learn Chemistry','Jack', 'CBC', 400, 220,20)
book3 = Book('957-7-39-347216-2', 'Learn Maths','John', 'XYZ', 500, 300,5)
book4 = Book('957-7-39-347216-2', 'Learn Biology','Jack', 'XYZ', 400, 200,6)

book1.display()
book2.display()
book3.display()
book4.display()


# 3. For the Book class that you have created, write a method named
# in_stock that returns True if number of copies is more than zero,
# otherwise it returns False.
# Create another method named sell that decreases the number of copies
# by 1 if the book is in stock, otherwise it prints the message that the
# book is out of stock.



class Book:
    def __init__(self,isbn,title, author, publisher, pages, price, copies):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.publisher = publisher
        self.pages = pages
        self.price = price
        self.copies = copies

    def in_stock(self):
        return True if self.copies > 0 else False

    def sell(self):
        if self.in_stock():
            self.copies -= 1
        else:
            print(f'The book {self.title} is out of stock')

    def display(self):
        print(f'isbn: {self.isbn}, title: {self.title}, price: {self.price}, number of copies: {self.copies}')


# 4. Create a list named books that contains the 4 Book instance objects
# that you have created in question 2. Iterate over this list using a for
# loop and call display() for each object in the list.

# Write a list comprehension to create another list that contains
# title of books written by Jack.


books = [book1, book2, book3, book4]

for book in books:
    book.display()

jack_titles = [book.title for book in books if book.author == 'Jack']
print(jack_titles)


# 5. In the Book class, create a property named price such that the
# price of a book cannot be less than 50 or more than 1000.

class Book:
    def __init__(self,isbn,title, author, publisher, pages, price, copies):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.publisher = publisher
        self.pages = pages
        self.price = price
        self.copies = copies

    def in_stock(self):
        return True if self.copies > 0 else False

    def sell(self):
        if self.in_stock():
            self.copies -= 1
        else:
            print(f'The book {self.title} is out of stock')

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        if 50 <= new_price <= 1000:
            self._price = new_price
        else:
            raise ValueError('Invalid price. Price cannot be less than 50 and more than 1000.')

    def display(self):
        print(f'isbn: {self.isbn}, title: {self.title}, price: {self.price}, number of copies: {self.copies}')


book5 = Book('957-7-39-347216-2', 'Learn Biology','Jack', 'XYZ', 400, 250,6)

book5.price
book5.price = 5000
book5.price = 500
book5.price
book5.display()

# 6. Make a class Fraction that contains two instance variables, nr and
# dr (nr stands for numerator and dr for denominator).
# Define an __init__ method that provides values for these instance variables.
# Make the denominator optional by providing a default argument of 1.

# In the __init__ method, make the denominator positive if it is negative.
# For example  -2/-3 should be changed to 2/3 and 2/-3 to -2/3.

# Write a method named show that prints numerator, then '/' and then
# the denominator.

# Make sure that you write this class as we will be using it to learn
# magic methods.


class Fraction:
    def __init__(self, nr, dr=1):
        self.nr = nr
        self.dr = dr
        if self.dr < 0:
            self.nr *= -1
            self.dr *= -1

    def show(self):
        print(f'{self.nr} / {self.dr}')


f1 = Fraction(-2,-3)
f1.show()

f2 = Fraction(2,-3)
f2.show()

# 7. Define a method named multiply that multiples two Fraction instance objects.
# For multiplying two fractions, you have to multiply the numerator with
# numerator and denominator with the denominator.

# Inside the method, create a new instance object that is the product of
# the two fractions and return it. Write your method in such a way that it
# supports multiplication of a Fraction by an integer also.

# Similarly define a method named add to add two Fraction instance objects.
# Sum of two fractions n1/d1 and n2/d2 is (n1*d2 + n2*d1) / (d1*d2).
# This method should also support addition of a Fraction by an integer.


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





f1 = Fraction(2,3)
f1.show()
f2 = Fraction(3,4)
f2.show()
f3 = f1.multiply(f2)
f3.show()
f3 = f1.add(f2)
f3.show()
f3 = f1.add(5)
f3.show()
f3 = f1.multiply(5)
f3.show()


# 8. For the following class Product, create a read only property named selling_price
# that is calculated by deducting discount from the marked_price.
# The instance variable discount represents discount in percent.

class Product:
    def __init__(self, id, marked_price, discount):
        self.id = id
        self.marked_price = marked_price
        self.discount = discount

    def display(self):
        print(self.id, self.marked_price, self.discount)

    @property
    def selling_price(self):
        return self.marked_price * (1 - self.discount / 100)



p1 = Product('X879', 400, 6)
p1.display()
p1.selling_price


# 9. Suppose after some time, you want to give an additional 2% discount on a product,
# if its price is above 500. To incorporate this change,
# implement discount as a property in your Product class.

class Product:
    def __init__(self, id, marked_price, discount):
        self.id = id
        self.marked_price = marked_price
        self._discount = discount

    @property
    def selling_price(self):
        return self.marked_price * (1 - self.discount / 100)

    @property
    def discount(self):
        return self._discount + 2 if self.marked_price > 500 else self._discount

    @discount.setter
    def discount(self, new_discount):
        self._discount = new_discount

    def display(self):
        print(self.id, self.marked_price, self.discount)


p1 = Product('A234', 100, 5)
p2 = Product('X879', 400, 6)
p3 = Product('B987', 990, 4)

print(p1.id, p1.selling_price, p1.discount)
print(p2.id, p2.selling_price, p2.discount)
print(p3.id, p3.selling_price, p3.discount)

p3.discount = 10
p3.display()
p3.discount
print(p3.id, p3.selling_price,p3.discount)


# 10. Write a Circle class with an instance variable named radius and a
# method named area. Create two more attributes named diameter and
# circumference and make them behave as read only attributes.

# Perform data validation on radius, user should not be allowed to
# assign a negative value to it.
#
# For a circle
#
# diameter =  2 * radius
#
# circumference =  2 * 3.14 * radius
#
# area =  3.14 * radius * radius


class Circle:
    def __init__(self,radius):
        self.radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, new_radius):
        if new_radius > 0:
            self._radius = new_radius
        else:
            raise ValueError('Radius should be positive.')

    @property
    def diameter(self):
        return 2 * self._radius

    @property
    def circumference(self):
        return 2 * 3.14 * self._radius

    def area(self):
        return 3.14 * self._radius * self._radius



c1 = Circle(-5)
c1.radius
c2 = Circle(2)
c2.radius
c2.area()
c2.diameter
c2.circumference
c2.radius = 5
c2.radius
c2.area()
c2.diameter
c2.circumference




