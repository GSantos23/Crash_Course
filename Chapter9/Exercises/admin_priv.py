# Module 2
from user import User

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