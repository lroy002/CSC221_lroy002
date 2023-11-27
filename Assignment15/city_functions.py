def city_country(city, country, population =None):
  if population is not None:
    return f"{city.title()}, {country.title()} - population {population}"
  else:
    return f"{city.title()}, {country.title()}"