# quotes
a = 'some string'
b = "some string"
print a == b  # True

# escaping
print 'it\'s a wonderful world'
print "she said, \"what's up?\""

# formatting/interpolation
name = 'phil'
print 'hello {}'.format('phil')
import time
print 'hello {name} the second in binary is {second:b}'.format(name='phil', second=int(time.time()))

# multi-line
story = """The Robot Who Cried Wolf

Once upon a time there was a young robot, who
"""
print story

# fun methods
print len('hello')  # 5

for letter in 'hello world':
    print letter.upper()

print 'e' in 'hello'  # True

print sorted('hello')  # ['e', 'h', 'l', 'l', 'o']

for word in 'HELLO world'.split():
    print word.lower()

print '     s p a c e d    '.strip()

print '     s p a c e d    '.replace(' ', '_')


# weird built-in tools
from collections import Counter
counts = Counter('there once was a droid from saskatchewan')
print counts
print counts.most_common(2)
