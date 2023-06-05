# Can mix data types (string, integer, etc) in lists
# but not recommended
cells = [['A1', 'A2', 'A3'], ['B1', 'B2', 'B3']]
print(cells[0])  # Prints all elements within first set of brackets
print(cells[0][0]) # Prints 1st element within first set of brackets

# to iterate nested lists, prints each item within brackets together
for x in cells:
    print('Element:', x)

# To access each element individually need nested for loops
for x in cells:
    for y in x:
        print('Element:', y)
# Nested lists also called multi-dimensional lists
# Great to iterate table
print()
table = [['A1', 'A2', 'A3'], ['B1', 'B2', 'B3']]
for row in table:
    for cell in row:
        print('Element:', cell)

# Can also print like a table
for row in table:
    for cell in row:
        print(cell, '', end='')
    print()

# For table like this
#1 2 3 4 5
#1 2 3 4 5
#1 2 3 4 5
#1 2 3 4 5
table = [[i for i in range(1, 6)] for j in range(4)]
print(table)
