## Boolean operators = and, or, not

user_age = int(input('What is your age? '))
user_country = input('What is your country? ')

if user_age < 25 and user_country == 'Germany':
    print('You can apply for a German student exchange program')
else:
    print('Sorry, you do not qualify')

########################################

user_country = input('What is your country? ')

if user_country == 'Sweden' or user_country == 'Denmark' or user_country == 'Norway':
    print('You can apply for a Scandinavian student exchange program')
else:
    print('Sorry, you do not qualify')

user_country = input('What is your country? ')    

if user_country == 'Sweden' or 'Denmark' or 'Norway':
    print('You can apply for a Scandinavian student exchange program')
else:
    print('Sorry, you do not qualify')

#########################################

user_country = input('What country are you from? ')

if not user_country == 'Germany':
    print('You are not from Germany')
else:
    print('You are from Germany')
    
########################################

user_age = int(input('What is your age? '))
user_country = input('What is your country? ')

if not user_country == 'Germany' and user_age < 25 or \
   user_country == 'Germany' and user_age < 23:
    print('You qualify!')
else:
    print('You don\'t qualify')

###########################################
##    Order of Boolean operators
##    1. not
##    2. and
##    3. or


# Add brackets to improve clarity, can also change order of Boolean operators

user_age = int(input('What is your age? '))
user_country = input('What is your country? ')

if ((not user_country == 'Germany') and user_age < 25) or \
   (user_country == 'Germany' and user_age < 23):
    print('You qualify!')
else:
    print('You don\'t qualify')

