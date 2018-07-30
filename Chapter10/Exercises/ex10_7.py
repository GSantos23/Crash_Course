# Exercise 10.7
'''
Addition Calculator: Wrap your code from Exercise 10-6 in a while loop
so the user can continue entering numbers even if they make a mistake and
enter text instead of a number.
'''

print("Type 'exit' to quit.")

while True:
	try:
		x = input("Enter a number: ")
		if x == 'exit':
			print("Bye.")
			break

		x = int(x)

		y = input("Enter a number: ")
		if y == 'exit':
			print("Bye.")
			break

		y = int(y)

	except ValueError:
		print("Sorry I can only handle numbers.")
	else:
		add = x + y
		print("Result: " + str(add))
