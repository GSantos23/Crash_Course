# Exercise 5.7
"""
Favorite Fruit: Make a list of your favorite fruits, and then write a series 
of independent if statements that check for certain fruits in your list.
	• Make a list of your three favorite fruits and call it favorite_fruits.
	• Write five if statements. Each should check whether a certain kind of 
	fruit is in your list. If the fruit is in your list, the if block should 
	print a statement, such as You really like bananas!
"""

favorite_fruits = ['Oranges', 'Apples', 'Bananas']

fruit = 'Oranges'

if fruit in favorite_fruits:
	print("You really like", fruit)
	fruit = 'Apples'
if fruit in favorite_fruits:
	print("You really like", fruit)
	fruit = 'Bananas'
if fruit in favorite_fruits:
	print("You really like", fruit)
	fruit = 'Avocados'
if fruit not in favorite_fruits:
	print(fruit, "is not listed")
	fruit = "Pears"
if fruit not in favorite_fruits:
	print(fruit, "is not listed")