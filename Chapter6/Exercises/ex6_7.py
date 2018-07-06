# Exercise 6.7
"""
People: Start with the program you wrote for Exercise 6-1 (page 102).
Make two new dictionaries representing different people, and store all three
dictionaries in a list called people . Loop through your list of people. As you
loop through the list, print everything you know about each person.
"""

person_0 = {'first_name': 'Gerson',
		  'last_name': 'Santos',
		  'age': 25,
		  'city': 'El Paso' }


print(person_0['first_name'] + " " + person_0['last_name'])
print(person_0['age'])
print(person_0['city'])

person_1 = {
	'first_name': 'Michael',
	'last_name':  'Mcgarry',
	'age': 45,
	'city':	'New York',
}

person_2 = {
	'first_name': 'Malieh',
	'last_name':  'Zargaran',
	'age': 29,
	'city': 'Tehran'
}

people = [person_0, person_1, person_2]

for names in people:
	print(names['first_name'] + " " + names['last_name'] + " >> " 
		+ str(names['age']) + " >> " + names['city'])

