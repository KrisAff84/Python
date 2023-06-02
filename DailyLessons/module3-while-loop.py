counter = 1
while counter < 101:  # While condition is met
    print(counter)      # do something
    counter += 1
print('Finished!')

# With user input
secret_number = 14
print('''
==========================
=== SECRET NUMBER GAME ===
==========================
''')
user_input = int(input('Try to guess the secret number from 0 to 20: '))
while user_input != secret_number:
    if user_input > 20:
        print('The number must be between 0 and 20!')
        user_input = int(input('Try to guess the secret number from 0 to 20: '))
    else:
        print('Wrong!')
        user_input = int(input('Try to guess the secret number from 0 to 20: '))
print('Perfect! You have guessed the secret number.')
