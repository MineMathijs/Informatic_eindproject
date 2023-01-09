import numpy as np
from random import randint, shuffle


def leegRooster(dagen: int, uuren: int):
    return np.zeros(shape=(dagen, uuren), dtype=np.int8)


def vulRooster(leegrooster: np.array, vakken: np.array):

    rooster = np.ravel(leegrooster)
    options = np.arange(rooster.size)
    shuffle(options)
    print(options)
    for vak in vakken:
        print(vak)
        for _ in range(int(vak[2])):
            if options.any():
                rooster[options[0]] = int(vak[0])
                np.delete(options, 0)
            rooster.shape(np.shape(leegrooster))
            return rooster


vak = np.array([[1, "Informatica", 3], [2, "Natuurkunde", 4]])
leeg = leegRooster(5, 8)
vul = vulRooster(leeg, vak)
print(vul)
