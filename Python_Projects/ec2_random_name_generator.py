import random
import string

number_of_instances = int(input('How many EC2 instances do you need names for? '))
department = input('What department do you work in? ')

for x in range(number_of_instances):
    characters = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    print(department + '-' + characters)

