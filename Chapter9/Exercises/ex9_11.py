# Exercise 9.11
'''
Imported Admin: Start with your work from Exercise 9-8 (page 178).
Store the classes User , Privileges , and Admin in one module. Create a sepa-
rate file, make an Admin instance, and call show_privileges() to show that
everything is working correctly.
'''
from administrator import User, Privileges, Admin

abi = Admin('abigail', 'ortega', 24, 'USA')

#abi.privileges.show_privileges() # This work assuming list on class instance

# now using different way
abi.privileges.privileges = ['can add post',
						   'can delete post',
						   'can ban user', 
						   'can add user']
abi.privileges.show_privileges()

