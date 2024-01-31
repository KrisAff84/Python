from cities_function import city_population

while True:
    city = input('Please enter a city: ')
    if city == 'q':
        break
    country = input('Please enter a country: ')
    if country == 'q':
        break
    population = input('Please enter a population: ')
    if population == 'q':
        break

    print(city_population(city, country, population))
    