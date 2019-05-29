# Scrapers

Scrapes for (specific) comics, tv, or movies on specific websites.

## How to use
### Windows
python controller.py -s {comic|tv|movie} -a "{arguments}"

### Linux/Mac
./controller.py -s {comic|tv|movie} -a "{arguments}"
  
-a requires double quotes
if using multiple arguments, -a requires a comma delimited list with no spaces before or after the argument. For example:

controller.py -s movie -a "test1,test2,test3"

However, spaces are allowed in-between words i.e -a "infinity war"
  
## Comic Scraper
Currently hard coded to speciic comics that I am keeping up with.
arguments is optional

Prints out the latest comic along with release date

## Movie Scraper
Uses arguments passed in as search keywords with a movie filter on a specific website.

Prints out any matching search results.

## TV Scraper
Uses arguments passed in as search keywords with a TV filter on a specific website.

Prints out any matching search results.

TODO: Check the latest season and print out latest episode
