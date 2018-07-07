# Exercise 7.2
"""
Restaurant Seating: Write a program that asks the user how many people
are in their dinner group. If the answer is more than eight, print a message 
saying they’ll have to wait for a table. Otherwise, report that their table 
is ready.
"""

number_people = int(input("How many people are in ther dinner group? "))

if number_people > 8:
	print("Sorry, we are full. You'll have to wait")
else:
	print("Alright, your table is ready.")