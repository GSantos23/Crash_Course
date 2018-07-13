# Exercise 7.9
"""
No Pastrami: Using the list sandwich_orders from Exercise 7-8, make sure
the sandwich 'pastrami' appears in the list at least three times. Add code
near the beginning of your program to print a message saying the deli has
run out of pastrami, and then use a while loop to remove all occurrences of
'pastrami' from sandwich_orders . Make sure no pastrami sandwiches end up
in finished_sandwiches .
"""

sandwich_orders = ['tuna', 'blt', 'pastrami', 'pastrami', 'pastrami']
finished_sandwiches = []

print("Deli has run out of pastrami D:")

while 'pastrami' in  sandwich_orders:
	sandwich_orders.remove('pastrami')

#print(sandwich_orders)


while sandwich_orders:
	order = sandwich_orders.pop()			# To retreive sandwich
	print("I made your " + order.title() + " sandwich")	
	finished_sandwiches.append(order) 


# Print all the sandwich orders
print("\nList of sanwich: ")
for subway in finished_sandwiches:
	print(subway.title())