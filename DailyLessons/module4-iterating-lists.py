# can iterate lists
top_cities = ['New York City', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
for city in top_cities:
    print('Current city:', city)

# to access element and index number
# len returns number of characters in string and number of elements in list
for city_index in range(len(top_cities)):
    print('Current index:', city_index, '| Current city:', top_cities[city_index],)

spendings = [32.45, 18.65, 23.45, 78.32, 5.23]
sum = 0.0
for spending in spendings:
    sum += spending
print('Money spent;', sum)




