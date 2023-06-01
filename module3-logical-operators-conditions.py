## Available logical operators
##
## < less than
## > greater than
## <= less than or equal to
## >= greater than or equal to
## == equals
## != does not equal

password = input('Do you know the secret password? ')
if password != '--secret':
    print('Not correct')
else:
    print('Correct password')

## Boolean values can be True or False
## Do not use quotes around True or False
## Make sure to capitalize

if True:
    print('Condition met')   # Will always execute

if False:
    print('Condition met')  # Will never execute

if 2 == 2:
    print('True')

if 2 == 1:
    print('True')

if 2 == 2.0:       # Will print true, Python automatically converts to integer
    print('True')

    

