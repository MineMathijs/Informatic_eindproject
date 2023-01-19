import numpy as np
from random import randint, shuffle, choice, random
import copy


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


def calcFitness(startFitness, rooster):
    fitness = startFitness
    for i, dag in enumerate(rooster):
        for j, uur in enumerate(dag):
            if uur in dag[j+1:] and uur != 0:
                if uur in dag[j+2:]:
                    # print(f"2x in een dag op {i} : {j} met {uur}")
                    fitness -= 100
                if uur in [dag[j+1]]:
                    fitness += 50
                    # print(f"blokuur op {i} : {j} met {uur}")
            if uur == 0 and np.count_nonzero(dag[:j]) != 0 and np.count_nonzero(dag[j+1:]):
                # print(f"tussenuur op {i} : {j} met {uur}")
                fitness -= 25
    return fitness


def sortArr(arr):
    sortedArr = arr[arr[:, 1].argsort()]
    sortedReverse = np.flip(sortedArr, axis=0)
    return sortedReverse


def crossover(parent1, parent2):
    # Create copies of the parent
    offspring = np.array([])
    parent2_copy = np.copy(np.ravel(parent2))

    # Create a dictionary of unique elements and their counts in the first parent
    element_counts_parent1 = dict(zip(*np.unique(parent1, return_counts=True)))
    # Randomly select an index to start from in the second parent
    start_index = randint(0, parent2_copy.shape[0]-1)
    # Iterate through the second parent starting from the selected index
    for i in range(start_index, parent2_copy.shape[0]):
        if element_counts_parent1.get(parent2_copy[i], 0) > 0:
            element_counts_parent1[parent2_copy[i]] -= 1
            offspring = np.append(offspring, parent2_copy[i])
    # If we still need more elements, iterate from the beginning of the second parent
    for i in range(0, start_index):
        if element_counts_parent1.get(parent2_copy[i], 0) > 0:
            element_counts_parent1[parent2_copy[i]] -= 1
            offspring = np.append(offspring, parent2_copy[i])
    offspring = offspring.reshape(parent1.shape)
    return offspring


def mutate(arr):
    rows, cols = arr.shape
    x1, y1 = np.random.randint(0, rows), np.random.randint(0, cols)
    x2, y2 = np.random.randint(0, rows), np.random.randint(0, cols)
    temp = arr[x1, y1]
    arr[x1, y1] = arr[x2, y2]
    arr[x2, y2] = temp
    return arr


def geneticAlgorithm(eenRooster):
    vakken = eenRooster[2]
    leegRooster = eenRooster[1]
    populationSize = 1000
    fitnesStop = 1500
    selectBest = 50
    maxGenerations = 75
    startFitness = 1000
    crossoverSize = 500
    mutateChance = 0.85
    mutateAmmount = 2
    mutateOnlySize = 150

    population = np.array([[vulRooster(copy.copy(leegRooster), vakken), startFitness]
                          for _ in range(populationSize)], dtype=object)
    # print(population)

    for i, rooster in enumerate(population):
        fitness = calcFitness(startFitness, rooster[0])
        population[i, 1] = fitness

    population = sortArr(population)
    generation = 0
    # print(f"best solution for generation {generation}: \n {population[0]}")

    while population[0, 1] < fitnesStop and generation < maxGenerations:
        lastbest = copy.deepcopy(population[:selectBest])
        newPopulation = np.array([row[0] for row in lastbest])

        for _ in range(crossoverSize):
            parent1 = lastbest[randint(0, len(lastbest)-1), 0]
            parent2 = lastbest[randint(0, len(lastbest)-1), 0]
            child = crossover(parent1, parent2)
            for _ in range(mutateAmmount):
                if random() <= mutateChance:
                    child = mutate(child)
            newPopulation = np.append(newPopulation, [child], 0)

        for _ in range(mutateOnlySize):
            child = lastbest[randint(0, len(lastbest)-1), 0]
            for _ in range(mutateAmmount):
                if random() <= mutateChance:
                    child = mutate(child)
            newPopulation = np.append(newPopulation, [child], 0)

        wildcards = populationSize - len(newPopulation)
        for _ in range(wildcards):
            child = vulRooster(copy.copy(leegRooster), vakken)
            newPopulation = np.append(newPopulation, [child], 0)

        population = np.array([[gene, calcFitness(startFitness, gene)]
                               for gene in newPopulation], dtype=object)
        population = sortArr(population)
        generation += 1
        # print(f"best solution for generation {generation}: \n {population[0]}")

    return population[0,0]


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
