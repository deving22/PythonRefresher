# Python has functions for creating, reading, updating, and deleting files.

# Open a file
myFile = open('myfile.txt', 'w')

# Get some info about file
print('Name: ', myFile.name)
print('Is closed: ', myFile.closed)
print('Opening mode: ', myFile.mode)

# Write to file
myFile.write('I love python')
myFile.write(' and Javascript')

# Close file
myFile.close()

# Append to file
myFile = open('myfile.txt', 'a')
myFile.write(' and PHP')

# Close file
myFile.close()

# Read from file
myFile = open('myfile.txt', 'r+')
text = myFile.read(100)

print(text)