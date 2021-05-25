import argparse
import urllib3

from bs4 import BeautifulSoup

def parse(url: str, source: str) -> str:
    """
    Parse the list of titles from a URL.
    Available sources are 'collison', 'goodreads'
    """
    http = urllib3.PoolManager()
    data = http.request('GET', url).data
    soup = BeautifulSoup(data, 'html.parser')
    if source == 'collison':
        return collison(soup)
    if source == 'goodreads':
        return goodreads(soup)
    raise ValueError('Unknown book list source!')


def collison(soup, include={'teal', 'green'}):
    """
    We can also filter books by the colour coding.
    Ignore the blue-coded books by default.
    """
    categories = {
            'blue': 'a',
            'teal': 'i', # substantially above average
            'green': 'b' # particularly great!
            }

    tags = list(filter(lambda x: x.a.get('href', '')[:4] == 'http', soup.find_all('li')))
    titles = []

    for category, ident in categories.items():
        if category in include:
            filtered_tags = list(filter(lambda x: x.next_element.name == ident, tags))
            titles.extend([x.text for x in filtered_tags])

    return set(titles)

def goodreads(soup):
    """
    Read the book titles from the image alt text.
    """
    titles = list(
        map(
            lambda x: x.img.get('alt'),
            filter(
                lambda x: x.next_element.name == 'img' and '/book/show/' in x.get('href', ''), 
                soup.find_all('a')
            )
        )
    )
    return set(titles)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Parse titles from Goodreads or the bookshelf of Patrick Collison')
    parser.add_argument('--url', help='URL of bookshelf', required=True)
    parser.add_argument('--source', help='Either "collison" or "goodreads"', required=True)
    parser.add_argument('--file', help='Name of the results file', required=False)
    args = parser.parse_args()
    
    titles = parse(args.url, args.source)
    if args.file:
        with open(args.file, 'w') as f:
            f.write('\n'.join(titles))