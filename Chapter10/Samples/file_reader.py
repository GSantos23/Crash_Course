# Sample 10.1

# Version 1
'''
with open('pi_digits.txt') as file_object:
	contents = file_object.read()
	#print(contents)
	print(contents.rstrip())	# To remove extra blank line
'''

# Version 2
'''
filename = 'pi_digits.txt'

with open(filename) as file_object:
	for line in file_object:
		print(line.rstrip())
'''

# Version 3
filename = 'pi_digits.txt'

with open(filename) as file_object:
	lines = file_object.readlines()		# Return a list of lines

for line in lines:
	print(line.rstrip())