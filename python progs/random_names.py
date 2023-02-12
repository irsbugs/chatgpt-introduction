"""
1. Create a list of first names
2. Create a list of last names
3. Combine them randomly into a list of 100 full names
"""

import random

#1
first_names = ['John', 'Dave', 'Steve', 'Michael', 'Alex', 'Amy', 'Mary', 'Mandy', 'Jane', 'Claire']

#2
last_names = ['Smith', 'Wilson', 'Johnson', 'Williams', 'Black', 'White', 'Davis', 'Jones', 'Thompson', 'Taylor']

#3
full_names = []

for i in range(100):
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    full_name = first_name + ' ' + last_name
    full_names.append(full_name)

print(full_names)


