numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# Write method calls to perform the following operations on this list.

# 1. Add 100 at the end of the list

numbers.append(100)
numbers

# 2. Add 200 in the beginning of the list

numbers.insert(0,200)
numbers


# 3. Add 150 at index 3

numbers.insert(3,150)
numbers

# 4. Add 12, 13, 14, 15 at the end of the list in one step.

numbers.extend([12, 13, 14, 15])
numbers

# 5. Delete element 5 from the list.
numbers.pop(4)
numbers

# 6. Delete the last element from the list

numbers.pop()
numbers

# 7. Delete the element at index 5
numbers.pop(5)
numbers


# 8. Delete the first element from the list
numbers.pop(0)
numbers


# 9. Delete all the elements of the list

numbers.clear()
numbers

# 10.  Using the del keyword delete the element at index 5.

listA = [20, 30, 40, 50, 60, 70]
del listA[5]
listA


# 11.  Using the del keyword delete the last 3 elements.
listA = [20, 30, 40, 50, 60, 70]
del listA[-3:]
listA

# 12. What is the difference# between listA.clear() and del listA.
# listA.clear() makes the list empty, while del listA will undefine the name listA. After del
# listA, if you reference the name listA, NameError will be raised.

# 13.  What is the value of this expression sorted(numbers)[2:4]
numbers = [98, 11, 22, 9, 6, 32, 5]
sorted(numbers)[2:4]

# 14. Make a new list that contains the 5 largest numbers from this list.
# (You should get this list[22, 32, 35, 39, 98])
numbers = [39, 4, 1, 98, 11, 35, 7, 22, 9, 6, 32, 5, 10]
sorted(numbers)[-5:]

# 15. Make a new list that contains the 5 smallest numbers from this list.
# (You should get this list[1, 4, 5, 6, 7])
numbers = [39, 4, 1, 98, 11, 35, 7, 22, 9, 6, 32, 5, 10]
sorted(numbers)[:5]


# 16. Sort this list in reverse order.
numbers = [3, 2, 1, 5, 7, 9]
numbers.sort(reverse=True)
print(numbers)

# 17. Sort this list of strings based on their length.
fruits = ['banana', 'fig', 'Mango', 'pomegranate', 'Apple']
sorted(fruits, key=len)

# 18. Perform case insensitive sort on this list of strings.
fruits = ['banana', 'fig', 'Mango', 'pomegranate', 'Apple']
sorted(fruits, key=str.lower)

# 19.
listA = [4, 3, 2, 6]
listA = listA.sort(reverse=True)
print(listA)

listB = [9, 4, 3]
listB = listB.append(5)
print(listB)

# What will the above code print. - None because both return None

# 20. Find the second largest and third smallest elements from this list.

numbers = [4, 3, 5, 6, 1, 7, 2, 9]

numbers.sort()
print(numbers[-2])
print(numbers[2])

# 21.
numbers = [1, 2, 3]
numbers.extend([4, 5, 6])
print(len(numbers))

numbers.append([7, 8, 9])
print(len(numbers))

