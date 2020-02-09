# Darrell Powe III
# This is a practice exercise from the book "Python Crash Course"
# Exercise 8-6


def city_country(city, country):
    """Returns a string formatted like 'Santiago, Chile'."""

    clean = "'" + city.title() + ', ' + country.title() + "'"
    return clean


change = city_country('new york', 'united states')
print(change)