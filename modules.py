# A module is basically a file containing a set of functions to include in your application. There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules

#Core modules
import datetime

#PIP module

#Custom module
from validator import validate_email

#Alternatively:
from datetime import date
from time import time

#today = datetime.date.today()
today = date.today()
timestamp = time()

print('Today is : ' + format(today))
print('Timestamp: '+format(timestamp))

email = 'deving22t.edu'

print(validate_email(email))