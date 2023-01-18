import numpy as np
from random import randint, shuffle


def leegRooster(dagen: int, uuren: int):
    return np.zeros(shape=(dagen, uuren), dtype=np.int8)


def vulRooster(leegrooster: np.array, vakken: np.array):

    rooster = np.ravel(leegrooster)
    options = np.arange(rooster.size)
    shuffle(options)
    # print(options)
    for vak in vakken:
        # print(vak)
        for _ in range(int(vak[2])):
            if options.any():
                # print(options[0])
                rooster[options[0]] = int(vak[0])
                options = options[1:]
                # print(options[0])
    rooster.shape = np.shape(leegrooster)
    return rooster

def geneticAlgorithm(eenRooster):
    vakken = eenRooster[2]
    leegRooster = eenRooster[1]
    populationSize = 500
    fitnesStop = 1500
    maxGenerations = 200
    startFitness = 1000

    population = np.array([[vulRooster(leegRooster,vakken), startFitness] for _ in range(populationSize)], dtype=object)
    print(population)

    for i, rooster in enumerate(population):
        fitness = calcFitness(startFitness,rooster[0])
        population[i,1] = fitness
    return population[0]

def calcFitness(startFitness,rooster):
    fitness = startFitness
    for i, dag in enumerate(rooster):
        for j, uur in enumerate(dag):
            if uur in dag[:j-1]+dag[j+1:]:
                print("2x in een dag")
                fitness -= 50

if __name__ == "__main__":
    Rooster = np.array([
        np.array(['4', 'John', 'Doe'], dtype='<U11'),
        np.array([[0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0]], dtype=np.int8),
        np.array([['1', 'Informatica', '4'],
                ['2', 'Natuurkunde', '5'],
                ['3', 'Engels', '5'],
                ['4', 'Scheikunde', '3'],
                ['5', 'Duits', '2'],
                ['6', 'Wiskunde', '6'],
                ['7', 'Nederlands', '3']], dtype=object)], dtype=object)

    algor = geneticAlgorithm(Rooster)
    print(algor)
