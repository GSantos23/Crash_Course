# Part of Exercise 11.1
def city_coutry_names(city, country, population = ''):
	"""Display city and country neatly"""
	if population:
		result = city + ', ' + country + ' - population: ' + str(population)
	else:
		result = city + ', ' + country
	return result.title()

# Only for quick test
#print(city_coutry_names('santiago', 'chile'))
