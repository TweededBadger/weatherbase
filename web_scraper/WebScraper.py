from bs4 import BeautifulSoup
import urllib2
from selenium import webdriver
from web_cache.WebCache import WebCache

class WebScraper():
    def __init__(self):
        self.web_cache = WebCache()

    def get_source(self,url,method="urllib2"):
        page = self.web_cache.get_page(url=url)
        if page == None:
            if method == "selinium":
                self.browser = webdriver.Chrome()
                self.browser.implicitly_wait(1)
                self.browser.get(url)
                html_source = self.browser.page_source
                self.web_cache.add_page(url=url,source=html_source)
                self.browser.quit()
                return html_source
            elif "urllib2":
                req = urllib2.Request(url, headers={ 'User-Agent': 'Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11' })
                html_source = urllib2.urlopen(req).read()
                self.web_cache.add_page(url=url,source=html_source.decode('utf-8'))
                return html_source
                # self.dc.add_page(url=url,source=page)
        else:
            return page.source