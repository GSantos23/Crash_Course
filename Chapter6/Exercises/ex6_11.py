# Exercise 6.11
"""
Cities: Make a dictionary called cities . Use the names of three cities as
keys in your dictionary. Create a dictionary of information about each city 
and include the country that the city is in, its approximate population, and 
one fact about that city. The keys for each city’s dictionary should be 
something like country , population , and fact . Print the name of each city 
and all of the information you have stored about it.
"""

cities = {
	'chicago': {
		'country': 		'USA',
		'population':	2.7e+06,
		'fact':			'Chicago Cubs 2016 Champions',
	},
	'dublin': {
		'country':		'Ireland',
		'population':	5.2e+05,
		'fact':			'Redhead heaven',
	},
	'osaka': {
		'country':		'Japan',
		'population':	2.6e+06,
		'fact':			'Famous for puppets plays'
	}
}

for place, info in cities.items():
	print(place.title())
	cntr = info['country']
	popu = info['population']
	fcts = info['fact']

	print("\tCountry: " + cntr)
	print("\tPopulation: " + str(popu))
	print("\tFacts: " + fcts)