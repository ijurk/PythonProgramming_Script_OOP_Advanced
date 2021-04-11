# 1. Write a program to display only those lines from a file that
# don’t start with #.

with open('data.txt','r') as f:
    for line in f:
        if not line.startswith('#'):
            print(line, end="")


# 2. Write a program to display only the first 5 lines of a file.

with open('data.txt','r') as f:
    for i in range(5):
        print(f.readline(),end="")


# 3. Write a program to display only the last 5 lines of a file.

with open('data.txt','r') as f:
    for line in f.readlines()[-5::]:
        print(line,end="")


# 4. Write a program to copy the contents of one file to another
# file such that each space in first file is replaced with a dash.

with open('data.txt','r') as f1:
    with open('new.txt','w') as f2:
        f2.write(f1.read().replace(' ','-'))


# 5. Write a function copy_file that takes source and destination +
# file names, and copies the file by copying 100 characters at a time.

def copy_file(source, destination):
    f1 = open(source,'r')
    f2 = open(destination, 'w')

    while True:
        s = f1.read(100)
        if s == '':
            break
        f2.write(s)
    f1.close()
    f2.close()

copy_file('data.txt','new_2.txt')

# 6. Write a program to compare two files line by line and report
# the line where they differ.

with open('data.txt','r') as f1:
    with open('new_2.txt','r') as f2:
        count = 1
        while True:
            line1 = f1.readline()
            line2 = f2.readline()
            if line1 != line2:
                print('Files differ at line', count)
                break
            if line1 == '':
                print('Files are same')
                break
            count+=1

# 7. In the exercise on loops, we had written a program to
# count frequency of each word in a string. Now write a
# program to count frequency of each word in a file.
import pprint

f = open('data.txt','r')
count = {}
for word in f.read().split():
    count[word] = count.get(word,0) + 1
pprint.pprint(count)

# 8. Write a program to replace each occurrence of a given word
# with another word.

with open('data.txt','r+') as f:
    s = f.read().replace('test','T')
    f.seek(0)
    f.write(s)
    f.truncate()


# 9. with open('data.txt', 'r') as f:
# lines =[line.rstrip() for line in f ]
# print(lines)
# What problem will be there if you use the expression
# line[:-1] instead of line.rstrip().
#ANSWER: the last line might not have /n character and we'll still
# strip the last character

# 10. Write a program to add an empty line after
# each line in the file.

with open('data.txt','r+') as f:
    lines = [line+'\n' for line in f]
    f.seek(0)
    f.writelines(lines)

# 11. Write a program to search for a string in all the files of
# a directory.

import os

search_string = 'test'

for name in os.listdir('.'):
    if os.path.isfile(name):
        with open(name,'r') as f:
            for line in f:
                i = line.find(search_string)
                if i >=0:
                    print('Found line:\n',line, '\n in file', name)
        print()




# 12. Write a program to delete lines that start with #.
import os

with open('data.txt','r') as f1:
    with open('data_new.txt','w') as f2:
        for line in f1:
            if not line.startswith('#'):
                f2.write(line)

os.remove('data.txt')
os.rename('data_new.txt','data.txt')


# 13. Write a for loop that prints the line number
# before each line of the file.

for number,line in enumerate(open('data.txt','r'),1):
    print(number,line,end='')
