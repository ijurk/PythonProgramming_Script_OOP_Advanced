# 1.Write a program that enters a string and prints
# whether it is a palindrome.Ignore case and spaces, so
# that all expressions like 'Nurses run'   'Madam I am Adam'
# are considered palindromes.

s = input('Enter a string: ')

if s.replace(' ','').lower()[::-1] == s.replace(' ','').lower():
    print('It is a palindrome')
else:
    print('It is not a palindrome')



# 2. Write a program that inputs the length of three sides
# of a triangle, and prints the perimeter of the triangle.It
# should also print whether the triangle is equilateral, isosceles or scalene.
# If there is no triangle possible
# with the given sides, then instead of printing the
# above things it should print 'No triangle possible with these sides'
# (In an equilateral triangle, all sides are equal.
# In an isosceles triangle, any two sides are equal.
# In a scalene triangle, all three sides are unequal.
# For a triangle to be possible with given sides, sum of any two sides
# should be greater than the third side.)
# Here is a sample run of the program.

side_first = int(input('Enter first side: '))
side_second = int(input('Enter second side: '))
side_third = int(input('Enter third side: '))

if side_first + side_second > side_third \
    and side_second + side_third > side_first \
    and side_first + side_third > side_second:
    print('Perimeter of the triangle is ', side_first + side_second + side_third)
    if side_first == side_second == side_third:
        print('Equilateral Triangle')
    elif side_first != side_second != side_third:
        print('Scalen Triangle')
    else:
        print('Isosceles Triangle')
else:
    print('No triangle possible with these sides')

# 3. Write a program that prompts the user to input his / her
# weight in kg and height in cms, and calculates the body mass index(BMI).BMI is calculated
# by dividing body weight in kg by square of height in meters.
# For example if weight is 70 kg, height is 170 cm,
# then BMI is 70 / (1.7 * 1.7) = 24.2
# Display the BMI and appropriate message according to the BMI.
# Underweight < 18.5
# Normal weight 18.5 to 24.9
# Overweight 25 to 29.9
# Obese >= 30

w = float(input('Enter your weight in kg: '))
h = float(input('Enter your height in cm: '))
h /= 100

bmi = w / (h * h)

print('Your BMI is ', bmi)

if bmi < 18.5:
    print('Underweight')
elif 18.5<=bmi<24.9:
    print('Normal Weight')
elif 24.9<=bmi<29.9:
    print('Overweight')
else:
    print('Obese')


# 5. Write a program to check whether a given sentence is a pangram or not.
# A pangram is a sentence that uses every letter of the alphabet at least once.
# Some examples of pangrams are -
# The quick brown fox jumps over the lazy dog.
# Pack my box with five dozen liquor jugs.
# Waltz, nymph, for quick jigs vex Bud.

s = 'The quick brown fox jumps over the lazy dog.'
abc_set = set('abcdefghijklmnoprstuvzxywq')
if abc_set - set(s.replace(' ','').lower()) == set():
    print('Pangram')
else:
    print('Not Pangram')


# 7. Write a program to find whether a year is leap year or not. A year is a
# leap year if it is divisible by 4, but not every year that is a multiple of 4 is a
# leap year. If a year is divisible by 100, then it is not a leap year unless it divisible
# by 400.
# Years 1980, 2040 are leap years as they are divisible by 4.
#
# Years 2000,  2400 , 1800, 1900, 2500 are divisible by 4, but since they are divisible
# by 100 we cannot say that all of them are leap years. Only those which are divisible
# by 400 will be leap years.
#
# Years 2000 and 2400 are leap years as they are divisible by 400, while 1800, 1900,
# 2500 are not leap years.

y = 1980

if y%400==0 or y%4==0 and y%100!=0:
    print('Leap')
else:
    print('Not leap')

# 9.  Rewrite this piece of code using ternary operator
bill_amount = 1500

if bill_amount>2000:
   free_home_delivery = 'Available'
else:
   free_home_delivery = 'Not Available'

free_home_delivery = 'Available' if bill_amount>2000 else 'Not Available'
print(free_home_delivery)

# 10.  Write a more efficient version of this code

if x < y:
  print('x is less than y')
elif x > y:
  print('x is greater than y ')
else:
   print ('x is equal to y')


# 11. A list named L contains some integer values, write a line of
# code to find average of the list elements using ternary operator.

L = [2,5,9,6]

avg = sum(L)/len(L) if len(L) != 0 else None

# 12. We have seen that we can use the get method to avoid error while accessing a
# non-existent key.

D = {'a':23, 'd':34, 'j':56}
val = D['b']   # Raises Error
val = D.get('b',0)  # Returns 0
val
# Instead of using get(), write a line of code that uses ternary operator to return
# a default value when the key is not present in the dictionary.
key = 'a'

val = D[key] if key in D.keys() else 0
val

# 1.  NOT (a AND b) = (NOT a) OR (NOT b)
#
# 2.  NOT (a OR b) = (NOT a) AND (NOT b)

if not (marks > 0 and marks <= 100):
       print('Out of range')

if marks <= 0 or marks > 100:
    print('Out of range')

if not (age<18 or weight >60 ):
      print('Allowed to play the game')

if age>=18 and weight<=60:
      print('Allowed to play the game')
