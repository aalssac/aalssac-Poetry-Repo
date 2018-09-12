# -*- coding: utf-8 -*-
"""
AUTHOR: Abbie Carrier
DESCRIPTION: Python text generator
LICENSE:GNU General Public License v2
"""

import random

random.seed()

#list of nouns
#nouns = ["sailor", "ship", "anchor"]
#print nouns[2]

#i = 0
#for noun in nouns:
#    print nouns [i]
#    i = i + 1
#    


##list of verbs
#verbs = ["runs",
#        "floats",
#         "sinks", 
#         "types",
#         "jumps"]
#
##list of adjectives
#adjectives = ["blue",
#              "orange",
#              "colorful",
#              "confusing",
#              "agreeable",
#              "eager"]
#
#noun = random.choice(nouns)
##print noun
#
#verb = random.choice(verbs)
#
#adjective = random.choice(adjectives)
#
#second_adjective = random.choice(adjectives)
#
#print "The "+ adjective + ", " + second_adjective + " " + noun + " " + verb + "."
#
#print "The {adj} {n} {v}".format(adj=adjective, n=noun, v=verb)
#
#print "The " +adjective + " " + noun + " "


#
#nouns = ["woman", "girl", "femme", "mujer"]
#
#verbs = ["roar", "rugir", "rugido"]
#
#adverbs= ["loudly", "blaringly", "vociferously", "bruyant"]
#
#noun= random.choice (nouns)
#
#print nouns
#
#print verbs
#
#noun = random.choice(nouns)
#verb = random.choice(verbs)
#adverb = random.choice(adverbs)
#
#print " {noun}  {verb} {adverb}.".format( noun=noun, verb=verb, adverb=adverb)

import random
random.seed()
i=random.randint(1,20)

whitespace = " " * i

print whitespace + "hello world!"

names = ["Elizabeth", "Fitzwilliam", "Marie"]
pronouns = ["he", "she", "it"]

name = random.choice(names)
pronoun = random.choice(pronouns)
#
print pronoun.capitalize() + " " + name

print "On a dark and stormy night {name} went up to the old house.\
{pronoun} was about to roll the dice.".format (name=name, pronoun=pronoun)

roll = random.randint(1,6)
print "{name} rolled a {roll}".format(name=name, roll=roll)

if  roll ==  1:
#    print "Success!" + pronoun + "rolled a" + str(roll)
#    print "Success! {pronoun} rolled a {roll}".format(pronoun=pronoun, roll=roll)
    print "Bad luck!"
elif roll == 6:
    print "Good luck!"
else: 
    print "Not so bad luck..."