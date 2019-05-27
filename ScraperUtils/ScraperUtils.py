from bs4 import BeautifulSoup
import requests

class Utils:
    def get_source(self, url):
        print("Retrieving source for " + url)
        return requests.get(url).text


    def convert_to_soup(self, source):
        print("Converting source to soup object")
        return BeautifulSoup(source, 'lxml')


    def create_soup_from_url(self, url):
        return self.convert_to_soup(self.get_source(url))


    def find_all(self, element, soup):
        print("Finding all elements for: " + element)
        return soup.find_all(element)


    def get_title_string(self, soup):
        return soup.get('title')

