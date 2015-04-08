__author__ = 'William'

import unittest

from  web_cache.WebCache import WebCache
from web_scraper.WebScraper import WebScraper


class TestCache(unittest.TestCase):
    def setUp(self):
        self.dc = WebCache()
        self.scraper = WebScraper()
    def test_add_page(self):
        url="http://www.weatherbase.com/weather/weather.php3?s=27730&cityname=Slough-England-United-Kingdom"
        source = self.scraper.get_source(url=url)
        self.dc.add_page(url=url,source=source)
        page = self.dc.get_page(url=url)
        self.assertEqual(len(source),len(page.source))
    def test_get_nonexistant_page(self):
        page = self.dc.get_page(url="http://asasdasdasd.com")
        self.assertFalse(page)



if __name__ == '__main__':
    unittest.main()
