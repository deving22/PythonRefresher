# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
 
# Create tuple
fruits = ('Apples','Oranges','Grapes')

# Constructor
fruits2 = tuple(('Apples','Oranges','Grapes'))

print(fruits, fruits2)
print(fruits[1])
# Need trailing comma to ensure it is a tuple
fruits3 = ('Apples',)

print(fruits3,type(fruits3))

# Can't change value
#fruits[0] = 'Pears'

# Delete tuple
del fruits2

#print(fruits2)

# Get length
print(len(fruits))

# A Set is a collection which is unordered and unindexed. No duplicate members.

# Create set
fruits_set = {'Apples', 'Oranges', 'Mangoes'}

# Check if in set
print('Apples' in fruits_set)

# Add to set
fruits_set.add('Grapes')

# Remove from set
fruits_set.remove('Grapes')

# Clear set
#fruits_set.clear()

# Delete set
#del fruits_set

print(fruits_set)