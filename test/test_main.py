import unittest
from datetime import date, datetime
from weather_history.WeatherHistory import WeatherHistory
from weather_history.DataObjects import WeatherObject

class TestWeatherHistory(unittest.TestCase):
    def setUp(self):
        self.wr = WeatherHistory()

    def test_get_city_id(self):
        country_code = "GB"
        city_name = "London"
        city_code = self.wr.get_city_id(country_code,city_name)
        self.assertEqual(city_code, 67730)

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

    def test_weather_data_difference(self):
        city_code = 67730
        test_date = date(2012, 6, 24)
        today_data = self.wr.get_day_data(city_code,test_date)
        today_average_data = self.wr.get_average_data(city_code,test_date)
        difference_data = today_data.difference(today_average_data)
        self.assertIsInstance(difference_data,WeatherObject)
        self.assertIsNotNone(difference_data)
        self.assertIsInstance(difference_data.dewpoint,float)
        self.assertIsInstance(difference_data.temperature,float)
        self.assertIsInstance(difference_data.barometer,float)
        self.assertIsInstance(difference_data.wind_speed,float)
        self.assertIsInstance(difference_data.humidity,float)

    def test_get_hourly_data(self):
        city_code = 51730
        test_date_time = datetime(2014,4,20,12,0,0)
        hour_data = self.wr.get_hour_data(city_code,test_date_time)
        print hour_data

        self.assertIsInstance(hour_data,WeatherObject)
        self.assertIsNotNone(hour_data)
        self.assertIsInstance(hour_data.dewpoint,float)
        self.assertIsInstance(hour_data.temperature,float)
        self.assertIsInstance(hour_data.barometer,float)
        self.assertIsInstance(hour_data.wind_speed,float)
        self.assertIsInstance(hour_data.humidity,float)





if __name__ == '__main__':
    unittest.main()
