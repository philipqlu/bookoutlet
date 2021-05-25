# bookoutlet
Find books on bookoutlet.ca.

I decided to make this after perusing Patrick Collison's bookshelf and trying to see which books were available at my favourite discount book store.

After a bunch of unsuccessful searches, I decided to [automate](https://xkcd.com/1319/) the task and here we are, several hours later...

## Supported sources:
- Patrick Collison's [bookshelf](https://patrickcollison.com/bookshelf)
- Any public Goodreads page with book previews (eg, [memoirs](https://www.goodreads.com/genres/memoir))

## How to use
Set-up (Python >= 3.6)
```
pip install -r requirements.txt
```

Usage:
```
usage: main.py [-h] --url URL --source SOURCE [--file FILE]

Search for books on bookoutlet

optional arguments:
  -h, --help       show this help message and exit
  --url URL        URL of bookshelf
  --source SOURCE  Either "collison" or "goodreads"
  --file FILE      Name of the results file
```

The program will parse the book titles from the input URL, search for them on bookoutlet, and write the results to a file.

Example:
```
python main.py --url https://www.goodreads.com/genres/memoir --source goodreads --file gr_memoir.txt
```
