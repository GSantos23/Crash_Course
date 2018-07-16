# Exercise 8.3
'''
T-Shirt: Write a function called make_shirt() that accepts a size and the
text of a message that should be printed on the shirt. The function should 
print a sentence summarizing the size of the shirt and the message printed 
on it.
Call the function once using positional arguments to make a shirt. Call the
function a second time using keyword arguments.
'''

def make_shirt(size, msg):
	"""Display size and message for tshirt
	size -> number, msg -> string"""
	print('The size of my T-Shirt is ' + str(size) + ' and the message is: ')
	print('\t\t ' + msg + '.')


# Positional arguments
make_shirt(12,'I love Pizza')

# Keyword arguments
make_shirt(size=8, msg='BadabimBadaBoom')
