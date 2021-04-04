# 1. Write a function that multiplies all the entries of a list by a number.
L = [1,2,3,4]


def func(l,n):
    for i in range(len(l)):
        l[i]*=n

func(L,3)
print(L)

# 2. Write a function that takes a number and returns the sum of digits in it.

number = 156

def sum_dig(n):
    sum_d = 0
    for ch in str(n):
        sum_d+=int(ch)
    return sum_d

sum_dig(number)

# or

def sum_digits(n):
    s = 0
    while n != 0:
        s += n % 10
        n //= 10
    return s


sum_digits(2134)

# 3. Write a function do_nothing() that does nothing when executed.

def do_nothing():
     pass

do_nothing()

# 4. Write a function that takes in a string and returns number of vowels and consonants in that string.

s = 'ao\h;b svi vhndovhn'

def num_vowles_consonants(s):
    vowels = 0
    consonants = 0
    for ch in s:
        if ch.isalpha():
            if ch.lower() in 'aeiou':
                vowels+=1
            else:
                consonants+=1
    return vowels, consonants

num_vowles_consonants(s)

# 5. Write a function is_prime that takes in an integer and returns True if the argument is prime,
# otherwise returns False.

def is_prime(num):
    for n in range(2,num):
        if num%n == 0:
            return False
        else:
            return True

number = 5
is_prime(number)

# 6. Write a function that returns factorial of a number.

number = 5

def factorial_num(n):
    fact = 1
    while n > 0:
        fact*=n
        n-=1
    return fact

factorial_num(number)

# 7. Write a function that takes two arguments and returns sum, difference and product of
# those two arguments.

def func(a,b):
    return a+b, a-b, a*b

func(12,8)

# 8. Write a function named find that takes in a list and a value. It should return True if that
# value is found in the list and False otherwise.
# Does your function work for strings, tuples, sets and dictionaries also ?

def find(L,a):
    if a in L:
        return True
    else:
        return False

find('hello','i')
find([1,5,6,9],10)

# 9. Write a function named fizzbuzz that takes an integer as argument and returns
# 'Fizz' if that integer is divisible by 3, returns 'Buzz' if it is divisible by 5
# and returns 'FizzBuzz' if it is divisible by both 3 and 5, otherwise it returns the integer itself.

# Use you function fizzbuzz in the following code.
#
def func(x):
   for i in range(1,x+1):
      print(fizzbuzz(i))



def fizzbuzz(n):
    if n%3 == 0 and n%5 == 0:
        return 'FizzBuzz'
    elif n%3 == 0:
        return 'Fizz'
    elif n%5 == 0:
        return 'Buzz'
    return n

func(50)


# 10. Write a function that takes in a list of integers and returns the number of
# even and odd numbers from that list.

L = [5,6,4,2,2,4]

def even_odd_count(L):
    even = odd = 0
    for i in L:
        if i%2 == 0:
            even+=1
        else:
            odd+=1
    return even, odd

even_odd_count(L)

# 11. If two consecutive odd numbers are both prime (e.g. (3,5) (17, 19)) then they are known as
# twin primes. Write a function that returns a tuple containing all twin primes in a given range.
# Use the is_prime function defined in question 5.

def twin_prime(x,y):
    tp = []
    for i in range(x,y+1):
        if is_prime(i) and is_prime(i+2):
            tp.append((i,i+2))
    return tp

print(twin_prime(2,15))