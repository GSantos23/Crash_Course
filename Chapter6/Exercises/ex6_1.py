# Exercise 6.1
"""
6-1. Person: Use a dictionary to store information about a person you know.
Store their first name, last name, age, and the city in which they live. You
should have keys such as first_name , last_name , age , and city . Print each
piece of information stored in your dictionary.
"""

person = {'first_name': 'Gerson',
		  'last_name': 'Santos',
		  'age': 25,
		  'city': 'El Paso' }


print(person['first_name'] + " " + person['last_name'])
print(person['age'])
print(person['city'])