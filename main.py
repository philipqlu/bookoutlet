import argparse

from parser import parse
from search import Scraper

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Search for books on bookoutlet')
    parser.add_argument('--url', help='URL of bookshelf', required=True)
    parser.add_argument('--source', help='Either "collison" or "goodreads"', required=True)
    parser.add_argument('--file', help='Name of the results file', required=False)
    args = parser.parse_args()

    # download and parse the webpage's book titles
    books = parse(args.url, args.source)

    # search each book title
    scraper = Scraper(books)
    found = scraper.search_all_titles()

    # write found titles to disk
    if args.file:
        with open('found-' + args.file, 'w') as f:
            f.write('\n'.join(found))
