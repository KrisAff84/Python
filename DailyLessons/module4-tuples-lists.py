city_1 = ('London', 'UK', 8.98)
city_2 = ('Canberra', 'Australia', 0.4)
city_3 = ('Algiers', 'Algeria', 3.9)
capitals = [('London', 'UK', 8.98), ('Canberra', 'Australia', 0.4), ('Algiers', 'Algeria', 3.9)]

for capital in capitals:
    print('Name:', capital[0], ', Country:', capital[1], ', Population:', capital[2])

user_data = ('John', 'American', 1964, [187.00, 185.57, 183.20])  #list inside tuple
# Can add new weight measurements to list inside of tuple
# Example:
user_data[3].append(182.34)
print(user_data)
print(user_data[3][1])


