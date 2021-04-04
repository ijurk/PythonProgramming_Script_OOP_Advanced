# 1. Write a loop to iterate over the keys of this dictionary in reverse
# sorted order.

D = { 'apple':210, 'banana':100, 'grapes':90, 'mango':250, 'cherry':225, 'guava':80 }

for key in reversed(sorted(D)):
    print(key)

# 2. Write a for loop to capitalize each string of this list. Use enumerate().

L = ['this', 'that', 'the', 'hello world']

for i,item in enumerate(L):
    L[i] = item.capitalize()

print(L)

# . Given a list of integers, write a for loop that multiplies each odd number
# of the list by 2 and divides each even number by 2. Use if else operator
# inside the loop.

listA = [1,6,9,76,13,5]

for i,number in enumerate(listA):
    listA[i] = number//2 if number%2==0 else number*2

print(listA)


# 4. Write a for loop to print the elements of the following list in sorted
# order without duplicates.


L = [2,4,1,6,7,8,9,7,1,2,6]

for n in set(sorted(L)):
    print(n, end=" ")

# 5. Write a program to create the following dictionary in which keys are
# numbers and values are their factorials. Don't use nested loops.

{0: 1,1: 1,2: 2,3: 6,4: 24, 5: 120, 6: 720, 7: 5040}

D={}
x = 1

for n in range(8):
    if n!=0:
        x*=n
    D[n] = x

print(D)

# or

D={}
D[0] = 1

for i in range(1,8):
    D[i] = i*D[i-1]
print(D)


# 6. Write a program to remove nth occurrence of an item from a list.

L = [11,23,31,4,23,45,11,23,79,23,81,43,23]
n = 3
item = 23
count = 0

for i,num in enumerate(L):
    if num == item:
        count+=1
    if count == n:
        L.pop(i)
        break
print(L)

# 7. Print the names of unique cities from the following dictionary.
# The city names should be in all capitals.

D = {'Sam': 'Paris', 'Tom': 'London', 'Bob': 'Paris', 'Dev': 'Bareilly', 'Tim':'Paris', 'Raj':'London'}


for city in set(D.values()):
    print(city.upper())


# 8. In the lecture on for loop, we encrypted a message by replacing each
# letter by subsequent letter. Modify that program so that a character
# at even index is replaced by subsequent letter and a character at
# odd index is replaced by previous character.


message = 'Hello World'
emessage = ''


for i,ch in enumerate(message):
    if i%2==0:
        emessage += chr(ord(ch)+1)
    else:
        emessage += chr(ord(ch)-1)

print(emessage)

dmessage = ''

for i, ch in enumerate(emessage):
    if i % 2 == 0:
        dmessage += chr(ord(ch) - 1)
    else:
        dmessage += chr(ord(ch) + 1)

print(dmessage)

# 9. Encrypt the strings of this list by changing each letter of the
# string to next letter.

L = ['this', 'that', 'here', 'there']

eL = []

for word in L:
    eword = ''
    for ch in word:
        eword += chr(ord(ch)+1)
    eL.append(eword)

print(eL)

dL = []

for word in eL:
    dword = ''
    for ch in word:
        dword += chr(ord(ch) - 1)
    dL.append(dword)

print(dL)

# 10. Write a program to find whether a list contains any duplicate value.

L = [2,9,3,4,1,2,5,7,8,3,6]
prev = None

for item in sorted(L):
    if prev == item:
        print('Duplicate item found')
        break
    prev = item
else:
    print('No duplicates found')


# 11. The following for loop is written to delete all occurrences of an
# item from a list.  Will it work properly? If not, what changes need
# to be made in this code.
L = [1,2,3,2,4,5,2,2,2,7]
x = 2
for item in L:
  if item == x:
    L.remove(item)
print(L)

# correction: iterate over a copy of teh list:

L = [1,2,3,2,4,5,2,2,2,7]
x = 2
for item in L[:]:
  if item == x:
    L.remove(item)
print(L)


# 12. What will be the output of this program -

L = [1,2,-3,4,-5,-6,8]
i = 0
while i < len(L):
   print(i, L[i])
   if L[i] < 0:
      L.remove(L[i])
   i+=1
print(L)

# 13.In this for loop, we are iterating over the items of a list and
# finding the largest even number.
# Make changes in this code so that you get the largest even number
# as well as its index.

data = [2,3,1,4,7,5]
max_even = 0
for i,item in enumerate(data):
   if item%2==0 and item>max_even:
       max_even = item
       max_i = i
print(f'Largest even number is {max_even} and it index is {max_i}')



# 14.

L = [1,2,-3,4,-5,-6, -8]
for item in L[:]:
       if item>=0:
          L1.append(item)
print(L)
# Instead of using this list copy solution for the problem that we saw in our lecture, we could do the following.

L = [1,2,-3,4,-5,-6, -8]
L1 = []
for item in L:
       if item>=0:
          L1.append(item)
L = L1
print(L)

# What kind of problems can this solution create? It will create a new object and L will reffer to it. It will not change the original object.
# If there are multiple references to teh original object it will not change those other references

# 15.
D = { 'John' :  [90,78,87,67] ,
          'Sam' :  [95,76,78,57] ,
          'Dev' :  [80,69,59,45]
        }
subjects = ['Physics', 'Chemistry', 'Maths', 'Biology']
max_marks = [100, 80, 100, 75]
pass_marks = [40, 25, 40, 20]
# Write a program that displays the following output from the above data. Use zip in for loop to iterate over the lists.

for key in D:
    print(key, end='\n'+'-'*50+'\n')
    for subject,max_mark, pass_mark, mark in zip(subjects,max_marks, pass_marks,D[key]):
        print(f"{subject:10}{max_mark:4}{pass_mark:4}{mark:5}")
    print(f"Total = {sum(D[key]):3}")
    print(f"Percentage = {sum(D[key])/sum(max_marks)*100:4.2f}")
    print('-'*50)


