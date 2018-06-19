# Exercise 2.10
# Adding Comments: Choose two of the programs you’ve written, and add at least one comment to each. 
# If you don’t have anything specific to write because your programs are too simple at this point, just add your name and
# the current date at the top of each program file. Then write one sentence describing what the program does.

# Author : Gerson Santos
# Date 	 : Tuesday, June 19th 2018


# Program 1: Exercise 2.9
# Print a message with my favorite number

fav_num = 23
message = "My favorite number is: "

print(message + str(fav_num))			# str() to typecast int -> str

# Author : Gerson Santos
# Date 	 : Tuesday, June 19th 2018

# Program 2: Exercise 2.4
# Display a neme in different formats

name = "Gerson"

print("lowercase: " + name.lower())
print("uppercase: " + name.upper())
print("titlecase: " + name.title())