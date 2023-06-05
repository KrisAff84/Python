name_original = 'Jon Snow'
name_new = name_original
# Both variables now have the same value but are independent
# example, now change one of the variables
name_original = 'Daenerys Targaryen'
print(name_new, name_original)

# Same rule applies to other basic data types
# But not to data collections like lists
# The below example prints the same numbers
list_original = [1, 2, 3]
list_new = list_original
list_original[0] = -5
print('Original', list_original, '\nNew:', list_new)
# Name of list does not point to actual list
# References place variables are stored
# To actually make a copy you can modify
# Use slicing
list_original = [1, 2, 3]
list_new = list_original[:]
list_original[0] = -5
print('Original', list_original, '\nNew:', list_new)

# Or
list_original = [1, 2, 3]
list_new = list_original[:2]  # Until 2
list_original[0] = -5
print('Original', list_original, '\nNew:', list_new)