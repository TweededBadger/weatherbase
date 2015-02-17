from bs4 import BeautifulSoup
import lxml.html
import re
from weather_history import helpers
from weather_history.DataObjects import WeatherObject

from web_scraper.WebScraper import WebScraper


class WeatherHistory():
    def __init__(self):
        self.scraper = WebScraper()

    def get_city_id(self, country_code, city_name):
        url = "http://www.weatherbase.com/weather/city.php3?c=" + country_code
        tree = lxml.html.fromstring(self.scraper.get_source(url))
        cities = tree.find_class("redglow")
        for element in cities:
            if element.text.lower() == city_name.lower():
                code = re.findall("\?s=(.*)\&",element.attrib['href'])[0]
                return int(code)


    #http://www.weatherbase.com/weather/weatherdaily.php3?s=172752&month=02&theday=09&units=metric
    #http://www.weatherbase.com/weather/weatherhourly.php3?s=172752&date=2010-02-17&set=metric

    def get_average_data(self, city_code, today,units='metric'):

        url = "http://www.weatherbase.com/weather/weatherdaily.php3?s={0}&month={1}&theday={2}&units={3}"\
            .format(city_code,today.month,today.day,units)
        tree = lxml.html.fromstring(self.scraper.get_source(url))
        temp_data = helpers.get_table_data(tree,"Temperature",1)
        dewpoint_data = helpers.get_table_data(tree,"Dewpoint",1)
        humidity_data = helpers.get_table_data(tree,"Humidity",1)
        barometer_data = helpers.get_table_data(tree,"Barometer",1)
        wind_speed_data = helpers.get_table_data(tree,"Wind Speed",1)
        precipitation_data = helpers.get_table_data(tree,"Precipitation",1)
        return_object = WeatherObject(
            temp_data,dewpoint_data,humidity_data,barometer_data,wind_speed_data,precipitation_data)
        return return_object

    def get_day_data(self, city_code, d, units='metric'):
        url = "http://www.weatherbase.com/weather/weatherhourly.php3?s={0}&date={1}-{2}-{3}&set={4}"\
            .format(city_code,d.year,d.month,d.day,units)
        print url
        tree = lxml.html.fromstring(self.scraper.get_source(url))
        temp_data = helpers.get_table_data(tree,"Temperature",1)
        dewpoint_data = helpers.get_table_data(tree,"Dewpoint",1)
        humidity_data = helpers.get_table_data(tree,"Humidity",1)
        barometer_data = helpers.get_table_data(tree,"Barometer",1)
        wind_speed_data = helpers.get_table_data(tree,"Wind Speed",1)
        precipitation_data = helpers.get_table_data(tree,"Precipitation",1)
        return_object = WeatherObject(
            temp_data,dewpoint_data,humidity_data,barometer_data,wind_speed_data,precipitation_data)
        return return_object