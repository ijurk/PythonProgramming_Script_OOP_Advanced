#  1. Write code to find sum of first n natural numbers using a
# (a) while loop
# (b) for loop
# (c) without any loop

n = 5
i = 1
s = 0

while i <= n:
    s += i
    i += 1

n = 5
for i in list(range(1,n+1)):
    s+=i

n = 5
sum(list(range(1,n+1)))

# 2. Factorial of a non-negative integer n, is the product of all positive
# integers less than or equal to n. For example, factorial of 6 is equal to
# 6*5*4*3*2*1 = 720
#  Write a program to find out the factorial of a given number, using a
#  while loop.

n = 6
f = 1
while n > 0:
    f*=n
    n-=1

print(f)

3. Write a program that counts the number of vowels, consonants and
digits in a string.

text = 'sdkzbiweufh13545cb'
v = c = d = 0

for ch in text:
    if ch.isalpha():
        if ch.lower() in set('aeiou'):
            v+=1
        else:
            c += 1
    elif ch.isdigit():
        d+=1

print(v,' ',c,' ',d)

# 4. Write a for loop to find the product of all the elements in a list

numbers = [1,2,3,4]
product = 1

for n in numbers:
    product*=n

print(product)

# 5. Write a program to count frequency of all characters in a string.

text = 'aajikkkjll'
freq = {}

for ch in text:
    freq[ch] = freq.get(ch,0)+1

print(freq)

# 6. Write a program to count frequency of all words in a string.
# Split the string into words using whitespace as the separator.

text = 'There is the dog with another dog'
word_freq = {}

for word in text.split(' '):
    word_freq[word] = word_freq.get(word,0)+1

print(word_freq)

# 7. Given a text string, create a dictionary in which keys are five
# vowels and values are the frequencies of those vowels in the string.

test = 'skjbdbvhfdzdifcejudf'
v = 'aeiou'
v_dict = {}.fromkeys(v,0)

for ch in test:
    if ch in v_dict.keys():
        v_dict[ch]+=1

print(v_dict)

# 8. Write a program to multiply two numbers by Russian Peasant Method.
# In this method, any two numbers can be multiplied using only
# multiplication by 2, division by 2 and addition.

# To multiply 2 numbers, divide the first number by 2(integer division)
# and multiply the second number by 2 repeatedly till the first number
# reduces to 1.

num_1 = 38
num_2 = 16
num_dict = {}
product = 0

while num_1 >= 1:
    num_dict[num_1] = num_2
    num_1//=2
    num_2*=2

for k,v in num_dict.items():
    print(f'key: {k}, value: {v}')
    if k%2 != 0:
        product+=v

print(product)

#shorter way

num_1 = 38
num_2 = 16
product = 0

while num_1 >= 1:
    if num_1%2 != 0:
        product+=num_2
    num_1//=2
    num_2*=2

print(product)

# 9. Write a loop to censor certain words in a text by replacing them with
# asterisks.  The words to be replaced are given in a list.  Here is an
# example -

s = '''Here’s to the crazy ones. The misfits. The rebels. The troublemakers. The ones who see things differently. They’re not fond of rules. And while some may see them as the crazy ones, we see genius. Because the people who are crazy enough to think they can change the world, are the ones who do.'''
L = ['crazy', 'mad', 'rebels', 'lunatic', 'troublemakers', 'insane']

for word in L:
    s = s.replace(word,'*'*len(word))

print(s)

# 10. Change your code written in the previous question, such that for
# all words that are to be censored, only the first letter is displayed.
# For the rest of the word, asterisks are displayed.

s = '''Here’s to the crazy ones. The misfits. The rebels. The troublemakers. The ones who see things differently. They’re not fond of rules. And while some may see them as the crazy ones, we see genius. Because the people who are crazy enough to think they can change the world, are the ones who do.'''
L = ['crazy', 'mad', 'rebels', 'lunatic', 'troublemakers', 'insane']

for word in L:
    s = s.replace(word,word[0] + '*'*(len(word)-1))

print(s)

# 11.

# age = int(input('Enter your age : '))
#       print(age)
# This code gives error if the user enters any non-numeric value.
# Rewrite the above two lines of code so that the user is forced to
# enter a numeric value for age, and that value should be less than or
# equal to 100.

age = input('Enter your age : ')

while not age.isdigit() or int(age) > 100:
    age = input('Wrong input\nEnter your age : ')

age = int(age)
print(age)


# 12. From this dictionary students, create two sets named toppers and
# champions. In the toppers set, add names of those students who have
# got more than 90 marks, and in the champions set, add names of those
# students who have more than 4 sports medals.

students = {   'id11' : { 'name': 'Amit',  'marks':97,  'sports_medals':0},
               'id12' : { 'name': 'Dev',   'marks':92,  'sports_medals':6},
               'id13' : { 'name': 'Ted',   'marks':81,  'sports_medals':2},
               'id14' : { 'name': 'Rob',   'marks':66,  'sports_medals':1},
               'id15' : { 'name': 'Sam',   'marks':56,  'sports_medals':1},
               'id16' : { 'name': 'Pam',   'marks':66,  'sports_medals':7},
               'id17' : { 'name': 'Ram',   'marks':98,  'sports_medals':9},
               'id18' : { 'name': 'Tim',   'marks':66,  'sports_medals':5},
           }

toppers = set()
champions = set()

for student in students.values():
    if student['marks'] > 90:
        toppers.add(student['name'])
    if student['sports_medals'] > 4:
        champions.add(student['name'])

print(toppers)
print(champions)

# 14. From the following set, make another set of all the names that
# start with an underscore.

names = {'_num', 'var', 'product', '_add', '_sub', 'square'}
x = set()

for name in names:
    if name.startswith('_'):
        x.add(name)
print(x)

