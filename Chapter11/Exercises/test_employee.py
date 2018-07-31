# Test case for class
import unittest
from employee_pay import Employee

class TestEmployeeInfo(unittest.TestCase):
	"""Test employee_pay.py."""
	def setUp(self):
		"""
		Create variable for both cases
		"""
		first_name = 'Gerson'
		last_name = 'Santos'
		annual_salary = 5000
		self.gerson = Employee(first_name, last_name, annual_salary)

	def test_default_raise(self):
		"""
		Increase salary, $5000
		"""
		self.gerson.give_raise()
		self.assertEqual(self.gerson.annual, 10000)

	def test_another_raise(self):
		"""
		Increase salary, using other raise value
		"""
		self.gerson.give_raise(9000)
		self.assertEqual(self.gerson.annual, 14000)
		

unittest.main()
