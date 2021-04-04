# 1.  Write a list comprehension to create a list that contains
# root of only positive numbers in this list.

L = [81, -9, 4, 16, -25, 64]

L1 = [ n ** 0.5 for n in L if n>0]
print(L1)

# 2. Use a list comprehension to construct this list

# [ '5x’, ’7x’, '9x', '11x', '13x', '15x', '17x' ]

L = [ str(n)+'x' for n in range(5,18,2)]
print(L)

# 3. Create the list L using using zip instead of len and range.

X=[1,2,3,4]
Y=[5,6,7,8]
L = [X[i]*Y[i] for i in range(len(X))]
print(L)

L1 = [ x*y for x,y in zip(X,Y)]
print(L1)

# 5.  These three lists contain names, heights and weights of 6 people.
# Heights are in cms and weights are in kilograms.
#
names = ['John', 'Joe', 'Ted', 'Sam', 'Jack', 'Jill']
heights = [160, 152, 147, 167, 177, 182]
weights = [54, 60, 90, 77, 87, 67]
# Write a list comprehension to create a list of 2 element tuples where
# first element is the name, and second element is  the bmi of the person.
# BMI(body mass index) is calculated by dividing body weight in kg by
# square of height in meters.
# For example if weight is 70 kg, height is 170 cm,
# then BMI is 70/(1.7*1.7)  = 24.2

BMI = [(name, weight/((height/100) ** 2)) for name, weight, height in zip(names, weights, heights)]

print(BMI)

# 6. This list comprehension creates a list of cubes of all odd numbers.
#   cubes = [ n**3  for n in range(5,21) if n%2!=0]
# Can you write it without the if clause.

cubes = [ n**3  for n in range(5,21,2)]

# 7. The following dictionary contains names of
# products as keys and prices as values.
prices = {'pencil': 23,'pen': 34,'eraser':12,'sharpener':13,'marker':30}

# Write a list comprehension to create a list named costly_products
# that contains names of those products whose cost is more than 20.

costly_products = [item for item, price in prices.items() if price > 20]
print(costly_products)

# 8. Given this dictionary where country name is the key and currency
# name is the value, how will you find the name of the country whose
# currency is 'Yen'


d = {   'India' :  'Rupee',
        'UK' : 'Pound',
        'France':'Euro',
        'Japan' : 'Yen',
        'Austria' : 'Euro',
        'Bangladesh': 'Taka',
        'Italy' : 'Euro'
     }

yen_country = [country for country,ccy in d.items() if ccy == 'Yen']

# Create a list of countries that have 'Euro' as the currency.

euro_country = [country for country, ccy in d.items() if ccy == 'Euro']

print(yen_country)
print(euro_country)

# 9. From this dictionary create a list of students whose
# total marks are more than 200.

students = {105416: {'name': 'John',
                     'gender': 'M',
                     'city': 'Paris',
                     'age': 21,
                     'marks': {'Maths': 89,
                               'Physics': 78,
                               'Chemistry': 91},
                     'is_sporty': True},

            144547: {'name': 'Dev',
                     'gender': 'M',
                     'city': 'London',
                     'age': 23,
                     'marks': {'Maths': 58,
                               'Physics': 57,
                               'Chemistry': 68},
                     'is_sporty': False},

            132399: {'name': 'Mary',
                     'gender': 'F',
                     'city': 'Paris',
                     'age': 22,
                     'marks': {'Maths': 99,
                               'Physics': 87,
                               'Chemistry': 88},
                     'is_sporty': True}
            }


L = [student['name'] for student in students.values() if sum(student['marks'].values()) > 200]
print(L)


# 10. Write a list comprehension that returns the sum of these two matrices M1 and M2.


M1 = [[1, 4, 8, 3],
      [2, 5, 6, 3],
      [7, 9, 5, 8]]

M2 = [[3, 5, 2, 3],
      [5, 2, 7, 9],
      [2, 8, 1, 8]]


M = [[i1+i2 for i1, i2 in zip(L1,L2)] for L1,L2 in zip(M1,M2)]

print(M)


#11.  This list L contains 6 references to the same list. How would you create
# this list L to avoid this aliasing problem.

L = [ [None]*3 ] * 6

L = [[None]*3 for i in range(6)]

# check
print(L)
L[0][0] = 1
print(L)


#12.Transpose a matrix is a new matrix in which rows become columns and vice versa.

M = [ [5,4,3,6],
      [6,3,1,2],
      [8,9,7,4]  ]

# Transpose of this matrix M is -

T = [ [5,6,8],
      [4,3,9],
      [3,1,7],
      [6,2,4] ]

#Write a list comprehension to create a list of lists that represents
# transpose of the matrix represented by M.


T = [[M[row][col] for row in range(3)] for col in range(4)]
print(T)

# or
T = [[row[i] for row in M] for i in range(4)]


# Write a list comprehension that can replace this code.

pairs = []
for n1 in range(4):
     for n2 in range(4):
          if n1!=n2:
             pairs.append((n1,n2))

pairs = [(n1, n2) for n1 in range(4) for n2 in range(4) if n1!=n2]

#14.  Write a list comprehension to create a list of lists that represents of
# size 3 X 4 with all its elements initialized to 0

M = [[0]*4 for row in range(3)]
print(M)

