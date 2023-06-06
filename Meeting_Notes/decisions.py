import random

number = random.randint(0, 10)

threshold = 6

if number > 8:
    print('Huge number')
if number > threshold:
    print('Big number')
elif number < threshold:
    print('small number')
elif number == threshold:
    print('number is equal to ', threshold)
if number > 4:
    print('number is greater than 4')


print(number)
