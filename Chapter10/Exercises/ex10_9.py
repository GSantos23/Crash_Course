# Exercise 10.9
'''
10-9. Silent Cats and Dogs: Modify your except block in Exercise 10-8 to fail
silently if either file is missing.
'''
def read_file(file_name):
	"""Function to read files"""
	try:
		with open(file_name) as f_obj:
			contex = f_obj.read()
	except FileNotFoundError:
		pass
	else:
		print(contex)

filename = ['cats.txt', 'dogfs.txt']
for archive in filename:
	read_file(archive)