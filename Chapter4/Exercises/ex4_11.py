# Exercise 4.11
"""
My Pizzas, Your Pizzas: Start with your program from Exercise 4-1
(page 60). Make a copy of the list of pizzas, and call it friend_pizzas .
Then, do the following:
	• Add a new pizza to the original list.
	• Add a different pizza to the list friend_pizzas .
	• Prove that you have two separate lists. Print the message, My favorite
	pizzas are:, and then use a for loop to print the first list. Print the message,
	My friend’s favorite pizzas are:, and then use a for loop to print the sec-
	ond list. Make sure each new pizza is stored in the appropriate list.
"""
pizza_types = ['Pepperoni', 'Veggie', 'Meat']
message = " Pizza, is delicious"

for favorite in pizza_types:
	print(favorite + message)

print("I really love pizza")

print()
friend_pizzas = pizza_types[:]
print(friend_pizzas)

# Add new pizza to pizza_types
pizza_types.append('Chicago')
#print(pizza_types)

# Add new pizza to friend_pizzas
friend_pizzas.append('New York')
#print(friend_pizzas)

# Print lists
print("\nMy favorite pizzas are: ")
for myPizzas in pizza_types:
	print(myPizzas)

print("\nMy friend's favorite pizzas are: ")
for themPizzas in friend_pizzas:
	print(themPizzas)

