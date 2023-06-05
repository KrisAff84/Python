# swapping values
first = input('Enter first number: ')
second = input('Enter second number: ')
# if you do first = second or vice versa you lose one value
# first = second   does not work
# second = first   does not work
# Most programming languages can do the following

print('Before swapping:', first, second)
temporary = first
first = second
second = temporary
print('After swapping:', first, second)

# Shortcut in python

first = input('Enter first number: ')
second = input('Enter second number: ')
print('Before swapping:', first, second)
first, second = second, first
print('After swapping:', first, second)

# Works with lists as well
top_cities = ['New York City', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
top_cities[0], top_cities[4] = top_cities[4], top_cities[0]
print(top_cities)

# to sort
top_cities.sort()
print(top_cities)
# with numbers too

random_numbers = [2, 5, 0, -3, 4]
random_numbers.sort()
print(random_numbers)

# Reverse order
random_numbers = [2, 5, 0, -3, 4]
random_numbers.sort(reverse=True)
print(random_numbers)

# No going back after sort. If you need a temporary sort
top_cities = ['New York City', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
print(sorted(top_cities))
print(top_cities)

# list_name.sort is a method, sorts original list
# sorted(list_name) gives a new sorted list, keeps original unchanged