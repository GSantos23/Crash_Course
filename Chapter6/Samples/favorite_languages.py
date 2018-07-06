favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python'
}

"""
print("Sarah's favorite language is " +
	favorite_languages['sarah'].title() +
	".")
"""

for name, language in favorite_languages.items():
	print(name.title() + "'s favorite language is " + language.title() + ".")

print()

for name in favorite_languages.keys():
	print(name.title())

print()

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
	print(name.title())

	if name in friends:
		print(" Hi " + name.title() + " , I see your favorite language is " +
		      favorite_languages[name].title() + "!")


print()
if 'erin' not in favorite_languages.keys():
	print("Erin, please take our poll!")


# Loop through dictionary in order
for name in sorted(favorite_languages):
	print(name.title() + ", thank you for taking the poll.")


# Looping through all values
print()
print("The following languages have been mentionated:")
for language in favorite_languages.values():
	print(language.title())


# Use set to prevent repetition
print()
print("The following languages have been mentionated:")
for language in set(favorite_languages.values()):
	print(language.title())

# using dictionaries
favorite_languages = {
	'jen':   	['python', 'c'],
	'sarah':	['c'],
	'edward':	['ruby', 'go'],
	'phil':		['python', 'haskell'],
}

for name, languages in favorite_languages.items():
	print("\n" + name.title() + "'s favorite languages are:")
	for language in languages:
		print("\t" + language.title())