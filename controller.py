from argparse import ArgumentParser
from enum import Enum
from ComicScraper.Core.ComicScraper import ComicScraper
from MovieScraper.MovieScraper import MovieScraper
from TVScraper.TVScraper import TVScraper

class ScraperType(Enum):
    comic = ComicScraper(False, "opm", "mha", "sds", "gs", "dbs")
    movie = MovieScraper(False)
    tv = TVScraper(True, "test")


def main():
    args = parse_args()
    ScraperType[args.scraper].value.scrape(args.args)


def parse_args():
    parser = ArgumentParser(description='Scrapes the web')
    scrapers = ['comic', 'movie', 'tv']
    parser.add_argument('-s', '--scraper', choices=scrapers, required=True, help='comic | movie | tv')
    parser.add_argument('-a', '--args', required=False, help='Comma delimited list that you would like to pass to the Scraper. No spaces inbetween commas and args')

    parsed_args = parser.parse_args()

    # Validate certain args
    if parsed_args.scraper == 'movie' and parsed_args.args is None:
        parser.error("Movie scraper requires additional arguments passed with -a/--args to use as search keywords")

    return parsed_args


if __name__ == '__main__':
    main()