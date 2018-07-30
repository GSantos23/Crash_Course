# Exercise 11.1
'''
City, Country: Write a function that accepts two parameters: a city name
and a country name. The function should return a single string of the form
City, Country, such as Santiago, Chile. Store the function in a module
called city_function.py
	Create a file called test_cities.py that tests the function you just
wrote (remember that you need to import unittest and the function you want
to test). Write a method called test_city_country() to verify that calling
your function with values such as 'santiago' and 'chile' results in the
correct string. Run the test_cities.py, and make sure test_city_country()
passes.
'''
import unittest
from city_function import city_coutry_names

class CityAndCountry(unittest.TestCase):
	"""Test for city_function.py"""
	def test_city_country(self):
		"""Expectect output City, Country"""
		string_names = city_coutry_names('santiago', 'chile')
		self.assertEqual(string_names, 'Santiago, Chile')


	def test_city_country_populaton(self):
		"""Expect >> city, Country, population xxx"""
		string_names = city_coutry_names('santiago', 'chile', 500000)
		self.assertEqual(string_names, 'Santiago, Chile - Population: 500000')



# To run the test when you execute python script
unittest.main()
