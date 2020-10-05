from pybot import findimage, makerune, mx, my


### spell then runeloop int ###
#spell = ["encurso magni", 4] # HMM
spell = ["encurso magni ignis", 10] # GFB
#spell = ["encuro vita", 3] # UH
#spell = ["encurso vita virtus", 2] # SD
#spell = ["encreo mas amplio", 2] # Explo
findimage('handR')
handx, handy = mx, my
makerune(handx, handy)