def get_average(input_numbers):
    sum = 0.0
    for number in input_numbers:
        sum += number
    average = sum / len(input_numbers)
    print(average)


get_average([5.0, 3.5, 7.8, 9.9, 10.0])  # list is called argument
# list is assigned to parameter, but argument is not the same as parameter


def print_letter_count(text, letter):
    counter = 0
    for char in text:
        if char == letter:
            counter += 1
    print('Number of', letter, 'is', counter)


print_letter_count('excellent', 'e')
print_letter_count('in order to succeed, you must be willing to put in the work every day', 'n')

# position of argument is important, they are called positional arguments
# can also used named arguments to swap places of arguments
print_letter_count(letter='a', text='What a lovely day it is today!')



