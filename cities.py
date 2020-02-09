# Darrell Powe III
# This is a practice exercise from the book "Python Crash Course"
# Exercise 8-5


def describe_city(city, country='The United States'):
    """Prints a simple sentence about the parameters passed to the function."""
    print(city.title() + ' is in ' + country.title() + '.')


describe_city('New York')
describe_city('Tokyo', country='Japan')
describe_city('Manchester', country='The United Kingdom')
