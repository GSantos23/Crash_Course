# Sample 11.5
import unittest
from survey import AnonymusSurvey

class TestAnonymusSurvey(unittest.TestCase):
	"""Tests for the class AnonymusSurvey"""

	def setUp(self):
		"""
		Create a survey and a set of responses for use in all test methods.
		"""
		question = "What language did you first learn to speak?"
		self.my_survey = AnonymusSurvey(question)
		self.responses = ['English', 'Spanish', 'Mandarin']

	def test_score_single_response(self):
		"""Test that a single response  is stored properly"""
		self.my_survey.store_response(self.responses[0])
		self.assertIn('English', self.my_survey.responses)

	def test_score_three_responses(self):
		"""Test that three individual responses are stored properly."""		
		for response in self.responses:
			self.my_survey.store_response(response)

		for response in self.responses:
			self.assertIn(response, self.my_survey.responses)


unittest.main()