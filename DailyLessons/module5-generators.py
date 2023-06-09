# Generators typically used when you want to return a lot of values 1 by 1

def get_number():
    for i in range(1, 4):
        yield i    # Using yield makes this function a generator

generator = get_number()
print(next(generator))
print(next(generator))
print(next(generator))

# Will get new generators with next as long as function code allows it

for x in get_number():  # Can also use generator in for loop
    print(x)

# Or in lists
numbers = list(get_number())
print(numbers)

# Don't worry too much about generators as entry-level developer
