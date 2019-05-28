from ScraperUtils.ScraperUtils import Utils
import re

class MovieScraper(Utils):
    def __init__(self, debug, *args):
        self.debug = debug
        self.base = "https://www6.putlockertv.to/search?keyword="


    def scrape(self, args):
        for arg in args.split(","):
            print("Starting movie scrape for: " + arg)
            soup = self.create_soup_from_url(self.base + arg.replace(" ", "+"))
            self.log("Searching url: " + self.base + arg.replace(" ", "+"))
            elements = self.find_all('div', soup)
            for element in elements:
                str = element.get("class")
                if str is not None:
                    if "item" in str:
                        anchors = element.find_all('a')
                        str_pattern = ".*" + arg.upper() + ".*"
                        pattern = re.compile(str_pattern)
                        if pattern.match(anchors[1].text.upper()) is not None:
                            print("--")
                            print("--")
                            print("Found match for keywords \"" + arg + "\": " + anchors[1].text)
                            print("--")
                            print("--")



