# 1. The range function does not take a float value as a step.
# The call range(1, 10, 0.5) does not work. Write your own version of
# range that can accept a float value as the step.


def test_range(start, stop=None, step=1):
    if stop is None:
        stop = start
        start = 0

    while start < stop:
        yield start
        start += step


for x in test_range(5):
    print(x)

for x in test_range(2,5,0.5):
    print(x)

for x in test_range(0.5,3):
    print(x)


# 2. Write a generator function that behaves like enumerate.

def test_enumerate(sequence):
    i = 0

    for element in sequence:
        yield i,element
        i += 1

for i in test_enumerate(['dog','cat','bird']):
    print(i)


# 3. Write a generator function that takes a number n and then
# yields values from n to 1 and then again upto n. If n is 5,
# the values that are generated are : 5 4 3 2 1 2 3 4 5

def reverse_counter(n):
    for i in range(n,1,-1):
        yield i
    for i in range(1,n+1):
        yield i


for i in reverse_counter(5):
    print(i)

# 4. Write an infinite generator that yields values 1 -1 2 -2 3 -3……..
# Use it in a loop with break statement.


def gfc():
    i = 1
    while True:
        yield i
        yield -i
        i +=1


for i in gfc():
    if i == 5:
        break
    print(i, end=' ')

# 5. The following code does not work.

L = [1,2,3,4,5]
def combine1(a,b,c):
    return a+b+c
for i in combine1(L, range(10,15), "ABCDEF"):
print(i, end = ' ')

# Write a generator function named combine that yields
# values from the list, range function and the string.

def combine2(a,b,c):
    for i in a:
        yield i

    for i in b:
        yield i

    for i in c:
        yield i


for i in combine2(L, range(10,15), "ABCDEF"):
    print(i, end = ' ')


# 6. Write a generator that generates squares of numbers.

def squares(start,stop):
    while start <= stop:
        yield start * start
        start += 1

for i in squares(2,10):
    print(i, end=' ')


# 7. Write a generator function that accepts a sequence
# and generates its numbers in reverse order.

def reverse_order(sequence):
    for i in range(len(sequence)-1,-1,-1):
        yield sequence[i]


for item in reverse_order([1,2,3,4,5]):
    print(item, end=' ')