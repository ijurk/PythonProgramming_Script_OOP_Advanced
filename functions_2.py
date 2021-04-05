# 1. In the lecture on returning multiple values, we had written this function.

def max_min_avg(L):
   return max(L), min(L), sum(L)/len(L)

# Modify this function so that it can work with variable number of arguments.


def max_min_avg(*args):
   return max(args), min(args), sum(args)/len(args)


max_min_avg(5,6,9,6,4)
max_min_avg(5,6,9)

# 2.

def result(*args, grade=False):
    total = sum(args)
    per = total / len(args)
    print(f'Total Marks = {total}, percentage = {per}%')
    if grade == False:
        return
    if per > 80:
        print('Grade A')
    elif per > 50:
        print('Grade B')
    else:
        print('Grade C')


result(90,90,90, grade = True)

result(90,90,90, True)

# Give reason for the output of the second call.
#The grade parameter is placed after *args, so it will only accept key word argument,
# because it was not a key word argument, the function unpacks it as part
# of the args tuple and uses 1 for True. Since grade argument is not passed, it uses
# the default which is False

# 3. What will be the output of this-

def func(n):
    print('hello ' * n)


def f(x, y):
    x(y)


f(func, 4)

# The output will be: 'hello hello hello hello '

# 4. Write a function that accepts any number of integers passed to it and
# returns their product.

def multiplication(*args):
    multi = 1
    for n in args:
        multi*=n
    return multi


multiplication(5,2,2)
multiplication(5,2,2,4,5)

# 5. Write a function that takes in a variable number of strings and returns a
# list of all those strings in reverse form (use list comprehension).


def revers_string(*args):
    rev = [s[::-1] for s in args]
    return rev

revers_string('hello','test','house')
revers_string('hello','test','house','beach','sun')

# 6.In the function definition of the function display(), make changes such
# that the user is forced to send keyword arguments for the last two parameters.

def display(L, start='', end=''):
    for i in L:
        if i.startswith(start) and i.endswith(end):
            print(i, end=' ')


display(dir(str), 'is', 'r')


def display(L, *,start='', end=''):
    for i in L:
        if i.startswith(start) and i.endswith(end):
            print(i, end=' ')


display(dir(str), start = 'is', end = 'r')

# 7. What will be the output of this code.

M = [[1, 6, 2, 3],
     [7, 5, 6, 9],
     [8, 9, 3, 2]]

T = [list(t) for t in zip(*M)]
print(T)

# output will be: T = [
#                         [1,7,8],
#                         [6,5,9],
#                         [2,6,3],
#                         [3,9,2]
#                       ]


# 8. Is there any error in the following code. NO

def subtract(a, b):
    print(a - b)


def add(a, b):
    print(a + b)


def multiply(a, b):
    print(a * b)


def divide(a, b):
    print(a // b)


d = {'a': add, 's': subtract, 'm': multiply, 'd': divide}
choice = ''
while choice != 'q':
    print('a - Add')
    print('s - Subtract')
    print('m - Multiply')
    print('d - Divide')
    print('q - Quit\n')

    choice = input('Enter your choice :')
    if choice == 'q':
        break
    x = int(input('Enter a number : '))
    y = int(input('Enter another number : '))

    d[choice](x, y)