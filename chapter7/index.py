import re

names = ['onaolapo Badmus','omolori','chidera','oluseyi','david uranamus']

regex = '^\w+ \w+$'

for name in names:
    result = re.search(regex,name)
    if result:
        print(name)

#Practice Project
# For practice, write programs to do the following tasks.
# Strong Password Detection
# Write a function that uses regular expressions to make sure the password
# string it is passed is strong. A strong password is defined as one that is at
# least eight characters long, contains both uppercase and lowercase charac-
# ters, and has at least one digit. You may need to test the string against mul-tiple regex patterns to validate its strength.