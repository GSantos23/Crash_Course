# Exercise 9.12
'''
Multiple Modules: Store the User class in one module, and store the
Privileges and Admin classes in a separate module. In a separate file, create
an Admin instance and call show_privileges() to show that everything is still
working correctly.
'''

from user import User
from admin_priv import Admin, Privileges

abi = Admin('abigail', 'ortega', 24, 'USA')
abi.describe_user()

abi.privileges.privileges = ['can add post',
						   'can delete post',
						   'can ban user', 
						   'can add user']
abi.privileges.show_privileges()
