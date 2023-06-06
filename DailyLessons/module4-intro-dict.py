# Collections used to store key value pairs

emails = {
    'Anne Stahl': 'astahl@gmail.com',
    'Peter Small': 'peters@yandex.com',
    'Mark Steel': 'mark@steel.com'
}
print(emails)
print(emails['Mark Steel'])  # Show value for key "Mark Steel"

spanish_animals = {
    'dog': 'el perro',
    'cat': 'el gato',
    'horse': 'el caballo',
    'bird': 'el pájaro'
}
print(spanish_animals['bird'])

# can't provide value to find key
# can use any data types as keys, integers, floats, or even tuples
tennis_ranking = {
    1: 'Ashleigh Barty',
    2: 'Naomi Osaka',
    3: 'Simona Halep'
}
print(tennis_ranking[2])

# Key must be immutable, value can be any data type

city_ratings = {
    'Bangkok': [7, 4, 7, 5],
    'Hanoi': [7, 6, 4, 5],
    'Manila': [6, 6, 4, 4, 5]
}
print(city_ratings['Hanoi'])