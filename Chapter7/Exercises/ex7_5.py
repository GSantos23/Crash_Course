# Exercise 7.5
"""
Movie Tickets: A movie theater charges different ticket prices depending on
a person’s age. If a person is under the age of 3, the ticket is free; if they are
between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is
$15. Write a loop in which you ask users their age, and then tell them the cost
of their movie ticket.
"""

prompt = "Enter your age to know your ticket price: "
prompt += "\nType '-1' to exit. -> "

while True:
	ticket = int(input(prompt))

	if ticket < 3 and ticket >= 0:
		print("Free ticket :)")
	elif ticket >= 3 and ticket <= 12:
		print("Ticket is $10")
	elif ticket > 12:
		print("Ticket is $15")
	else:
		break
