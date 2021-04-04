# formating string

name = 'Iva'
age = 35
wt = 43.5789

s = 'My name is {}, I am {} years old and my weight is {} kg'.format(name, age, wt)
print(s)

s = f'My name is {name}, I am {age} years old and my weight is {wt} kg'
print(s)

#allignment
s = f'My name is {name:8}, I am {age:<6} years old and my weight is {wt} kg'
print(s)

s = f'My name is {name:^8}, I am {age:^6} years old and my weight is {wt} kg'
print(s)

s = f'My name is {name}, I am {age:f} years old and my weight is {wt} kg'
print(s)

s = f'My name is {name}, I am {age:.3f} years old and my weight is {wt:.3f} kg'
print(s)

s = f'My name is {name}, I am {age:<10.3f} years old and my weight is {wt:.1f} kg'
print(s)

s = f'My name is {name}, I am {age:*^10.3f} years old and my weight is {wt:.1f} kg'
print(s)

s = fr'\name: {name.upper()}' #r escapes the escape character in this case \n
print(s)

money = 15269446315
s = f'I have: {money:,}'
print(s)