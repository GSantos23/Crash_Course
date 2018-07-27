# Exercise 9.14
'''
Dice: The module random contains functions that generate random num-
bers in a variety of ways. The function randint() returns an integer in the
range you provide. The following code returns a number between 1 and 6:
-----------------------------------------------------------------------
from random import randint
x = randint(1, 6)
----------------------------------------------------------------------
Make a class Die with one attribute called sides , which has a default
value of 6. Write a method called roll_die() that prints a random number
between 1 and the number of sides the die has. Make a 6-sided die and roll
it 10 times.
Make a 10-sided die and a 20-sided die. Roll each die 10 times.
'''
'''
from random import randint
x = randint(1 , 6)
print(x)
'''

from random import randint

#**********************************************************************
class Die():
	"""
	Emulate a die rolling
	Enter number of die sides
	"""
	def __init__(self, sides=6):
		self.sides = sides

	def roll_die(self):
		"""Roll the die!"""
		self.number = randint(1, self.sides)
		print(self.number, end=' ')

	def roll_10_times(self):
		"""Specify number of times (number)"""
		self.times = 10
		#print(self.times)
		for x in range(self.times):
			self.roll_die()

		print()

#**********************************************************************

# Instance for 6 side die
print("Result for 6-sided die: ")
roll_6 = Die(6)
roll_6.roll_die()
roll_6.roll_10_times()

# Instance for 10 side die
print("\nResult for 10-sided die: ")
roll_10 = Die(10)
roll_10.roll_die()
roll_10.roll_10_times()

# Instance for 20 side die
print("\nResult for 10-sided die: ")
roll_10 = Die(20)
roll_10.roll_die()
roll_10.roll_10_times()