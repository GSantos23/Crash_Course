# Administrator class
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

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

class Admin(User):
	"""Describe privileges for Administrator"""
	def __init__(self, first_name, last_name, age, country):
		super().__init__(first_name, last_name, age, country)
		self.privileges = Privileges()						# Insert Class


class Privileges():
	"""Store list of privileges"""
	def __init__(self, privileges=[]):	# privileges=['text']
		"""Privileges list"""
		#self.privileges = ['can add post',
		#				   'can delete post',
		#				   'can ban user', 
		#				   'can add user']
		self.privileges = []



	def show_privileges(self):
		"""List administrator privileges"""
		print("The list of available privileges are: ")
		for sudo in self.privileges:
			print(">> " + sudo.title()) 

