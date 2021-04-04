# 1. Write a statement to change the second last element of this list to 200.
listA = [1, 2, 3, 4, 5, 6, 7, 8]
listA[-2] = 200
# 2.
# In this list, replace the elements 3,4,5,6 with elements 30,40,50,60,70,80
listA = [1, 2, 3, 4, 5, 6, 7, 8]
listA[2:6] = [30,40,50,60,70,80]
print(listA)

# 3. Write a statement to replace all the elements from index 3 onwards with
# the characters of the string 'pqr'.
# Resulting list should be [1, 2, 3, 'p', 'q', 'r']
listA = [1, 2, 3, 4, 5, 6, 7, 8]

listA[3:] = 'pqr'
print(listA)
# 4. listA = [1, 2, 3, 4, 5, 6, 7, 8]
# Write a statement to insert new elements 10,20,30,40,50 starting at index 5.
# Resulting list should be [1, 2, 3, 4, 5, 10, 20, 30, 40, 50, 6, 7, 8]

listA = [1, 2, 3, 4, 5, 6, 7, 8]
listA[5:5] = [10,20,30,40,50]
print(listA)

# 5. listA = [1, 2, 3, 4, 5, 6, 7, 8]
# Write a statement to delete all elements from index 2 to index 5.
# Resulting list should be  [1, 2, 7, 8]
listA = [1, 2, 3, 4, 5, 6, 7, 8]
listA[2:6] = []
print(listA)

# 6.  listA = [1, 2, 3, 4, 5, 6, 7, 8]
# Write a statement to make a new list named cpy that is a copy of this list listA.

listA = [1, 2, 3, 4, 5, 6, 7, 8]
cpy = listA[:]
print(cpy)

# 7.  listA = [1, 2, 3, 4, 5, 6, 7, 8]
# Write a statement to make a new list named rev that is reverse of this list listA.
listA = [1, 2, 3, 4, 5, 6, 7, 8]
rev = listA[::-1]
print(rev)
# 8. What will be the output

listA = [4,5,6,7,8,9,10]
listA[2:5] = []
print(listA)
listA[2]=[]
print(listA)