# Exercise 10.1
'''
Learning Pytthon: Open a blank file in your text editor and write a few
lines summarizing what you've learned about Python so far. Start  each lime
with the phrase In Python you can ... Save the file as learning_python.txt in the
same directory as your exercises from this chapter. Write a program that reads 
the file and prints what you wrote three times. Print the contents once by reading
in the entire file, once by looping over the file object, and once by storing
the lines in a list and then working them outside the with block.
'''

filename = "learning_python.txt"

# Version one
with open(filename) as file_object:
	text = file_object.read()
	print(text)

# Version two
with open(filename) as file_object:
	for line in file_object:
		print(line)


# Version three
with open(filename) as file_object:
	code_text = file_object.readlines()

for lines in code_text:
	print(lines)