# If/ Else conditions are used to decide to do something based on something being true or false
x = 55
y = 50

# Comparison Operators (==, !=, >, <, >=, <=) - Used to compare values

#Simple if
if x > y:
    print('{x} is greater than {y}'.format(x = x, y=y))

#If/else
if x > y:
    print('{x} is greater than {y}'.format(x = x, y=y))
else:
    print('{y} is greater than {x}'.format(x = x, y=y))

#Elif
if x > y:
    print('{x} is greater than {y}'.format(x = x, y=y))
elif x == y:
    print('{x} is equal to {y}'.format(x = x, y=y))
else:
    print('{y} is greater than {x}'.format(x = x, y=y))

#Nested if
if x > 2:
    if x <= 10:
        print('{x} is greater than 2 and less than or equal to 10'.format(x = x))

# Logical operators (and, or, not) - Used to combine conditional statements
# And
if x > 2 and x <= 10:
    print('{x} is greater than 2 and less than or equal to 10'.format(x = x))

# Or
if x > 2 or x <= 10:
    print('{x} is greater than 2 or less than or equal to 10'.format(x = x))

# Not
if not(x == y):
    print('{x} is not equal to {y}'.format(x=x,y=y))


# Membership Operators (in, not in) - Membership operators are used to test if a sequence is presented in an object

numbers = [1,2,3,4,5]

# in
if x in numbers:
    print(x in numbers)

# not in
if x not in numbers:
    print(x not in numbers)

# Identity Operators (is, is not) - Compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:

# is
if x is y:
    print(x is y)

# is not
if x is not y:
    print(x is not y)