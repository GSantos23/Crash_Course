# Exercise 10.11
'''
Favorite Number: Write a program that prompts for the user’s favorite
number. Use json.dump() to store this number in a file. Write a separate pro-
gram that reads in this value and prints the message, “I know your favorite
number! It’s _____.”
'''
import json

def get_fav_number():
	"""Get stored username if available"""
	filename = 'fav_number.json'

	try:
		with open(filename) as f_obj:
			number = json.load(f_obj)
	except FileNotFoundError:
		return None
	else:
		return number


def get_new_number():
	"""Propmt for a new username"""
	number = input("What is your favorite number? ")
	filename = 'fav_number.json'
	with open(filename, 'w') as f_obj:
		json.dump(number, f_obj)
	return username



def display_number():
	"""Greet user by name"""
	number = get_fav_number()
	if number:
		print("I know your favorite number! It’s " + number + "!")
	else:
		number = get_new_number()
		print("We'll remember you when you come back, " + number + "!")


display_number()