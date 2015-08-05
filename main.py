from random import choice as swap
from adj import adjectives
from places import places
from verby import verbs
from nouns import nouns
from first import first_names
from last import last_names
import re


def fix(line):
    return re.sub(' a ([aeiouy])', r' an \1', line)

adj = adjectives
noun = ["man", "woman", "dog", "cat", "rabbit", "dude", "dudette", "developer", "muppet"] + nouns
verb = ["kicked", "ate", "fought", "gambled", "licked", "played", "tossed", "googled"] + verbs
con =["at", "in", "from", "with"]
pronoun = ["he", "she", "it", "they", "we"]
place = ["FanDuel", "Dumbiedykes", "Logic Now", "Skyscanner", "The BBC", "Edinburgh", "Glasgow", "Fort William"] + places

rand = adj + noun + verb

lim = [
    "There was a {ADJ} {NOUN} from {PLACE}",
    "Who {VERB} a {NOUN1} {CON} a {ADJ} {NOUN2}",
    "{PRO} {VERB} a {NOUN}",
    "{PRO} {VERB} a {NOUN}",
]

# RANDOMISER
lim[0]= lim[0].format(ADJ=swap(adj), NOUN=swap(noun), PLACE=swap(place))
lim[1] = lim[1].format(VERB=swap(verb), NOUN1=swap(noun), CON=swap(con), ADJ=swap(adj), NOUN2=swap(noun))
lim[2] = lim[2].format(PRO=swap(pronoun), VERB=swap(verb), NOUN=swap(noun))
lim[3] = lim[3].format(PRO=swap(pronoun), VERB=swap(verb), NOUN=swap(noun))


endings = [
    "But in the end it was all {}".format(swap(adj)),
    "But {PRO} ended up {ADJ} in a {NOUN}".format(PRO=swap(pronoun), ADJ=swap(adj), NOUN=swap(noun)),
    "So we all went off to {}".format(swap(place)),
    "and the {} was lost forever".format(swap(noun)),
    "And the {NOUN1} ran away with the {NOUN2}".format(NOUN1=swap(noun), NOUN2 = swap(noun)),
    "and {PRO} finally {VERB} the {NOUN}".format(PRO=swap(pronoun), VERB=swap(verb), NOUN=swap(noun))
]

titles = [
    "Ode to a {}".format(swap(noun)),
    "The {ADJ} {NOUN}'s lament".format(ADJ=swap(adj), NOUN=swap(noun)),
    "On the way to {}".format(swap(place)),
    "The ballad of the {}".format(swap(noun)),
    "My {NOUN1} is like a {ADJ} {NOUN2}".format(NOUN1=swap(noun), ADJ=swap(adj), NOUN2=swap(noun)),
    "a tale of the {ADJ} {NOUN}".format(ADJ=swap(adj), NOUN=swap(noun))
]

# PRINTING
title = fix(swap(titles)).upper()
print('\n{}'.format(title))
print('*' * len(title) + '\n')
name = "{FIRST} \"the {ADJ} {NOUN}\" {LAST}".format(FIRST=swap(first_names), ADJ=swap(adj), NOUN=swap(noun), LAST=swap(last_names))
print("By {}\n".format(name).title())

for line in lim:
    line = fix(line)
    print(line.title())
print(swap(endings).title())