import argparse
import urllib3
from bs4 import BeautifulSoup

parser = argparse.ArgumentParser(description='Parse the bookshelf of Patrick Collison')
parser.add_argument('--file', default='collison.html')
args = parser.parse_args()

categories = {
        'blue': 'a',
        'teal': 'i', # substantially above average
        'green': 'b' # particularly great!
        }

with open(args.file) as f:
    soup = BeautifulSoup(f, 'html.parser')

# only get the ones with external urls
all_titles = list(filter(lambda x: x.a.get('href', '')[:4] == 'http', soup.find_all('li')))

for category, ident in categories.items():
    filtered_titles = list(filter(lambda x: x.next_element.name == ident, all_titles))
    titles = [x.text for x in filtered_titles]
    file_name = category + '.txt'

    with open(file_name, 'w') as wf:
        wf.write('\n'.join(titles))

