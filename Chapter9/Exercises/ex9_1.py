# Exercise 9.1
'''
Restaurant: Make a class called Restaurant. The __init__() method for
Restaurant should store two attributes: a restaurant_name and cuisine_type.
Make a method called describe_restaurant() that prints these two pieces of
information, and a method called open_restautant that prints a message 
indicating that the restaurant is open.
	Make an instance called restaurant from your class. Print to attributes
indidually, and then call both methods.
'''

class Restaurant():
	"""Give you Restaurant information"""
	def __init__(self, restaurant_name, cuisine_type):
		#super(Restaurant, self).__init__()
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type


	def describe_restaurant(self):
		"""Print restaurant name and cuisine type"""
		print("The restaurant is called " + self.restaurant_name.title())
		print("It's cuisine type is " + self.cuisine_type)

	def open_restaurant(self):
		print(self.restaurant_name + " is open  now!")


# Instance of class
restaurant = Restaurant('Garufa', 'Argentinian')
restaurant.describe_restaurant()
restaurant.open_restaurant()
