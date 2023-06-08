print_return = print('Hello world')
print(print_return)

# None used to describe null value, None is not zero

x = None

if x:
    print('None is True')
elif x is False:
    print('None is False')
else:
    print('None is not True or False, None is just None')

# None returned by functions that return nothing meaningful

