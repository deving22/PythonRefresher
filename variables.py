# A variable is a container for a value, which can be of various types

'''
This is a 
multiline comment
or docstring (used to define a functions purpose)
can be single or double quotes
'''

"""
VARIABLE RULES:
  - Variable names are case sensitive (name and NAME are different variables)
  - Must start with a letter or an underscore
  - Can have numbers but can not start with one
"""

#Variable declaration (no typecasting needed)
#x = 1 # int
#y = 2.5 #float
#name = 'John' #str, single or double quotes
#is_cool = True #bool

#Multiple assignment
x,y,name,is_cool = (1,2.5,'John',True)

#In python3, need to use parantheses for print, not just quotes as in Python2
print(is_cool)

#Basic math
a = x+y
print('The value of a is:',a)

#Casting
x = str(x)
y = int(y)
z = float(y)

print(type(z), z)

