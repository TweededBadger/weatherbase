import unittest
from datetime import date
from weather_history.WeatherHistory import WeatherHistory
from weather_history.DataObjects import WeatherObject

class TestWeatherHistory(unittest.TestCase):
    def setUp(self):
        self.wr = WeatherHistory()

    def test_get_city_id(self):
        country_code = "TR"
        city_name = "Nusaybin"
        city_code = self.wr.get_city_id(country_code,city_name)
        self.assertEqual(city_code, 172752)

    def test_get_date_average_data(self):
        city_code = 172752
        today = date.today()
        average_data = self.wr.get_average_data(city_code,today)
        print average_data
        self.assertIsInstance(average_data,WeatherObject)
        self.assertIsNotNone(average_data)

    def test_get_date_daily_data(self):
        # city_code = 172752
        city_code = 67730
        d = date(2012, 6, 24)
        day_data = self.wr.get_day_data(city_code,d)
        print day_data
        self.assertIsInstance(day_data,WeatherObject)
        self.assertIsNotNone(day_data)




if __name__ == '__main__':
    unittest.main()
