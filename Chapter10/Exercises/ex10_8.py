# Exercise 10.8
'''
Cats and Dogs: Make two files, cats.txt and dogs.txt. Store at least three
names of cats in the first file and three names of dogs in the second file. Write
a program that tries to read these files and print the contents of the file to the
screen. Wrap your code in a try-except block to catch the FileNotFound error,
and print a friendly message if a file is missing. Move one of the files to a dif-
ferent location on your system, and make sure the code in the except block
executes properly.
'''
#filename = ['cats.txt', 'dogs.txt']
'''
try:
	with open(filename_1) as f_obj:
		contex = f_obj.read()
except FileNotFoundError:
	print("File does not exist. Sorry")
'''
'''
with open(filename_1) as f_obj:
	contex = f_obj.read()
	print(contex)


'''
def read_file(file_name):
	"""Function to read files"""
	try:
		with open(file_name) as f_obj:
			contex = f_obj.read()
	except FileNotFoundError:
		print("File " + file_name + " does not exist. Sorry")
	else:
		print(contex)

filename = ['cats.txt', 'dogs.txt']
for archive in filename:
	read_file(archive)