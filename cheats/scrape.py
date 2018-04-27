from bs4 import BeautifulSoup

import urllib2 
url = urllib2.urlopen("http://martinesyms.com/the-mundane-afrofuturist-manifesto/")

content = url.read()

soup = BeautifulSoup(content)
manifesto = soup.find("div", { "class" : "entry-content" })

for line in manifesto.children:
    if line.name == 'p':
        print line.text


