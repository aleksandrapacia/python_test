import unittest 
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """Tests for AnonymousSurvey"""

    def setUp(self):
        question = 'What is your language?'
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['english', 'italian', 'polish']

    def test_store_single_response(self):
        """Checks whether single answer is properly stored"""
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)
        
        

    def test_store_three_responses(self):
        """Checks whether three given answers are correctly stored"""

        for response in self.responses:
            self.my_survey.store_response(response)
            
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)

if __name__ == '__main__':
    unittest.main()