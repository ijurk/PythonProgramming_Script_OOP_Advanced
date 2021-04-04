# 1. Make a string s3, by concatenating the last 4 characters of string
# s1 and first 3 characters of string s2.

s3 = s1[-4:] + s2[:3]
# 2.  Make a string s1 from string s,
# in which the first 2 characters are repeated 5 times and the last character
# is repeated 3 times. For example if the string s is 'Hello World !', then
# the string s1 is 'HeHeHeHeHello World !!!'

s1 = s[:2]*5 +s[2:-1] + s[-1]*3

# 3. Write a program that inputs an email id and extracts the user name and domain
# name from the email id. For example if email is myname@somesite.com then username
# is myname and domain name is somesite.com
# (Hint : Use index() method)

email = input("Enter your email: ")
myname = email[:email.index('@')]
domain = email[email.index('@')+1:]


# 4. Write a program to extract whatever is enclosed inside asterisks in a string.
# For example if the string is 'Raj 35 *14/12/1978* Paris', the portion extracted
# is 14/12/1978
# (Hint : Use index() and rindex() methods)

s[s.index('*')+1:s.rindex('*')]

# 5.  s = '   welcome to bengaluru    '
# Write a single statement to strip all the whitespaces from left and right of
# this string s and convert it to title case.
s.strip().title()

# 6. s = 'he he that he that he that that he he that'
# Write a single statement to replace all occurrences of 'he' with 'she' and first
# 3 occurrences of 'that' with 'this'.
s.replace('he','she').replace('that','this',3)

# 7.  Make a new string s1, in which the first half of the string s is changed to
# uppercase and the second half to lower case.
# For example if string s is 'Hello World', string s1 is 'HELLO world'
s[:len(s)//2].upper() + s[len(s)//2:].lower()

# 8.  Write a single statement to check whether the string begins with 'Line ' and
# ends with 'Done'
s.startswith('Line') and s.endswith('Done')

# 9. Write a statement to create a new string named code from three strings named
# name, dob and city.
# The string code contains every alternate character from string name(only upto
# 8th character), first two characters and last 2 characters from string dob and
# first three characters from string city. The string code will be 11 characters long.
# If
# name = 'Johny Abraham'
# dob = '09/11/1987'
# city = 'London'
# code will be 'JhyA0987Lon'
# If
# name = 'Marie Claire'
# dob = '12/04/1991'
# city = 'Paris'
# code will be 'MreC1291Par'

name[:8:2]+dob[:2]+dob[-2:]+city[:3]


# 10. Write a statement to print a line that contains 80 dashes.
print('-' * 80)
# 11.  Write a statement to print 5 blank lines. ('\n' is the newline character)
print('\n' * 5)
# 12. Write a statement to find reverse of an integer n.
int(str(n)[::1])
