fav_band = 'Steely Dan'
print(fav_band[5])
print(fav_band[:6])

# Upper or lower methods
text = 'please capitalize me'
text_cap = text.upper()
print(text_cap)

# Checks if input is a number
user_number = input('Please provide a number: ')
if user_number.isnumeric():
    print('Thank you, that\'s a correct number!')
else:
    print('Sorry,', user_number, 'is not a number!')



