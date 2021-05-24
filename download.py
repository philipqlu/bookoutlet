import argparse
import urllib3

parser = argparse.ArgumentParser(description='Download a webpage.')
parser.add_argument('--url', default='https://patrickcollison.com/bookshelf')
parser.add_argument('--file', default='collison.html')
args = parser.parse_args()
http = urllib3.PoolManager()
r = http.request('GET', args.url)
with open(args.file, 'wb') as wf:
    wf.write(r.data)
