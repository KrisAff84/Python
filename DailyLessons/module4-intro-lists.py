# Collection or container data types
# Can store more than one value in single variable

# Lists - store multiple values of same type
# Empty list
empty_list = []
# With values
top_cities = ['New York City', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
print(top_cities)
print(top_cities[0])
print(top_cities[-1])  # returns last element
print(top_cities[-4])  # returns 4th from last

## Slicing
print(top_cities[0:3])  # returns range - exclusive
print(top_cities[2: ])  # returns index 2 through end
print(top_cities[:3])   # returns from start to 3

# The following produces same result as integers[-2]
integers = [1, 4, -2]
print(integers[integers[-1]])

