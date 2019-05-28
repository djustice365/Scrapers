from argparse import ArgumentParser
from enum import Enum
from ComicScraper.Core.ComicScraper import ComicScraper
from MovieScraper.MovieScraper import MovieScraper
from TVScraper.TVScraper import TVScraper

class ScraperType(Enum):
    comic = ComicScraper(True, "opm", "mha", "sds", "gs", "dbs")
    movie = MovieScraper(True, "test")
    tv = TVScraper(True, "test")


def main():
    args = parse_args()
    ScraperType[args.scraper].value.scrape()


def parse_args():
    parser = ArgumentParser(description='Scrapes the web')
    scrapers = ['comic', 'movie', 'tv']
    parser.add_argument('-s', '--scraper', choices=scrapers, required=True, help='comic | movie | tv')
    return parser.parse_args()


#test_scrape = ComicScraper(True, "opm", "mha", "sds", "gs", "dbs")

if __name__ == '__main__':
    main()