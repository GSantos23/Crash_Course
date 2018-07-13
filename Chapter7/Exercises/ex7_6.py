# Exercise 7.6
"""
Three Exits: Write different versions of either Exercise 7-4 or Exercise 7-5
that do each of the following at least once:
• Use a conditional test in the while statement to stop the loop.
• Use an active variable to control how long the loop runs.
• Use a break statement to exit the loop when the user enters a 'quit' value.
"""

prompt = "Enter the pizza toppings you want in your pizza."
prompt += "\nEnter 'quit' to exit. "

# Version 1
"""
topping = input(prompt)

while topping != 'quit':
	print("Good Choice :)")

	topping = input(prompt)
"""

# Version 2
"""
active = True

while active:
	topping = input(prompt)

	if topping == 'quit':
		active = False
"""

# Version 3

while True:
	topping = input(prompt)

	if topping == 'quit':
		break
	else:
		print("Good choice :)")
