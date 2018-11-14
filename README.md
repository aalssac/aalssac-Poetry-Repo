# Poetry Repository

## Artist Statement

My hope for my poem would be to write something pertaining to the strength of women. I want to focus on famous women throughout history and their accomplishments. I would want my poem to educate those that are not as familar with these women as I am. I want it to introduce them to the masses, and let the masses know why their names should be known.


## Python code

```python
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

#print "{noun} {verb}.".format(noun=noun, verb=verb) 

print "They all changed the World"
```
```
import markovify as m

with open ("beauty.txt") as textfile:
    beauty = textfile.read()
    

with open ("joys.txt") as textfile:
    joy = textfile.read()
    
  

    
beauty_model = m.NewlineText(beauty)

joy_model = m.NewlineText(joy)


synthesized_model = m.combine([beauty_model, joy_model], [1,1])

with open ("poem.txt", "w") as m:
    for i in range(10):
       poem = synthesized_model.make_short_sentence(50)
       m.write(poem)
```

![waveform](Documents\GitHub\aalssac-Poetry-Repo/Capture.png)
