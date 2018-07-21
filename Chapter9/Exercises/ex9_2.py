# Exercise 9.2
'''
Three Restaurants: Start with your class from Exercise 9-1. Create three
different instances from the class, and call describe_restaurant() for each
instance.
'''

class Restaurant():
	"""Give you Restaurant information"""
	def __init__(self, restaurant_name, cuisine_type):
		super(Restaurant, self).__init__()
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type


	def describe_restaurant(self):
		"""Print restaurant name and cuisine type"""
		print("The restaurant is called " + self.restaurant_name.title())
		print("It's cuisine type is " + self.cuisine_type)

	def open_restaurant(self):
		print(self.restaurant_name + " is open  now!")



# Three insrances
favorite_restaurant = Restaurant('Los Arcos', 'Seafood')
expensive_restaurant = Restaurant('Maria Chuchena', 'Mexican')
old_trusty_restaurant = Restaurant('Mcdonals', 'Fast Food')

favorite_restaurant.describe_restaurant()
expensive_restaurant.describe_restaurant()
old_trusty_restaurant.describe_restaurant()