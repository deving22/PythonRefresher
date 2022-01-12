# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# Read more about dictionaries at https://docs.python.org/3/tutorial/datastructures.html#dictionaries

# Create dictionary
person = {
    'first_name': 'Devin',
    'last_name' : 'Grande',
    'age': 29
}

# Constructor to create
#person2 = dict(first_name='Devin',last_name='Grande')

print(person, type(person))

#print(person2, type(person2))

# Get value
print(person['first_name'])
print(person.get('last_name'))

# Add key value pair
person['phone'] ='401-864-7996'

# Get dict keys
print(person.keys())

# Get dict items
print(person.items())

print(person)

# Copy dictionary
person2 = person.copy()
person2['city'] = 'Boston'

print(person2)

# Remove item from dict
del(person['age'])
person.pop('phone')

# Clear
person.clear()

# Get length
print(len(person2))

print(person)

# List of dictionaries
people = [
    {
        'name': 'Martha',
        'age': 30
    },
    {
        'name': 'Kevin',
        'age' : 25
    }
]

print(people)
print(people[1]['name'])
