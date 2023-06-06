#
temp_list = [1, 2, 3]
for i in range(len(temp_list)):
    temp_list.insert(i, 0)
print(temp_list)

orig_list = [1, 2, 3]
new_list = orig_list
del new_list[1:2]
print(new_list)
print(orig_list)

# The following creates inner list and outer list produces copies
my_numbers = [[i for i in range(3)] for j in range(4)]
print(my_numbers)

values = [[3 - x for x in range(2)] for y in range(5)]
sum = 0.0
for row in values:
    for cell in row:
        sum = cell + sum
print(sum)

# The following produces same result as integers[-2]
integers = [1, 4, -2]
print(integers[integers[-1]])

# Output will be 10
my_list = [0, 1, 2] * 3 + [0]
print(len(my_list))






