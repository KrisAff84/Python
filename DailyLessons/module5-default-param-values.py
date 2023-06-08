print('Hello', 'How  are you?', end='.', sep='-')
print('Hello, how are you?')
# end and sep are keyword arguments, or named arguments
# Used at the end of a function invocation after all positional arguments
# Always optional and always have a default value
# In case of print function, default value of end=/n newline. Default value of sep=' '

# How keywords work for user created functions
def print_letter_count(text, letter='a'): # Assigns default for letter to a
    counter = 0
    for char in text:
        if char == letter:
            counter += 1
    print('Number of', letter, 'is', counter)


print_letter_count('How many letters a are here?')


# Postitional arguments must appear before named/keyword arguments