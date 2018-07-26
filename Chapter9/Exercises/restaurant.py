#  Restaurant Class
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


class IceCreamStand(Restaurant):
	"""Display information about ice cream flavors"""
	def __init__(self, restaurant_name, cuisine_type):
		super().__init__(restaurant_name, cuisine_type)
		self.flavors = ['vanilla', 'chocolate', 'lemon']

	def describe_flavors(self):
		"""Prints the flavors"""
		#print("The available flavors are: " + str(self.flavors))
		print("\nThe available flavors are: ")
		for flavors in self.flavors:
			print("* " + flavors)