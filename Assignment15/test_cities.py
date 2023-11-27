import unittest
from city_functions import city_country

class CitiesTestCase(unittest.TestCase):

  def test_city_country(self):
      formatted_name = city_country('Saratoga', 'New York')
      self.assertEqual(formatted_name, 'Saratoga, New York')

  def test_city_country_population(self):
      formatted_name = city_country('Saratoga, New York', populations = 28301)
      self.assertEqual(formatted_name, 'Saratoga, New York - population 28301')

if __name__ == '__main__':
  unittest.main()
