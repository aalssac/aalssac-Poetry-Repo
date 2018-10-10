# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 19:22:20 2018

@author: acarr56
"""

import markovify as m

with open ("beauty.txt") as textfile:
    beauty = textfile.read()
    

with open ("joys.txt") as textfile :
    joy= textfile.read()
    

    
beauty_model = m.NewlineText(beauty)

joy_model = m.NewlineText(joy)

synthesized_model = m.combine([beauty_model, joy_model], [1,1])




print synthesized_model.make_sentence()



with open ("poem.md", "a") as m:
    m.write ("## Title")
    m.write("\n")
    m.write("```")
    m.write("\n")
    for i in range(5):
        poem = synthesized_model.make_short_sentence(25)
        m.write(poem)
        m.write("\n")
    m.write("\n")
    m.write("```")
    m.write("\n")
       