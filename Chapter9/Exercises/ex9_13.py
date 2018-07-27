# Exercise 9.13
'''
OrderedDict Rewrite: Start with Exercise 6-4 (page 108), where you
used a standard dictionary to represent a glossary. Rewrite the program using
the OrderedDict class and make sure the order of the output matches the order
in which key-value pairs were added to the dictionary.
'''
from collections import OrderedDict

glossary = OrderedDict()

glossary['Dictionary'] = 'A collection of key-value pairs\n'
glossary['Tuples'] = 'A list of items that cannot change\n'
glossary['Lookup Table'] = 'Array of data to map input values to output values\n'
glossary['List Comprehension'] = 'Combination of a for loop and list append\n'
glossary['Simultaneous Assigment'] = 'Alternative form of assigment statement\n'
glossary['String'] = 'A series of characters\n'
glossary['Float'] = 'Any number with a decimal point\n'
glossary['Slice'] = 'Specific group of items on a list\n'
glossary['Conditional_Test'] = 'An expression that can be True or False\n'
glossary['Boolean_Expression'] = 'Another name for conditional test'


for terms, definitions in glossary.items():
	print(terms)
	print(definitions)