### Lists ###
var = []
print(type(var))
# Type for variable type
var = [236, 764, 218, 923, 143, 97, 357]
print(var)
var.append(1038)
print(var)
print(dir(var))  # To get info from function
var = var + [245]
print(var)
numbers = [0, 1, 2, 3, 4, ]
print(numbers)
for number in numbers:
    print(number * 2)

print(numbers[1])
numbers = numbers + [76]
print(numbers)

more_numbers = list(range(0, 20, 1))
# Above lists numbers in range 0-20 incremented by 1
print(type(more_numbers))
print(more_numbers)

more_numbers.reverse()
print(more_numbers)

print(more_numbers.index(13)) # To get index of value


