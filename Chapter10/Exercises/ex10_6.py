# Exercise 10.6
'''
Addition: One common problem when prompting for numerical input
occurs when people provide text instead of numbers. When you try to convert
the input to an int , you’ll get a TypeError . Write a program that prompts for
two numbers. Add them together and print the result. Catch the TypeError if
either input value is not a number, and print a friendly error message. Test your
program by entering two numbers and then by entering some text instead of a
number.
'''
def enter_two_numbers():
	"""Function to handle only numbers"""
	try:
		number_1 = int(input("Enter a number: "))
	except ValueError:
		print("Sorry I can only handle numbers.")
	else:
		return  number_1;
	

print(enter_two_numbers() + enter_two_numbers())
