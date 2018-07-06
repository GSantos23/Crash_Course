# Exercise 6.8
"""
Pets: Make several dictionaries, where the name of each dictionary is the
name of a pet. In each dictionary, include the kind of animal and the owner’s
name. Store these dictionaries in a list called pets . Next, loop through your 
list and as you do print everything you know about each pet.
"""

# Dictionary
pet_0 = {
	'kind': 'dog',
	'owner': 'james',
}

pet_1 = {
	'kind': 'cat',
	'owner': 'emily',
}

pet_2 = {
	'kind': 'bird',
	'owner': 'robert',
}

# list
pets = [pet_0, pet_1 ,pet_2]


for friend in pets:
	print(friend['owner'].title() + " has a " + friend['kind'])

