# Exercise 6.10
"""
Favorite Numbers: Modify your program from Exercise 6-2 (page 102) so
each person can have more than one favorite number. Then print each person’s
name along with their favorite numbers.
"""

fav_number = {
	'Gerson': 	[23, 21],
	'Yose':		[56,100,109],
	'Miguel':	[2,19],
	'Sarah':	[99,69],
	'Obi':		[66,1991],
}

for name, numbers in fav_number.items():
	print(name + " favorite numbers are: ")
	for var in numbers:
		print(var)