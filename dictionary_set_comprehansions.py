# 1. Write a dictionary comprehension to create a dictionary which
# has integers from 1 to 20 as the keys, and values are squares of the keys.


d = {i:i*i for i in range(1,21)}
print(d)

# 2.Write a dictionary comprehension to create the following dictionary from the list L.
L = [2,4,6,7,5]
# {2: [1, 2],
#  4: [1, 2, 3, 4],
#  6: [1, 2, 3, 4, 5, 6],
#  7: [1, 2, 3, 4, 5, 6, 7],
#  5: [1, 2, 3, 4, 5]
#  }

d = {item: [i for i in range(1,item+1)] for item in L}
print(d)

# 3.

names  = ['Ted', 'Sam', 'Jim', 'Rob', 'Anu']
maths = [98,67,54,88,95]
physics = [88,64,78,99,78]
chemistry = [78,67,45,79,87]
# These 4 lists contain the names and marks of students in 3 subjects.
# Write a dictionary comprehension to create the following dictionary
# from the above 4 lists.
# { 'Ted': [98, 88, 78],
#   'Sam': [67, 64, 67],
#   'Jim': [54, 78, 45],
#   'Rob': [88, 99, 79],
#   'Anu': [95, 78, 87]  }

d = {name: [math,physic, chem] for name, math, physic, chem in zip(names, maths, physics, chemistry)}
print(d)

# 4.  Change the dictionary comprehension that you wrote in previous question
# to create this nested dictionary.

{ 'Ted': {'Maths': 98, 'Physics': 88, 'Chemistry': 78},
  'Sam': {'Maths': 67, 'Physics': 64, 'Chemistry': 67},
  'Jim': {'Maths': 54, 'Physics': 78, 'Chemistry': 45},
  'Rob': {'Maths': 88, 'Physics': 99, 'Chemistry': 79},
  'Anu': {'Maths': 95, 'Physics': 78, 'Chemistry': 87}  }


d = {name: {'Maths':math,'Pysics':physic, 'Chemistry':chem} for name, math, physic, chem in zip(names, maths, physics, chemistry)}
print(d)

# 5.  From this dictionary create another dictionary that contains only those
# key value pairs where email id is on the website xyz.com

d  =   {'raj@xyz.com' : {'course':'Algorithms', 'city':'London'},
        'dev@abc.com' : {'course':'Painting', 'city':'Delhi'},
        'sam@pqr.com' : {'course':'Design Patterns', 'city':'London'},
        'jim@xyz.com' : {'course':'Networking', 'city':'Delhi'},
        'pam@abc.com' : {'course':'Algorithms', 'city':'Delhi'},
        'ray@abc.com' : {'course':'Painting', 'city':'London'},
        'anu@xyz.com' : {'course':'Algorithms', 'city':'London'},
        'bob@pqr.com' : {'course':'Data Structures', 'city':'Tokyo'},
        'ted@abc.com' : {'course':'Algorithms', 'city':'London'},
        'zen@abc.com' : {'course':'Painting', 'city':'London'} }


import pprint
new_d = {key:value for key,value in d.items() if key[-7:] == 'xyz.com'}
# or
new_d = {email:val for email,val in d.items() if email.endswith('xyz.com')}
pprint.pprint(new_d)

# 6. From the dictionary d given in previous question, create a new dictionary
# that has all the key value pairs of dictionary d, with all occurrences of pqr.com
# changed to pqr.org.

new_d = {email.replace('com','org') if email.endswith('pqr.com') else email:val for email,val in d.items()}
pprint.pprint(new_d)

# 7. A training on design patterns has to be delivered, all the enrolments are
# done. The following dictionary contains the registration ids as the key and
# another dictionary as the value.

trainees = { '12AB' : { 'name': 'Ash', 'experince':12, 'language': 'C++' },
             '34CD' : {'name': 'Dev', 'experince':5, 'language': 'Python' },
             '55AB' : { 'name': 'Raj', 'experince':10, 'language': 'C++' },
             '67CD' : {'name': 'John', 'experince':3, 'language': 'Java' },
             '23ED' : {'name': 'Drek', 'experince':7, 'language': 'Python' },
             '35ED' : {'name': 'Amit', 'experince':4, 'language': 'Python' }
            }


# The trainer wants to provide hand-outs of sample programs in all the languages
# that trainees have chosen. From this dictionary, find out a set of all the
# languages in which the trainer has to make programs.

language = {rec['language']for rec in trainees.values()}
print(language)

# 8. This is a dictionary of all employees where key is the id of an employee
# and value is another dictionary that contains name and phone number of the
# employee. In the phone number, the first three characters represent the code
# of a city. Make a list of all those employees who have city code 080.


emp =  {  'id01' :  { 'name' : 'Dev', 'phone' : '08056771173'},
          'id02' :{ 'name' : 'Raj', 'phone' : '01176791193'},
          'id03' :  { 'name' : 'Ami', 'phone' : '08056774473'},
          'id04' :{ 'name' : 'Anita', 'phone' : '011767976193'},
          'id05' :  { 'name' : 'Sam', 'phone' : '08056771173'},
          'id06' :{ 'name' : 'Reena', 'phone' : '02276791193'},
          'id07' :  { 'name' : 'Akul', 'phone' : '08056774473'},
          'id08' :{ 'name' : 'Amar', 'phone' : '011767976193'}}

L = [employee['name'] for employee in emp.values() if employee['phone'].startswith('080')]
print(L)


# 9. Find out the number of unique cities, whose code appears in the dictionary
# emp of previous question.

num_city = len({employee['phone'][:3] for employee in emp.values()})
print(num_city)

# 10.  The following dictionary maps city codes to city names.
# Create a set that contains the names of all cities whose code appears
# in the dictionary emp of question 8.
cities = { '080':'Bengaluru', '044':'Chennai', '040':'Hyderabad', '011':'Delhi', '022':'Mumbai' }


city_names = {cities[employee['phone'][:3]] for employee in emp.values()}
print(city_names)


# 11. From the dictionary emp(of Q8) and dictionary cities(10), create a
# list of employees who are in 'Delhi'.


employees_Delhi = [employee['name'] for employee in emp.values() if employee['phone'][:3] == {city:code for code,city in cities.items()}['Delhi']]
print(employees_Delhi)

# or

[emp['name'] for emp in emp.values() if cities[ emp['phone'][:3]] == 'Delhi']

