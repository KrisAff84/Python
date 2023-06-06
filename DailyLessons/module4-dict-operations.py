# Can start with empty and add elements to it
grades = {}
grades['John'] = 'A-'
grades['Anne'] = 'B'
print(grades)
# Can update same as adding
grades['Anne'] = 'A'
# Or
grades.update({'John':'A'})
print(grades)
print(len(grades))

# Using if in operator
if 'John' in grades:
    print('John got:', grades['John'])

# To delete key use del operator
del grades['John']
print(grades)

# Iteration
grades['John'] = 'B'
for el in grades:
    print(el)

# Same output
for el in grades.keys():
    print(el)

# Iterate items instead of keys
for el in grades.values():
    print(el)

# Iterate keys and values
for person, grade in grades.items():
    print(person, 'got', grade)
    print(grade, 'for', person)

# Practice
# Findin average lap time
lap_times = {}
lap_times[1] = 145
lap_times[2] = 135
lap_times[3] = 142
lap_times[4] = 137
lap_times[5] = 146

print(lap_times)
total_time = 0
for time in lap_times.values():
    total_time = total_time + time
print('The average lap time is', total_time // len(lap_times), 'seconds')










