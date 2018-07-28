# Exercise 10.4
'''
Guest Book: Write a while loop that prompts users for their name. When
they enter their name, print a greeting to the screen and add a line recording
their visit in a file called guest_book.txt. Make sure each entry appears on a
new line in the file.
'''

names = ''
filename = 'guest_book.txt'

print("Type q to exit.")


while names != 'q':
	names = input("Type your name >> ")

	if names != 'q':
		greeting = "Thanks " + names.title() + "!!!"
		print(greeting)
		with open(filename, 'a') as file_object:
			file_object.write(greeting + '\n')
	else:
		print("You exit the propmt. Now Verify the file")
