# Module 1
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
		print("User full name: " + self.first_name.title() + " " + self.last_name.title()
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