# Exercise 9.3
'''
Users: Make a class called User . Create two attributes called first_name
and last_name , and then create several other attributes that are typically 
stored in a user profile. Make a method called describe_user() that prints 
a summary of the user’s information. Make another method called 
greet_user() that prints a personalized greeting to the user.
Create several instances representing different users, and call both methods
for each user
'''

class User():
	"""User profile information"""
	def __init__(self, first_name, last_name, age, country):
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.country = country


	def describe_user(self):
		print("\nUser description ")
		print("User full name: " + self.first_name + " " + self.last_name 
			+ ".")
		print("User age: " + str(self.age))
		print("User country: " + self.country)


	def greet_user(self):
		print("\nHi, " + self.first_name + " " +self.last_name + ".")
		print("How is " + self.country + " today.")


gerson = User('Gerson', 'Santos', 26, 'Mexico')
abigail = User('Abigail', 'Ortega', 24, 'USA')
jin = User('Xeshing', 'Xao', 23, 'China')

gerson.describe_user()
gerson.greet_user()

abigail.describe_user()
abigail.greet_user()

jin.describe_user()
jin.greet_user()


