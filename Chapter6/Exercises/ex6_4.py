# Exercise 6.4
"""
Glossary 2: Now that you know how to loop through a dictionary, clean
up the code from Exercise 6-3 (page 102) by replacing your series of print
statements with a loop that runs through the dictionary’s keys and values.
When you’re sure that your loop works, add five more Python terms to your
glossary. When you run your program again, these new words and meanings
should automatically be included in the output.
"""

glossary = {
	'Dictionary': 'A collection of key-value pairs\n',
	'Tuples': 'A list of items that cannot change\n',
	'Lookup_Table': 'Array of data to map input values to output values\n',
	'List_Comprehension': 'Combination of a for loop and list append\n',
	'Simultaneous_Assigment': 'Alternative form of assigment statement\n',
	'String': 'A series of characters\n',
	'Float': 'Any number with a decimal point\n',
	'Slice': 'Specific group of items on a list\n',
	'Conditional_Test': 'An expression that can be True or False\n',
	'Boolean_Expression': 'Another name for conditional test'
}


for terms, definitions in glossary.items():
	print(terms)
	print(definitions)