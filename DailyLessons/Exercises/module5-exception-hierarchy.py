# sys exit
import sys

user_name = input('What is your name? ')
if user_name == '':
    print('Empty name? I cannot work with that. I am closing the program. Bye!')
    sys.exit()
print('Hello,', user_name)
print('Let us get started...')

# Stopping a program manually if it is in an infinite loop will produce
# a KeyBoardInterrupt exception

# Index and key errors
# Code below produces IndexError since index does not exist
# languages = ['Spanish', 'English', 'German', 'Italian']
# print(languages[8])

# Code below produces KeyError, key does not exist
# ages = {'Jim': 30, 'Pam': 28, 'Kevin': 33}
# ages['Michael']

# Code below will produce a TypeError since int is not specified for input
# age = input('What is your age? ')
# print('In 10 years, your age will be', age + 10)

# produces a value error if string instead of int is entered
age = int(input('What is your age? '))
