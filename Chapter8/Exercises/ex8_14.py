# Exercise 8.14
'''
Cars: Write a function that stores information about a car in a dictionary.
The function should always receive a manufacturer and a model name. 
It should then accept an arbirary number of keywords arguments. Call the
function with the requiered information and two other name-value pairs, such
as a color or optional feature. Your function should work for a call like 
this one:
------------------------------------------------
car = make_car('subaru', 'outback', color = 'blue', two_package = True)
-----------------------------------------------

Print the dictionary that's returned to make sure all the information was
stored correctly.
'''

def make_car(manufacturer, model, **addtional):
	feature = {}							# Create an empty dictionary

	feature['brand'] = manufacturer 		# Add key - value to dict
	feature['model'] = model 				# Add key - value to dict

	for key, value in addtional.items():	# Loop over new key - value
		feature[key] = value

	return feature							# send result



car = make_car('subaru', 'outback', color = 'blue', two_package = True)
print(car)

car = make_car('toyota', 'corolla', color = 'black')
print(car)


car = make_car('volkswagen', 'gti', color = 'red', turbo = True)
print(car)



