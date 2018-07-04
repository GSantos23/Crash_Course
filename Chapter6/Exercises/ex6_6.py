# Exercise 6.6
"""
Polling: Use the code in favorite_languages.py (page 104).
	• Make a list of people who should take the favorite languages poll. 
	Include some names that are already in the dictionary and some that 
	are not.
	• Loop through the list of people who should take the poll. If they have
	already taken the poll, print a message thanking them for responding.
	If they have not yet taken the poll, print a message inviting them to take
	the poll.
"""

favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python'
}

# List of names
poll_names = ['jen', 'phil', 'erika', 'paul']

for people in favorite_languages.keys():
	#print(people)

	if people in poll_names:
		print("Thanks " + people.title() + ", for responding the poll")
	else:
		print(people.title() + ", Do you want to fill a poll?")