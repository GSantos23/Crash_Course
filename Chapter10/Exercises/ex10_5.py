# Exercise 10.5
'''
Programming Poll: Write a while loop that asks people why they like
programming. Each time someone enters a reason, add their reason to a file
that stores all the responses.
'''
answer = ''
filename = 'responses.txt'

print("Type q to exit.")


while answer != 'q':
	answer = input("Why do you like programming? >> ")

	if answer != 'q':
		reason = answer.capitalize()					# Only first letter is mayus
		#print(greeting)
		with open(filename, 'a') as file_object:
			file_object.write(reason + '\n')
	else:
		print("You exit the propmt. Now Verify the file")