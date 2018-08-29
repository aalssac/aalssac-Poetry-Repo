# -*- coding: utf-8 -*-
"""
AUTHOR: Abbie Carrier
DESCRIPTION: Python text generator
LICENSE:GNU General Public License v2
"""

import random

random.seed()

#list of nouns
nouns = ["sailor", "ship", "anchor"]
#print nouns[2]

#i = 0
#for noun in nouns:
#    print nouns [i]
#    i = i + 1
#    


#list of verbs
verbs = ["runs",
        "floats",
         "sinks", 
         "types",
         "jumps"]

#list of adjectives
adjectives = ["blue",
              "orange",
              "colorful",
              "confusing",
              "agreeable",
              "eager"]

noun = random.choice(nouns)
#print noun

verb = random.choice(verbs)

adjective = random.choice(adjectives)

second_adjective = random.choice(adjectives)

print "The "+ adjective + ", " + second_adjective + " " + noun + " " + verb + "."

print "The {adj} {n} {v}".format(adj=adjective, n=noun, v=verb)

print "The " +adjective + " " + noun + " "

i=1
for verb in verbs:
    whitespace = " " * i
    print whitespace + verb
    i = i + 1


              