# Exercise 4.2
"""
Animals: Think of at least three different animals that have a common char-
acteristic. Store the names of these animals in a list, and then use a for loop to
print out the name of each animal.
	• Modify your program to print a statement about each animal, such as
	A dog would make a great pet.
	• Add a line at the end of your program stating what these animals have in
	common. You could print a sentence such as Any of these animals would
	make a great pet
"""

birds = ['Eagles', 'Hawks', 'Hummingbirds']
facts = ", are wounderful animals that fly in this world"

for names in birds:
	#print(names)
	print(names + facts)

print("Any of these animals must be protected from illegal hunting.")