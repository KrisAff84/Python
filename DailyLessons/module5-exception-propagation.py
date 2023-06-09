
def get_month(user_info):
    month = int(input('What is the month (1-12) of your birthday? '))
    user_info.append(month)

def get_day(user_info):
    day = int(input('What is the day of your birthday? '))
    user_info.append(day)

def get_year(user_info):
    year = int(input('What is the year of your birthday? '))
    user_info.append(year)

# Exceptions can be handled in the function that calls the other functions
# Exceptions are propagated
def get_user_bday(user_info):
    try:
        get_month(user_info)
        get_day(user_info)
        get_year(user_info)
        print('So your birthday is', user_info)
    except ValueError:
        print('You entered incorrect data, bye!')


print('Hi, I will collect some info about your birthday!')
user_info = []
get_user_bday(user_info)
