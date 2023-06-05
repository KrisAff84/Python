# Determines whether input is leap year or not, True or False
year = int(input())
if year % 4 != 0 and year % 100 == 0 or year % 400 != 0:
    print('False')
else:
    print('True')










