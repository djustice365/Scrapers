from ScraperUtils.ScraperUtils import Utils

class MovieScraper(Utils):
    def __init__(self, debug, *args):
        self.debug = debug
        self.args = args


    def scrape(self):
        print("MOVIE SCRAPER WOO")

