# Exercise 8.5
'''
Cities: Write a function called describe_city() that accepts the name of
a city and its country. The function should print a simple sentence, such as
Reykjavik is in Iceland . Give the parameter for the country a default value.
Call your function for three different cities, at least one of which is not in 
the default country.
'''

def describe_city(citiy_name, country):
	"""Display city name and country
	city_name -> string, country -> string"""
	print(citiy_name.title() + " is in " + country.title())


describe_city('reykjavik', 'Iceland')
describe_city('kiev', 'ukraine')
describe_city('guadalajara', 'mexico')
