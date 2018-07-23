# Exercise 9.4
'''
Number Served: Start with your program from Exercise 9-1 (page 166).
Add an attribute called number_served with a default value of 0. Create an
instance called restaurant from this class. Print the number of customers the
rstaurant has served and then change this value and print again.
	Add a method called set_number_served() that lets you set the number
of customers that have been served. Call this method with a new number and
print the value again.
	Add a method called increment_number_served() that lets you incremet
the number of customers who've been served. Call this method whit any
number you like that could represent ow many customers were served in , say, a
day of business.
'''

class Restaurant():
	"""Give you Restaurant information"""
	def __init__(self, restaurant_name, cuisine_type):
		#super(Restaurant, self).__init__()
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 0


	def describe_restaurant(self):
		"""Print restaurant name and cuisine type"""
		print("The restaurant is called " + self.restaurant_name.title())
		print("It's cuisine type is " + self.cuisine_type)


	def open_restaurant(self):
		print(self.restaurant_name + " is open  now!")


	def set_number_served(self, persons):
		"""Set number of customers that have been served"""
		self.number_served = persons		# Variable to hold new number
		print("The number of customers served: " + str(self.number_served))


	def increment_number_served(self, more_customers):
		"""Increment the number of customers who've been served"""
		self.number_served += more_customers


	def total_amout(self):
		"""Print total costumers in a day"""
		print("Total amount of costumers today: " + str(self.number_served))



# Instance of class
restaurant = Restaurant('Garufa', 'Argentinian')
restaurant.describe_restaurant()
restaurant.open_restaurant()

# Change number_served directly
#restaurant.number_served = 15
#print("The number of customers served: " + str(restaurant.number_served))

# Using a method
restaurant.set_number_served(25)

# Update costumers
restaurant.increment_number_served(100)

# Print total costumers
restaurant.total_amout()