from cities_function import city_population

def test_city_country_formatting():
    city_country = city_population('Santiago', 'Chile')
    assert city_country == 'Santiago, Chile'

def test_city_country_population_formatting():
    city_country = city_population('Santiago', 'Chile', 5000000)
    assert city_country == 'Santiago, Chile - Population 5000000'