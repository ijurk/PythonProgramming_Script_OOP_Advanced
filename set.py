# 1. Input two strings s1 and s2 and then create a list that contains
# all the common characters of the two input strings.

s1 = input('Enter first string: ')
s2 = input('Enter second string: ')

list(set(s1) & set(s2))

# 2. From the following two strings, find all words common in both the strings.
# Extract words from the string by splitting on spaces.
string1 = "Life has no remote, get up and change it yourself"
string2 = "Life has no ctrl+Z"

set(string1.split(' ')) & set(string2.split(' '))


# 3. How will you count the number of unique items in a list.

len(set(list1))

# 4. Create a new list by filtering out all the duplicates
# from the following list by using the set function.
L = [12,44,46,32,12,43,55,86,43]
list(set(L))
# Will the order of the original list be preserved if you
# use this method to filter out duplicates? No

# 5. Enter a string and create 2 sets v and c, where v is a
# set of vowels present in the string and c is a set of consonants
# present in the string.

string3 = 'eprzhjvfbslkdio'
vowels = set('aeiou')

v = set(string3) & vowels
v = set(string3).intersection(vowels)
c = set(string3).difference(v)

# 6. How can you perform order neutral equality tests in lists
# and strings using sets.
L1 = [1,2,3,4]
L2 = [2,3,1,4]
set(L1) == set(L2)

# These two lists L1 and L2 have same elements, only the order is different,
# so when you perform order neutral equality test on these 2 lists,
# they are considered equal. This test just checks whether both of them
# contain same elements.

# 7. How will you find out all the elements of list L1 that are not in L2.
L1 = [1,2,3,7]
L2 = [2,3,4,5]

set(L1).difference(set(L2))
set(L1) - set(L2)

# 8. How will you find all the common characters in three strings s1, s2 and s3
set(s1) & set(s2) & set(s3)

# You are given these 2 sets toppers and champions, where toppers is a
# set of roll numbers of academic toppers of the school and champions
# is a set of roll numbers of sports champions of the school.

toppers = { 'id11', 'id23', 'id34', 'id45', 'id77', 'id12', 'id89', 'id56', 'id55', 'id70' }
champions = { 'id19', 'id23', 'id78', 'id99', 'id79', 'id13', 'id56', 'id45', 'id80' }
# Answer questions from 9 to 14 based on these two sets.
# 9. From the set of toppers, remove student with rollnumber id12
dir(toppers)
toppers
toppers.remove('id12')
# 10. From the set of champions, add two students with roll numbers
# id45 and id19
dir(champions)
champions.add('id45')
champions.add('id19')

# 11. Find a set of all the toppers who are not champions
toppers.difference(champions)
toppers - champions
# 12. Find a set of all the champions who are not toppers
champions - toppers
# 13. Find a set of all students who are champions as well as toppers
champions & toppers
# 14. Find a set of all students who are either champions or toppers.
champions | toppers

