# Exercise 9.6
'''
Ice Cream Stand: An ice cream stand is a specific kind of restaurant. Write
a class called IceCreamStand that inherits from the Restaurant class you wrote
in Exercise 9-1 (page 166) or Exercise 9-4 (page 171). Either version of
the class will work; just pick the one you like better. Add an attribute called
flavors that stores a list of ice cream flavors. Write a method that displays
these flavors. Create an instance of IceCreamStand , and call this method.
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

# Instance for child class
ice_cream = IceCreamStand('Holanda','Ice Cream')
# If you want to use dot notation instead:
# Uncomment following line and clear the list of line 32 :)
#ice_cream.flavors = ['vanilla', 'chocolate', 'lemon']	 

ice_cream.describe_restaurant()
ice_cream.describe_flavors()