# Exercise 9.7
'''
Admin: An administrator is a special kind of user. Write a class called
Admin that inherits from the User class you wrote in Exercise 9-3 (page 166)
or Exercise 9-5 (page 171). Add an attribute, privileges , that stores a list
of strings like "can add post" , "can delete post" , "can ban user" , and so on.
Write a method called show_privileges() that lists the administrator’s set of
privileges. Create an instance of Admin , and call your method.
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



class Admin(User):
	"""Describe privileges for Administrator"""
	def __init__(self, first_name, last_name, age, country):
		super().__init__(first_name, last_name, age, country)
		self.privileges = []						# Insert list


	def show_privileges(self):
		"""List administrator privileges"""
		print("The list of available privileges are: ")
		for sudo in self.privileges:
			print(">> " + sudo.title()) 
		

elliot = Admin('Elliot','Anderson', 27, 'USA')
elliot.privileges = ['can add post', 'can delete post', 'can ban user', 'can add user']
# instance.method if you previouly defined arguments (^)
elliot.show_privileges()	