import argparse
from typing import List
from urllib.parse import urlencode
import cloudscraper
from bs4 import BeautifulSoup
from fuzzywuzzy import fuzz, process

class Scraper:
    def __init__(self, base_url: str, titles: List[str], fuzz_thresh: float = 0.92):
        self.base_url = base_url
        self.titles = titles
        self.scraper = cloudscraper.CloudScraper()
        self.fuzz_thresh = fuzz_thresh

    def parse_titles(self, response: str) -> List[str]:
        soup = BeautifulSoup(response, 'html.parser')
        titles = soup.find_all('p')
        titles = list(map(lambda x: x.a.get('data-text'), filter(lambda x: 'title' in x.get('class', []), titles)))
        print("{} titles found".format(len(titles)))
        return titles

    def search(self, query: str) -> str:
        print("Searching for: {}".format(query))
        words = query.split()
        # Long search queries don't work well
        if len(words) > 8:
            query = ' '.join(words[:8])
            print("Truncating query to: {}".format(query))
        encoded_query = urlencode({'qf': 'All', 'q': query})
        url = self.base_url + encoded_query
        return self.scraper.get(url).text

    def find_title(self, title: str, titles: List[str]) -> bool:
        """
        Fuzzy string match the title against a list of titles.
        """
        if titles:
            choice, ratio = process.extractOne(title.lower(), list(map(lambda x: x.lower(), titles)), scorer=fuzz.ratio)
            found = ratio >= self.fuzz_thresh
        else:
            choice = "N/A"
            found = False
        print("'{}' was {}found".format(title, "" if found else "not "))
        print("Closest match: {}".format(choice))
        return found

    def search_all_titles(self):
        found = 0
        for t in self.titles:
            # Search and check if the title was found
            print("***")
            r = self.search(t)
            r_titles = self.parse_titles(r)
            if r_titles and self.find_title(t, r_titles):
                found += 1
            print("***")

        print("{} titles found out of {}".format(found, len(self.titles)))

if __name__ == "__main__":
    # read list of titles from txt file
    parser = argparse.ArgumentParser(description = 'Search a list of titles from a file')
    parser.add_argument('file', help='Text file with list of books to search')
    args = parser.parse_args()
    with open(args.file) as f:
        titles = [l.strip() for l in f]

    # perform searches
    scraper = Scraper('https://bookoutlet.ca/Store/Search?', titles)
    scraper.search_all_titles()

