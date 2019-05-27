from enum import Enum
from ScraperUtils.ScraperUtils import Utils

class URL(Enum):
    opm = "https://manganelo.com/manga/read_one_punch_man_manga_online_free3"


class ComicScraper(Utils):
    def __init__(self, *args):
        for arg in args:
            self.scrape(URL[arg].value)
        pass

    def scrape(self, url):
        #TODO: Iterate over a list of sites to scrape, print if there is a new one
        soup = self.create_soup_from_url(url)
        elements = self.find_all('div', soup)
        count = 0
        for element in elements:
            if count > 1:
                break
            str = element.get("class")
            if str is not None:
                if "row" in str:
                    if count == 1:
                        spans = self.find_all('span', element)
                        print("--")
                        print("--")
                        print(self.get_title_string(spans[0].find('a')) + " | " + self.get_title_string(spans[2]))
                        print("--")
                        print("--")
                    count += 1

