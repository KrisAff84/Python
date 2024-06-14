list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8], [9]]
# Your list comprehension here
flattened_list = [i for sublist in list_of_lists for i in sublist]
print(flattened_list)

# for sublist in list, for item in sublist
"""
We work big to small for this list comprehension example, first dealing with the 
sublists in the list, for each item in the sublist. So another way of thinking about 
this problem is "list each item of the sublist (for i in sublist ), for each sublist 
in the list (for sublist in list). The very first "i" is what goes in the list.
"""

# Can also perform any alterations on the final numbers, such as squaring them
flattened_squared = [pow(i, 2) for sublist in list_of_lists for i in sublist]
print(flattened_squared)

# Or turning them into floats
floats_list = [float(i) for sublist in list_of_lists for i in sublist]
print(floats_list)

# Or floats with two decimal places 
two_decimals = [(f'{i:.2f}') for sublist in list_of_lists for i in sublist]
print(two_decimals)