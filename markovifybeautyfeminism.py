# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 19:22:20 2018

@author: acarr56
"""

import markovify as m

with open ("beauty.txt") as textfile:
    beauty = textfile.read()
    
with open ("feminism.txt") as textfile:
    feminism= textfile.read()
    
beauty_model = m.NewlineText(beauty)
feminism_model = m.NewlineText(feminism)

synthesized_model = m.combine([beauty_model, feminism_model], [1,1])

print synthesized_model.make_sentence()

#print randomly generated sentences
for i in range(9):
    print synthesized_model.make_short_sentence(50)


