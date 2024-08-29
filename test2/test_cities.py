import unittest  
from cities_countries import capital_country

class TestCities(unittest.TestCase):
    def test_city_country(self):
        """Tests for cities_countries.py"""
        formatted_city_country = capital_country('santiago', 'chile', '5000')

        self.assertEqual(formatted_city_country, 'Santiago, Chile - Population 5000')


if __name__ == '__main__':
    unittest.main()

