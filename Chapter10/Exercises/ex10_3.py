# Exercise 10.3
'''
Guest: Write a program that prompts the user for their name. When they
respond, write their name to a file called guest.txt.
'''

your_name = input("Please, type your name: ")
#print(your_name)

filename = 'guest.txt'

with open(filename, 'w') as file_object:
	file_object.write(your_name.title())

print("Now verify the file.")