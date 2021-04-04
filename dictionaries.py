# 1. On the interactive prompt, create an empty dictionary
# named currency and then add these key value pairs to it.
#  'India' : 'Rupee'
# 'UK' : 'Pound'
# 'Japan' : 'Yen'
# 'Austria' : 'Euro'
# 'Bangladesh' : 'Taka'
currency = dict()

currency = {'India': 'Rupee','UK': 'Pound','Japan': 'Yen','Austria': 'Euro','Bangladesh': 'Taka'
}


# 2. From the above dictionary, delete entry related to key 'UK'
del currency['UK']
print(currency)
# 3. Delete the entry related to key 'Japan' and store the return value in another
# variable named c.
c = currency.pop('Japan')

# 4. Delete a random key-value pair from the dictionary.
currency.popitem()
currency
# 5. Add a new entry in the dictionary with key 'Switzerland' and value 'Swiss Franc'.
currency['Switzerland'] = 'Swiss Franc'
currency
# 6. Change value for key 'India' from 'Rupee' to 'Indian Rupee'
currency['India'] = 'Indian Rupee'
currency
# 7. Using appropriate methods, print all keys, all values and all key-value
# pairs of the dictionary.
currency.keys()
currency.values()
currency.items()

# 8. Given the following dictionary -
fruits_prices = { 'apple': 100, 'banana':75, 'mango':80 }
# Using appropriate method, access the value associated with keys
# 'apple' and 'grapes'. If the key is not present in the dictionary
# it should be added with value 0.
fruits_prices.setdefault('apple',0)
fruits_prices.setdefault('grapes',0)
fruits_prices

# 9. Create a dictionary named login from this list named names.

names = ['John', 'Sam', 'Marie', 'Anne']

# The elements of this list should be the keys of the dictionary and
# value associated with all keys should be None.

login = dict.fromkeys(names, None)

# 10. Given these 2 lists-

designation = ['programmer', 'manager', 'accountant']
salary = [4000, 5000, 3000]
# Create the following dictionary from the above two lists.
# {'programmer':4000, 'manager':5000, 'accountant':3000}

D = dict(zip(designation, salary))
help('zip')

# 11. Given these 3 lists -

python_books = [ 'Learn Python', 'Programming in Python', 'Python in depth']
cplusplus_books = ['C++ in depth', 'C++ Programming']
java_books = ['Java Programming', 'Learn Java']

# Write a dictionary with 'python', 'c++' and 'java' as keys and these
# lists as values. So when you write books['java'] you get the list of
# java books and similarly for other keys.

books = {'python': python_books, 'c++': cplusplus_books, 'java': java_books}
books['java']

# 12.  Given these 2 dictionaries -
book_prices = {'Learn ABC':150, 'Learn 123': 200, 'Rhymes':300, 'Cursive Writing':250}
new_stock = {'Stories':350, 'Poems':290, 'Spellings':200}

# Add all the key-value pairs of new_stock to book_prices.

book_prices.update(new_stock)
book_prices

# 13. Create this dictionary using range() function and fromkeys() method.

# {1000: None, 2000: None, 3000: None, 4000: None, 5000: None, 6000: None,
# 7000: None, 8000: None, 9000: None}

D = dict.fromkeys(list(range(1000,10000,1000)), None)
D

# 14. In the following nested dictionary, how will you access the last name of
# the student.

student = { 'name': {  'first': 'John',
                       'last': 'Mark'
                      },
             'marks':98,
             'age':20
           }

student['name']['last']

# 15. From this dictionary d, create a list that contains all the keys in sorted order.

d = { 2:300, 8:900, 7:800, 1:100}
sorted(d.keys())

# 16. In this dictionary, key is an integer which represents the student id and
# value is list type which contains marks of the students in     three subjects.

marks =  {  2234 : [99,23,56],
            2135 : [67,56,68],
            2199 : [78,89,66]
          }
#How will you get total marks of student with student id 2135.
sum(marks[2135])

# 17. We have seen how to use a list of lists to represent a matrix. We used two
# indices to access an element of the matrix( for    example matrix[1][4]).
# If a matrix is sparse, then we can save space by using a dictionary to
# implement it. A matrix is sparse, if it has many zero values in it.
# For example this is a sparse matrix.
# Create a dictionary named matrix which stores only non-zero values of
# this matrix. Use a tuple of row and column numbers as the key.

matrix = {(0,5):4, (1,3):8, (3,4):6, (5,2):3}

# 18. In the implementation of matrix that we did in the last question,
# if we try to access any element of matrix that is zero, then we
# will  get an error. For example if we write matrix[1,2] or matrix[2,0] we
# will get error. This is because there is no key in the dictionary
# corresponding to zero elements of matrix. Tuples (1,2) or (2,0) are not
# present as keys in the dictionary.  Use the get method to solve this problem.

matrix.get((0,5),0)
matrix.get((1,2),0)
