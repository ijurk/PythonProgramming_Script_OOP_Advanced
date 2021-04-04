# Given this list -
numbers = [12,32,55,67,3,55,68,22,55,89,55,1,19,32]

# 1. Write a method call to find the number of occurrences of 55 in this list.
numbers.count(55)

# 2. Write a method call to find the index of first occurrence of 55 in this list.
numbers.index(55)

# 3. Write a method call to find the index of last occurrence of 55 in this
# list.

len(numbers) - list(reversed(numbers)).index(55) - 1

# 4. Write a method call to find the index of first occurrence of 55,
# in a portion of this list starting from index 4 to index 9.

numbers.index(55,4,9)

# 5. Write a method call to find the index of smallest element of the list.

numbers.index(min(numbers))

# 6. Write a statement to replace the largest element of the list with 1000.
print(numbers)
numbers[numbers.index(max(numbers))] = 1000
print(numbers)

# 7. Write a statement to make a new list that contains the three largest
# elements of the list.
sorted(numbers)[-3:]

# 8. Write a function call to find the sum of five smallest elements of the list.
sum(sorted(numbers)[:5])

# 9. Write a statement to find the minimum value of the first half of the list.
min(numbers[:len(numbers)//2])

# 10. Find the average of all the elements of the list.
sum(numbers) / len(numbers)

# 11. Write a statement to create a list of size 20 with all
# elements initialized to None.
L = [None] * 20

# 12. Create the following list using the range function.
# [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100]

list(range(1000,0,-100))

# 13. Create a list of all multiples of 7 greater than 50 and less than 150,
# using the range function.
list(range(56,150,7))

# 14.
# Create a string using the join method in which all these strings are joined
# by a comma
listD = ['Pluto', 'Goofy', 'Donald Duck', 'Alice']
','.join(listD)

#  15.  Write an expression that will give you the reverse of the string at
#  index 2.
fruits = ['apple', 'banana', 'grapes']
fruits[2][::-1]

#  16. What is the difference between these 2 statements
#        ls.append(2) # changes in-place
#        ls = ls + [2] # creates new object

# 17.  What will be the output -
x = [1,2,3]
y = [x]*4
print(y)
z = x*4
print(z)


# 18.  What will be the output -

L = [1,2,3]
X = ['a', L]
X[1][0] = 100
print(L)

# What can you do to avoid the side effect that is seen in this code.
##create a copy

X = ['a',L[:]]
X = ['a', L.copy()]
X[1][0] = 100