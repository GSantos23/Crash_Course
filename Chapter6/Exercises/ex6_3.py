# Exercise 6.3
"""
6-3. Glossary: A Python dictionary can be used to model an actual dictionary.
However, to avoid confusion, let’s call it a glossary.
	• Think of five programming words you’ve learned about in the previous
	chapters. Use these words as the keys in your glossary, and store their
	meanings as values.
	• Print each word and its meaning as neatly formatted output. You might
	print the word followed by a colon and then its meaning, or print the word
	on one line and then print its meaning indented on a second line. Use the
	newline character ( \n ) to insert a blank line between each word-meaning
	pair in your output.
"""

glossary = {
	'Dictionary': 'A collection of key-value pairs\n',
	'Tuples': 'A list of items that cannot change\n',
	'Lookup_Table': 'Array of data to map input values to output values\n',
	'List_Comprehension': 'Combination of a for loop and list append\n',
	'Simultaneous_Assigment': 'Alternative form of assigment statement\n'
}

print(glossary['Dictionary'])
print(glossary['Tuples'])
print(glossary['Lookup_Table'])
print(glossary['List_Comprehension'])
print(glossary['Simultaneous_Assigment'])