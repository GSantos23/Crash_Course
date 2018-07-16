# Exercise 8.4
'''
Large Shirts: Modify the make_shirt() function so that shirts are large
by default with a message that reads I love Python. Make a large shirt and a
medium shirt with the default message, and a shirt of any size with a different
message.
'''
def make_shirt(size='Large', msg='I love Python'):
	"""Display size and message for tshirt
	size -> string, msg -> string"""
	print('The size of my T-Shirt is ' + size + ' and the message is: ')
	print('\t\t ' + msg + '.')


# Default
make_shirt()

# Medium shirt, same message
make_shirt(size='Medium')

# Any size, different message
make_shirt(size='Small', msg='Reddit Rules!')