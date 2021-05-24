# bookoutlet
Find books on bookoutlet.ca.

I decided to make this after perusing Patrick Collison's bookshelf and trying to see which books were available at my favourite discount book store.

After a bunch of unsuccessful searches, I decided to [automate](https://xkcd.com/1319/) the task and here we are, several hours later...

## How to use
Set-up (Python >= 3.6)
```
pip install -r requirements.txt
```

Download a page (eg. https://patrickcollison.com/bookshelf)
```
python download.py --url https://patrickcollison.com/bookshelf
```

Get the list of titles (broken down by colour code)
```
python collison.py
```

Search for the list of titles on bookoutlet, eg. all of the light blue titles
```
python search.py teal.txt
```
