import numpy as np
# van random import randint
# import ook algorithm.py


vakken = np.array([ # dit zijn de vakken, voornu, het eerste getal is het vaknummer, en het tweede getal is het aantal uuren dat dit vak in het rooster moet zitten
    [0, 0, "-           "], 
    [1, 4, "Informatica "],
    [2, 3, "Wiskunde    "], # letop dit is geen lijst, maar een numpy array om het aantal uuren voor wiskunde te krijgen doe je dus vakken[2,1]
    [3, 3, "Engels      "],
    [4, 5, "Nederlands  "],
    [5, 2, "Natuurkunde "],
    [6, 4, "Scheikunde  "],
    [7, 3, "Duits       "]
])

# voornu gebruik dit als leeg rooster, 
leeg_rooster = np.zeros(shape=(5,8), dtype=int)

# maak een FUNCTIE(dus met def functie_naam(): ...) die iets genaamd is als rooster_vullen
# ga ieder vak af (gebruik een for-loop) en kies een random plek in het rooster(met behulp van een while-loop en randint())
# doe dit voor het aantal uuren die het vak heeft en return dan een np.array gevuld met vakken 

# om te kijken of de functie werkt moet je hem eerst callen:
# gevulde_rooster = rooster_vullen(leeg_rooster, vakken)
# en daarna printen:
# print(gevulde_rooster)

# handige links:
# https://stackoverflow.com/questions/44209368/how-to-change-a-single-value-in-a-numpy-array 
# https://fundament-online.nl/ 
# https://www.w3schools.com/python/python_for_loops.asp
# https://www.w3schools.com/python/python_while_loops.asp 

# probeer, als het lukt, de functie zo te maken dat je GEEN range(len()) gebruikt.