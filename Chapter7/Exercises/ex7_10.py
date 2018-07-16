# Exercise 7.10
"""
7-10. Dream Vacation: Write a program that polls users about their dream
vacation. Write a prompt similar to If you could visit one place in the world,
where would you go? Include a block of code that prints the results of the poll.
"""

# Dictionary to hold answers
answers = {}

active = True

while active:
	# Prompt name and answer
	name = input("\nMy name is: ")
	ans  = input("\nIf you could visit one place in the world where would you go? ")

	# Store data in dictionary dic[key] = value
	answers[name] = ans

	# Quit poll
	repeat = input("Would you like to quit? (yes/no) ")
	if repeat == 'yes':
		active = False


# Print output
print("Information about places: ")
for person, place in answers.items():
	print(person.title() + " ----> " + place)
	