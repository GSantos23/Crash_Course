# Exercise 9.8
'''
Privileges: Write a separate Privileges class. The class should have one
attribute, privileges , that stores a list of strings as described in Exercise 9-7.
Move the show_privileges() method to this class. Make a Privileges instance
as an attribute in the Admin class. Create a new instance of Admin and use your
method to show its privileges.
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
		self.privileges = ['can add post',
						   'can delete post',
						   'can ban user', 
						   'can add user']


	def show_privileges(self):
		"""List administrator privileges"""
		print("The list of available privileges are: ")
		for sudo in self.privileges:
			print(">> " + sudo.title()) 
		
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

elliot = Admin('Elliot','Anderson', 27, 'USA')
elliot.greet_user()
elliot.privileges.show_privileges()