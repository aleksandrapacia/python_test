import unittest  

from test1.names import get_formatted
# create a class named NameTestCase with parameter unittest.TestCase so that we inherit the TestCase class from unittest package
class NameTestCase(unittest.TestCase):
    def test_first_last_name(self):
        formatted_name = get_formatted('janis' ,'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

if __name__ == '__main__':
    unittest.main()


