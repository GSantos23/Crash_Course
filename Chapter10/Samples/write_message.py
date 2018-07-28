# Sample 10.3
filename = 'programming.txt'

'''
with open(filename, 'w') as file_object:
	file_object.write("I love programming.\n")
	file_object.write("I love creating games.\n")
'''
# Append anex new lines without deleting..
with open(filename, 'a') as file_object:
	file_object.write("I also love finding meaning in large databases.\n")
	file_object.write("I love creating apps that can run in a browser.\n")