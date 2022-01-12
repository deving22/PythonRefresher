# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

# Create class
class User:
    # Constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
    
    # Method
    def greeting(self):
        return 'My name is ' + self.name + ' and I am '+ format(self.age)

    def has_birthday(self):
        self.age += 1

# Extend user class
class Customer(User):
    # Constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0

    #Method
    def setBalance(self, balance):
        self.balance = balance

    # Method
    def greeting(self):
        return 'My name is ' + self.name + ' and I am '+ format(self.age) + ' and my balance is ' + format(self.balance)

# Instantiate object
devin = User('Devin', 'test@email.com', 29)

devin.has_birthday()
print(devin.greeting())

devin2 = Customer('Devin', 'test@email.com', 29)

devin2.setBalance(25)
print(devin2.balance)
print(devin2.greeting())