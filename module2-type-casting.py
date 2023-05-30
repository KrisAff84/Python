# Converting string input to float

height_in = input('Height converter: enter your height in inches: ')
float_height_in = float(height_in)
print('Your height in feet is:', float_height_in / 12)

# Method 2 - one function becomes argument of other function
# Both methods return the same result

height_in = float(input('Height converter: enter your height in inches: '))
print('Your height in feet is:', height_in / 12)

# Using integers instead of float using int() function

year_born = int(input('What year were you born? '))
print('In 2100, you will be', 2100 - year_born, 'years old, provided you live this long!')

# Use str() to convert integer or float to string

temp_c = input('Enter the temperature today in Celsius degrees: ')
temp_f = float(temp_c) * 1.8 + 32
temp_statement = str(temp_c) + ' degrees Celsius equals ' + str(temp_f) + ' degrees Farenheit.'
print(temp_statement)

# Converting types is called typecasting
