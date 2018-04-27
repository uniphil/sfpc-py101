from collections import Counter
import nltk
from nltk.book import text1, text2

file = open('manifesto.txt','rU')
raw_manifesto = file.read().decode('utf-8')

tokens = nltk.word_tokenize(raw_manifesto)
text = nltk.Text(tokens)

print Counter(tokens)
distribution = nltk.FreqDist(text)
distribution.most_common(50)
distribution.plot()

text1.concordance("galactic")  # No galactic whales :'(

print "\n\n"
text1.similar("monstrous")

print "\n\n"
text2.similar("monstrous")
