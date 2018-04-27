import random
import itertools

# JOKE TEMPLATE!
# Recipe: part_1 + part_2 + part_3 = joke.

part_1 = [
	"Knock knock!",
	"Your momma",
	"Someone walks into a bar",
	"What do you call a",
	"Why did the",
]

momma_adjectives = ["pretty", "loving", "smart", "horrible"]
part_2 = [
	"WHO IS THERE!?",
	"is so {} that".format(random.choice(momma_adjectives)),
	"with another person too and also one other person too",
	"chicken cross the road???!?!?",
	"penguin in a blender",
	"foiawroiahsdfh",
]

part_3 = [
	"and orders a drink",
	"orange you glad i didn't say banana?",
	"to get to the other side",
	"and it was actually a shark",
	"potato farmer",
	"that's so boring, I'd rather be a suitcase!!",
	"I DON'T KNOW",
]

print "{} {} {}!!!!!!!!!!!!!!!!!".format(
	random.choice(part_1),
	random.choice(part_2),
	random.choice(part_3))

all_jokes = list(itertools.product(part_1, part_2, part_3))
random.shuffle(all_jokes)
for a, b, c in all_jokes:
	print('{} {} {}!!!!!!!!'.format(a, b, c))
