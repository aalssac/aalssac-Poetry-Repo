# Poetry Repository

##This is my first markdown text.


## My hope for my poem would be to write something pertaining to the strength of women. I want to focus on famous women throughout history and their accomplishments. I would want my poem to educate those that are not as familar with these women as I am. I want it to introduce them to the masses, and let the masses know why their names should be known.


##python code##

import random
random.seed ()

nouns = "Artemisia" , "Maya" , "Eleanor" ,  "Joan", "Sojourner" , "Rosa"
verbs= "painted", "wrote", "lead", "fought", "escaped", "protested"


noun = random.choice(nouns)
verb = random.choice(verbs)

#
#print "{noun} {verb}.".format(noun=noun, verb=verb)

i = 0
for noun in nouns:
    i = i + 1
    whitespace = " " * i
    print whitespace + noun


i = 0
for verb in verbs:
    i = i + 1
    whitespace = " " * i
    print whitespace + verb


#
#print "{noun} {verb}.".format(noun=noun, verb=verb) 

print "They all changed the World"
    

