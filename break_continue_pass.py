# 1. Write a program that creates a list of all prime numbers from 100
# to 300.

L_prime = []

for n in range(100,300):
    for i in range(2,n//2):
        if n%i== 0:
            break
    else:
        L_prime.append(n)
print(L_prime)


# 2. Write a program that simulates dice rolling. Use randint from random module.

import random

while True:
    print("Rolling the dice")
    print(random.randint(1,6))
    response = input("Want to roll the dice again? [y/n]")
    if response == 'y':
        continue
    else:
        break


# 3. Write a program that adds numbers entered by the user. Stop entering when
# user enters 0. Don't add numbers that are negative or greater than 500.

total = 0

while True:
    number = int(input("Enter a number between 0 and 500: "))

    if 0 < number < 501:
        total += number
    elif number == 0:
        break
    else:
        print("Invalid entry, try again")
        continue

print(total)

# 5. You are given a text string and a list of prohibited words.
# Use a for loop with else block, to find whether the text string contains any
# prohibited word. If you find a prohibited word display 'Found a prohibited word'.
# If the text string does not contain any prohibited word, then display
# 'No prohibited word in the list'.


text = 'This is crazy sample'
prohibited_words = ['mad', 'lunatic', 'crazy']


for word in text.split(" "):
    if word in prohibited_words:
       print("Found a prohibited word")
       break
else:
    print("No prohibited word in the list")

# 7. Write a for loop to print all divisors of a number.

n = 10

for d in range(1,n+1):
    if n%d== 0:
        print(d)


# 8. Find the smallest divisor of a number greater than 1,
# using (i) a while loop (ii) for loop


n = 105

for d in range(2,n+1):
    if n%d== 0:
        # print(d)
        break
print(d)

i = 2
while n%i!=0:
    i+=1

print(i)

# 9. Write a for loop(use continue statement) to increase the price of all
# items by 10%, except fruits.   Rewrite the loop without continue statement.


fruits = {'apple', 'banana', 'grapes'}
veggies = {'potato', 'onion', 'cabbage'}
stationery = {'pencil', 'eraser', 'sharpener', 'marker'}
prices = {'pencil':10,'eraser':5,'sharpener':4, 'marker':20,'potato':30,
         'onion':25, 'cabbage':22,'apple':90, 'banana':60, 'grapes':80}


for k,v in prices.items():
    if k in fruits: continue
    else:
        prices[k] += v*0.1

print(prices)

# or

for k,v in prices.items():
    if k not in fruits:
        prices[k] += v*0.1

print(prices)


# 10.  We saw this loop in the lecture on break,modify this so that all the
# non-prime (composite) numbers are also printed.

for n in range(2,100):
  isprime=True
  for i in range(2,n):
       if n%i == 0:
           isprime = False
           break
  if isprime:
     print(n)



for n in range(2,100):
  isprime=True
  for i in range(2,n):
       if n%i == 0:
           isprime = False
           print(f"{n} is not a prime as {n} = {i} * {n//i}")
           break
  if isprime:
     print(f"{n} is prime")

