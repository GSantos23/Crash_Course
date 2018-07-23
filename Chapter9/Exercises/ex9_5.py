# Exercise 9.5
'''
Login attempts: Add an attribute called login_attempts to your User
class from Exercise 9-3 (page 166). Write a method called 
increment_login_attempts() that increments the value of login_attempts
by 1. Write another method called reset_login_attempts() that resets the
value of login_attempts to 0.
	Make an instance of the User class and call increment_login_attempts()
several times. Print the value of login_attempts() to make sure that it was
incremented properly, and then call resett_login_attempts(). Print 
login_attempts() again to make sure it was reset to 0.
'''
class User():
	"""User profile information"""
	def __init__(self, first_name, last_name, age, country):
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.country = country
		self.login_attempts = 0


	def describe_user(self):
		print("\nUser description ")
		print("User full name: " + self.first_name + " " + self.last_name 
			+ ".")
		print("User age: " + str(self.age))
		print("User country: " + self.country)


	def greet_user(self):
		print("\nHi, " + self.first_name + " " +self.last_name + ".")
		print("How is " + self.country + " today.")


	def increment_login_attempts(self):
		"""Increment value of login_attempts by 1."""
		self.login_attempts += 1


	def reset_login_attempts(self):
		"""Reset value of login_attempts to 0."""
		self.login_attempts = 0


gerson = User('Gerson', 'Santos', 26, 'Mexico')

#gerson.describe_user()
gerson.greet_user()

gerson.increment_login_attempts()
gerson.increment_login_attempts()
gerson.increment_login_attempts()
print("Number of login attempts: " + str(gerson.login_attempts))

gerson.reset_login_attempts()
print("Number of login attempts: " + str(gerson.login_attempts))