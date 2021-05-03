# 1. Write a class for implementing an infinite
# iterator that gives out Fibonacci numbers.


class Fibonacci:
    def __init__(self):
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        f = self.a
        self.a, self.b = self.b, self.a + self.b
        return f

x = Fibonacci()
i=0
while i <= 10:
    print(next(x),end=' ')
    i+=1


# 2. Write two classes Squares and SquaresIterator to implement an
# iterable that gives squares of numbers and supports multiple scans.

class Squares:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def __iter__(self):
        return SquaresIterator(self)


class SquaresIterator:
    def __init__(self, source):
        self.source = source
        self.current = source.start

    def __next__(self):
        if self.current > self.source.stop:
            raise StopIteration
        else:
            x = self.current * self.current
        self.current += 1
        return x


squares = Squares(1,10)

for square in squares:
    print(square)



# 3. Implement an iterator that gives squares of numbers
# using a single class.


class Squares:
    def __init__(self, start, stop):
        self.current = start
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.stop:
            raise StopIteration
        else:
            x = self.current * self.current
        self.current += 1
        return x



# 4. Write two classes Factorial and FactorialIterator to
# implement an iterable that gives factorials of numbers and
# supports multiple scans.


class Factorial:
    def __init__(self, high):
        self.high = high

    def __iter__(self):
        return FactorialIterator(self)


class FactorialIterator:
    def __init__(self, source):
        self.source = source
        self.factor = 1
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.source.high < self.current:
            raise StopIteration
        else:
            self.factor *= self.current
            self.current += 1
            return self.factor



f = Factorial(5)

for i in f:
    print(i)