import numpy as np

def printrooster(rooster, vakken):
        
    vakIdNaam = {int(vak[0]):vak[1]for vak in vakken}

    roosterNaam = []

    for dag in rooster:
        for uur in dag:
            try:
                naam = vakIdNaam[uur]
            except:
                naam = "-"
            naamcentre = naam.center(20)
            roosterNaam.append(naamcentre)

    roosterNaamArray = np.array(roosterNaam)   

    shape = np.shape(rooster)
    roosterNaamArray = roosterNaamArray.reshape(shape)

    return roosterNaamArray

if __name__ == "__main__":
    rooster = np.array([[1, 0, 1, 0, 3, 3, 4, 5],[4, 5, 2, 3, 1, 1, 1, 0],[0, 0, 1, 3, 4, 3, 4, 5],[3, 3, 3, 2, 0, 0, 0, 1],[4, 2, 1, 3, 4, 5, 2, 0]])
    vakken = np.array([['1', 'Informatica', '4'],['2', 'Natuurkunde', '5'],['3', 'Engels', '5'],['4', 'Scheikunde', '3'],['5', 'Duits', '2'],['6', 'Wiskunde', '6'],['7', 'Nederlands', '3']])

    a = printrooster(rooster, vakken)
    print(a)