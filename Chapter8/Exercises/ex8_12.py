# Exercise 8.12
'''
Sandwiches: Write a function that accepts a list of items a person wants
on a sandwich. The function should have one parameter that collects as many
items as the function call provides, and it shold print a summary of the
sandwich that is being ordered. Call the function three times, using a 
different number of arguments each time.
'''

def make_sandwich(*ingredients):
	"""Collects ingredients for a sandwich"""
	print("\nThe ingredients for this order are:")
	for items in ingredients:
		print("* " + items.title())


make_sandwich('cheese')
make_sandwich('peanut butter', 'jelly')
make_sandwich('veggies','meatballs','pepper jack cheese')


