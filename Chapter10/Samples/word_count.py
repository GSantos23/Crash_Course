# Sample 10.6
def count_words(filename):
	"""Count the approximate number of words in a file"""
	try:
		with open(filename) as f_obj:
			contents = f_obj.read()
	except FileNotFoundError:
		#msg = "Sorry, the file " + filename + " does not exist."
		#print(msg)
		pass
	else:
		# Count the approximate number of words in the file
		words = contents.split()
		num_word = len(words)
		print("The file " + filename + " has about " + str(num_word) + 
			" words.")

# Version 1
#filename = 'alice.txt'
#count_words(filename)

# Version 2
filenames = ['alice.txt', 'siddharta.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
	count_words(filename)
