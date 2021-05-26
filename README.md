# bookoutlet
Find out what books are available at your local library or discount book store.

## Supported sources
- Goodreads book lists (eg. [memoirs](https://www.goodreads.com/genres/memoir))
- Radical reads (eg. Jon Hamm's [favorite books](https://radicalreads.com/jon-hamm-favorite-books/))
- Favobooks (eg. Larry Page's [favorite books](http://favobooks.com/enterpreneurs/110-Larry-Page-books-that-stimulate-your-mind.html))
- Patrick Collison's [bookshelf](https://patrickcollison.com/bookshelf)

## Supported stores/libraries
- [Book Outlet](https://www.bookoutlet.ca)
- [Ottawa Public Library](https://biblioottawalibrary.ca/en)
- [Toronto Public Library](https://www.torontopubliclibrary.ca/)

## How to use
Set-up (Python >= 3.6)
```
pip install -r requirements.txt
```

Usage:
```
usage: main.py [-h] --url URL --source SOURCE --store STORE [--file FILE]

Search for books on bookoutlet

optional arguments:
  -h, --help       show this help message and exit
  --url URL        URL of bookshelf
  --source SOURCE  Name of source for book list ("collison", "goodreads", "radicalreads", "favobooks")
  --store STORE    Name of store ("bookoutlet", "opl", "tpl")
  --file FILE      Name of the results file
```

The program will parse the book titles from the input URL and source, search for them on the specified store, and write the results to a file.

Example:
```
python src/bookoutlet/main.py --url https://www.goodreads.com/genres/memoir --source goodreads --store bookoutlet --file gr_memoir.txt
```
