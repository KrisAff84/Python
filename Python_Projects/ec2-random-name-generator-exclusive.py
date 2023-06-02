import random
import string

number_of_instances = int(input('How many EC2 instances do you need names for? '))
department = input('What department do you work in? ')

if department.casefold() in {'Marketing'.casefold(), 'Accounting'.casefold()}:
    for x in range(number_of_instances):
        characters = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
        print(department.capitalize() + '-' + characters)
elif department.casefold() in {'finops'.casefold(), 'financial operations'.casefold(), 'fin ops'.casefold()}:
    for x in range(number_of_instances):
        characters = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
        print('FinOps' + '-' + characters)
else:
    print('You do not have permission to use this name generator')
