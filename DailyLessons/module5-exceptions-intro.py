# Sometimes errors are generated by users, not through code
# Example

value = int(input('Enter an integer: '))
print('The inverse of', value, 'is', 1 / value)
# If the value that is input is not an integer Python will produce a value error
# Exception is event that occurs during execution of program that
# disrupts the normal flow of program instructions

# We can use the following to handle exceptions:

try:
    value = int(input('Enter an integer: '))
    print('The inverse of', value, 'is', 1 / value)
except ValueError:
    print('You did not provide a number, so I will not calculate the inverse')
    value = int(input('Enter an integer: '))
except ZeroDivisionError:
    print('Division by zero is not possible, sorry')
    value = int(input('Enter an integer: '))

# Use raise SyntaxError to raise syntax errors
