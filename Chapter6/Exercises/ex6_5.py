# Exercise 6.5
"""
Rivers: Make a dictionary containing three major rivers and the country
each river runs through. One key-value pair might be 'nile': 'egypt'.
	• Use a loop to print a sentence about each river, such as The Nile runs
	through Egypt.
	• Use a loop to print the name of each river included in the dictionary.
	• Use a loop to print the name of each country included in the dictionary.
"""

rivers = {'nile': 'egypt', 'sena': 'france', 'rin': 'germany'}

for output, country in rivers.items():
	print("The " + output.title() + " runs through " + country.title())

# River Name
# Another solution is keys() method
print()
for riverName in rivers:
	print(riverName.title())

# Country Name
print()
for countryName in rivers.values():
	print(countryName.title())