empty_tuple = ()
one_el_tuple_a = (1,)
one_el_tuple_b = 1,
three_el_tuple = 1, 2, 3
print(three_el_tuple)
print(one_el_tuple_a)
print(one_el_tuple_b)

# Lists are mutable
# Tuples are immutable, like strings
# You can change the assigned values like so

user_data = ('John', 'American', 1964)
user_data = ('Katya', 'Russian', 1980)
print(user_data)

# But cannot append or delete values

user_data.append('teacher') # Returns error
del user_data[0]  # returns error

