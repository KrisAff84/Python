names = ['Alice', 'Bob', 'Amanda', 'Charlie', 'David', 'Annie']

names_starting_with_A = [n for n in names if n.upper().startswith('A')]
print(names_starting_with_A)

# Or without accounting for lowercase first letters
names_starting_with_A = [n for n in names if n.startswith('A')]

# Another way

alt_way = [n for n in names if n.upper()[0] == 'A']
print(alt_way)