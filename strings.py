# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name = 'Devin'
age = 29

# Concatenate 
print('Hello, my name is ' + name + ' and I am ' + str(age))

# String Formatting

# Positional arguments
print('My name is {name} and I am {age}'.format(name=name, age=age))

# F-Strings (python 3.6 and later)
#print(f'Hello, my name is {name} and I am {age})

# String Methods

s = 'hello world'

#Capitalize string
print(s.capitalize())

#Get length
print(len(s))

#Replace
print(s.replace('world','everyone'))

