from enum import Enum
from ScraperUtils.ScraperUtils import Utils

class URL(Enum):
    opm = "https://manganelo.com/manga/read_one_punch_man_manga_online_free3"
    sds = "https://manganelo.com/manga/read_nanatsu_no_taizai_manga_online_free"
    gs  = "https://mangakakalot.com/manga/hgj2047065412"
    mha = "https://manganelo.com/manga/read_boku_no_hero_academia_manga"
    dbs = "https://manganelo.com/manga/dragon_ball_super"


class ComicScraper(Utils):
    def __init__(self, debug):
        self.debug = debug


    def scrape(self, args):
        for arg in args.split(","):
            print("Starting comic scrape for: " + arg)
            soup = self.create_soup_from_url(URL[arg].value)
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

