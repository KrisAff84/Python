invited_guests = ['Kate', 'Adam', 'Kris', 'Silas', 'Cara Ann', 'Wilder', 'Jimmy']
name = input('What is your name? ')
if name in invited_guests:    # Checks for presence of name in invited_guests list
    print('Welcome!')
else:
    print('You are not invited!')

# Can also use not in

invited_guests = ['Kate', 'Adam', 'Kris', 'Silas', 'Cara Ann', 'Wilder', 'Jimmy']
name = input('What is your name? ')
if name not in invited_guests:    # Checks for presence of name in invited_guests list
    print('Welcome!')
else:
    print('You are not invited!')