# Exercise 4.13
"""
Buffet: A buffet-style restaurant offers only five basic foods. Think of five
simple foods, and store them in a tuple.
	• Use a for loop to print each food the restaurant offers.
	• Try to modify one of the items, and make sure that Python rejects the
	change.
	• The restaurant changes its menu, replacing two of the items with different
	foods. Add a block of code that rewrites the tuple, and then use a for
	loop to print each of the items on the revised menu.
"""

buffet = ('French Fries', 'Classic Burger', 'Pasta', 'Sushi', 'Meat Loaf')

# Print buffet
for foods in buffet:
	print(foods)

# Error
#buffet[0] = "Sweet Potato"		# uncomment for error

# New Buffet
print("\nRevised menu: ")
buffet = ('Sweet Potato', 'Dobule Cheese Burger', 'Pasta', 'Sushi', 'Meat Loaf')
for foods in buffet:
	print(foods)

