# Hello! 👻

Today we're going to talk a bit about text scraping, manipulation, and analysis in Python.

Workshop by [Phil](https://github.com/uniphil), [Riley](https://github.com/rileyjshaw), and [Yeli](https://github.com/oa495).

## Tools

### [Sublime Text](https://www.sublimetext.com/)

If you don't have a favorite text editor already, download [Sublime Text](https://www.sublimetext.com/). You _can_ use Xcode for these exercises if you're used to it, but we recommend Sublime since it's simpler and less clunky.

### [pip](https://pip.pypa.io/en/stable/installing/)

Open up a terminal and run this command to download the installer:

```bash
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py`
```

then to install,

```bash
sudo python get-pip.py
```

### [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)

Once we've got `pip` set up, we can install Beautiful Soup with `pip install beautifulsoup4`.

### [Natural Language Toolkit (NLTK)](http://www.nltk.org/)

Once we've got `pip` set up, we can install NLTK with `pip install nltk`. NLTK is a suite of text processing libraries for Python that lets us analyze text in some really interesting and powerful ways. For the intro exercises, we'll work through part of the [NLTK Book](http://www.nltk.org/book/). It's a great resource, check it out!!

NLTK comes loaded with a bunch of [corpora and trained models](http://www.nltk.org/nltk_data/). We're going to use some of them, so in your Python REPL type:

```
import nltk
nltk.download()
```

If it looks like nothing happened, check if a new window popped open in the background. We want to download `book` under the "Collections" tab.
