# 1. The following dictionary has fruit names as keys and their prices as values.
D = {'apple':100, 'banana':200, 'grapes':55, 'guava':60 }

#  Write a for loop that iterates over this dictionary and increases the
#  price of a fruit by 10, if its price is less than 100, otherwise it decreases
#  the price by 10.

for k,v in D.items():
    D[k] = D[k] + 10 if v < 100 else D[k] - 10

print(D)

# 2. What is wrong in the following code.
L = [ ['John', [88,89,78] ],  ['Sam', [89,76,99] ],  ['Dev', [85,67,89] ] ]
for name, m1,m2,m3 in L:
     total = m1+m2+m3
     print(name, total)


L = [ ['John', [88,89,78] ],  ['Sam', [89,76,99] ],  ['Dev', [85,67,89] ] ]

for name,[m1,m2,m3] in L:
    total = m1+m2+m3
    print(name, total)

# 3. Write a program to create this dictionary in which the keys are numbers and
# values are their squares.
# { 1:1, 2:4, 3:9, 4:16, 5:25}
d = {}
for i in range(1,6):
    d[i] = i * i
print(d)

# 4. Write a program to enter more student records inside the following dictionary.

students = { 105416 : { 'name':'John',
                        'age': 21,
                        'marks':  { 'Maths' :  89,
                                   'Physics' : 78,
                                   'Chemistry':91 }
                       },
             144547 : { 'name':'Dev',
                            'age': 23,
                        'marks': { 'Maths' :  88,
                                   'Physics' : 77,
                                   'Chemistry':98 }
                      },
             132399 : { 'name':'Mary',
                        'age': 22,
                        'marks':  { 'Maths' :  99,
                                    'Physics' : 87,
                                    'Chemistry':88 } ,
                      }
            }

done_entering = False

while not done_entering:
    studentID = input("Enter student ID: ")
    students[studentID]= {}
    students[studentID]['name'] = input("Enter student name: ")
    students[studentID]['age'] = int(input("Enter student age: "))
    students[studentID]['marks'] = {}
    students[studentID]['marks']['Maths'] = int(input("Enter student math grade: "))
    students[studentID]['marks']['Physics'] = int(input("Enter student physics grade: "))
    students[studentID]['marks']['Chemistry'] = int(input("Enter student chemistry grade: "))

    done_entering = input("Press enter to enter another student, otherwise press any key")


for id,student in students.items():
    print(id)
    for k, v in student.items():
        print(k,'-->', v)
    print('-'*40)




 # 5. Write a program that finds the shortest and the longest string from a
# list of strings.


L = ['kaslk','j','jbsackjb','max']
min_s = L[0]
max_s = L[0]

for i in range(1,len(L)):
    if len(L[i]) < len(min_s):
        min_s = L[i]
    if len(L[i]) > len(max_s):
        max_s = L[i]

print(f"max string is: {max_s}; min string is: {min_s}")


# 6.Write a program that inserts all common items of these 2 lists into a
# third list L3.

L1  = ['China', 'Brazil', 'India', 'Iran', 'Iraq', 'Russia']
L2  = ['Italy', 'Japan', 'China', 'Russia', 'Nepal', 'France']


list(set(L1).intersection(set(L2)))

# or

L3 = []

for l_1 in L1:
    for l_2 in L2:
        if l_1 == l_2:
            L3.append(l_1)
print(L3)

# or

for l_1 in L1:
    if l_1 in L2:
        L3.append(l_1)

print(L3)

# 7.
D  = {'pen':10, 'pencil':5, 'eraser':8, 'marker':15, 'ruler':19 }
# Draw the following chart for this dictionary
#
# pen         ----------
#
# pencil     -----
#
# eraser     --------
#
# marker   ---------------
#
# ruler       -------------------

for k,v in D.items():
    print(k.ljust(8),'-'*v)


# 8. In this dictionary, keys are names of fruits and values are
# their respective prices. For fruits that are out of stock, price is
# marked as None. Iterate over this dictionary and print only those fruits
# with their prices, that are in stock. Use ljust() and rjust() methods of
# str type to align your output.

D  = {'pen':10, 'pencil':5, 'eraser':8,  'sharpener':None, 'marker':15, 'ruler':None }

for item, price in D.items():
    if price is not None:
        print(item.ljust(8,'.'), str(price).rjust(3))

# or

for item, price in D.items():
    if price!=None:
        print(item.ljust(8,'.'), str(price).rjust(3))


# 9. Create a randomised list of size 10, that contains random numbers in the
# range 1 to 50. Use randint function from random module.

import random
L_rand = []

for i in range(10):
    L_rand.append(random.randint(1,50))

print(L_rand)

# 10. Fibonacci series is a series of numbers in which each number is the
# sum of previous two numbers.

# 1  1  2  3  5  8  13  21  34  55  89  144  233

# (i) Print first n Fibonacci numbers using a for loop.

# (ii) Print all Fibonacci numbers less than a number n, using a while loop

x,y = 1, 1
n = 10

for i in range(n):
    print(x, end= ' ')
    y,x = x+y,y



x,y = 1, 0
n = 10

while n > x:
    print(x, end=' ')
    y += x
    y, x = x, y


n = 10
x,y = 1,1
for i in range(n):
  print(x, end=' ')
  x,y = y,x+y
print()

 # 11. What is wrong in the following code.

text = input('Enter some text : ')
ch = input('Enter a character : ')
i = 0
while  i<len(text) and text[i]!=ch:
   i+=1
print(f'{ch} appears at index {i} in {text}')

# The following two exercises(12 and 13) ask you to print pyramid patterns.
# They might not be of practical use but are helpful in understanding loops
# and are very interesting.


# 12.

n=4
for i in range(1, n+1):
    print(i*'*')

n=4
for i in range(1,n+1):
    print(i*str(i))

n=4
for i in range(1,n+1):
    print(' ' * (n-i), end='')
    print('*' * i)

n=4
for i in range(1,n+1):
  print(' ' * (n-i), end='') # for printing spaces before asterisks
  print('*' * (2*i-1))