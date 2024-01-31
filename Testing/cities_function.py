def city_population(city, country, population=''):
    """Return a string like 'Santiago, Chile - population 5000000'."""
    if population:
        city_country = f"{city}, {country} - population {population}"
    else:
        city_country = f"{city}, {country}"

    return city_country.title()