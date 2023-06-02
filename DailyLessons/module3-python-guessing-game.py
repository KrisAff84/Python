year_released = 1994
guess = int(input('When was Python 1.0 released? '))
while guess != year_released:
    if guess > year_released:
        print('It was earlier than that!')
        guess = int(input('When was Python 1.0 released? '))
    elif guess < year_released:
        print('It was later than that!')
        guess = int(input('When was Python 1.0 released? '))
    else:
        break
if guess == year_released:
    print('Correct!')

#### Another method ######

year_released = 1994
while True:
    guess = int(input('When was Python 1.0 released? '))
    if guess > year_released:
        print('It was earlier than that!')
    elif guess < year_released:
        print('It was later than that!')
    else:
        print('Correct!')
        break
        
