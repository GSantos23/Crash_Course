# Exercise 11.13
'''
Employee: Write a class called Employee . The __init__() method should
take in a first name, a last name, and an annual salary, and store each of 
these as attributes. Write a method called give_raise() that adds $5000 to 
the annual salary by default but also accepts a different raise amount.
Write a test case for Employee . Write two test methods, test_give_
default_raise() and test_give_custom_raise() . Use the setUp() method so
you don’t have to create a new employee instance in each test method. Run
your test case, and make sure both tests pass.
'''
class Employee():
	"""Collects employee data and annual salary,."""
	def __init__(self, first, last, annual):
		self.first = first.title()
		self.last = last.title()
		self.annual = annual

	def give_raise(self, raise_value=5000):
		"""Add $5000 to annual salary."""
		self.annual += raise_value
