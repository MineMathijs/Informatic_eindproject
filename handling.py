import database
import algorithm
import numpy as np
import algorithm2


# def vak_naar_bin(v1, v2, v3, v4, v5, v6, v7, v8, v9, v10):
#     binary = 0b10
#     if v1:
#         binary += 1
#         # print("v1")
#     binary = binary << 1
#     if v2:
#         binary += 1
#         # print("v2")
#     binary = binary << 1
#     if v3:
#         binary += 1
#         # print("v3")
#     binary = binary << 1
#     if v4:
#         binary += 1
#         # print("v4")
#     binary = binary << 1
#     if v5:
#         binary += 1
#         # print("v5")
#     binary = binary << 1
#     if v6:
#         binary += 1
#         # print("v6")
#     binary = binary << 1
#     if v7:
#         binary += 1
#         # print("v7")
#     binary = binary << 1
#     if v8:
#         binary += 1
#         # print("v8")
#     binary = binary << 1
#     if v9:
#         binary += 1
#         # print("v9")
#     binary = binary << 1
#     if v10:
#         binary += 1
#         # print("v10")
#     return bin(binary)


def delays():
    a = 10_000_000
    b = 0
    for i in range(a):
        b += i
    return b


def alleRoosters(dagen: int, uuren: int, leerlingen: np.array):
    data = np.array([])


def run():
    daguur = database.get_daguur()
    # print("daguur data: \n", daguur)
    dagen = daguur[1]
    uuren = daguur[2]
    # print(dagen, uuren)

    vakData = database.get_vakken()
    vakkendic = {int(vak[0]): vak[0::] for vak in vakData}

    leerlingenRaw = database.get_leerlingen()
    # print("leerlingen data: \n", leerlingenRaw)

    leerlingen = np.empty((0, 4))

    for leerling in leerlingenRaw:
        leerlingVakkenMet0 = np.frombuffer(leerling[3], dtype=np.int16)
        leerlingVakken = np.array(leerlingVakkenMet0[leerlingVakkenMet0 != 0])
        newRow = np.array(
            [[int(leerling[0]), leerling[1], leerling[2], leerlingVakken]], dtype=object)
        leerlingen = np.append(leerlingen, newRow, 0)
        # print(leerlingVakken)
    # print(leerlingen)

    alleRoosters = np.empty((0,3))


    for leerling in leerlingen:
        persoon = np.array([leerling[0], leerling[1], leerling[2]])
        rooster = algorithm.leegRooster(dagen,uuren)

        keuzes = leerling[3]
        vakken = np.array([[0,"-",0]], dtype=object)
        for keuze in keuzes:
            arr = vakkendic[keuze]
            vakken = np.append(vakken, [arr], 0)
        # print(vakken)

        newRow = np.array([[persoon,rooster,vakken]], dtype=object)
        alleRoosters = np.append(alleRoosters, newRow, 0)

    # print(alleRoosters)

    for i, rooster in enumerate(alleRoosters):
        goedrooster = algorithm.geneticAlgorithm(rooster)
        alleRoosters[i,1] = goedrooster

    
    print("--------------------------------------------")
    print(alleRoosters)
    print("--------------------------------------------")

    for i, rooster in enumerate(alleRoosters):
        naamRooster = algorithm2.printrooster(rooster[1], vakkendic)
        alleRoosters[i,1] = naamRooster
    
    print("--------------------------------------------")
    print(alleRoosters)
    print("--------------------------------------------")

    return alleRoosters


if __name__ == "__main__":
    a = run()
    # print(a)
    # z = database.get_vakken()
    # print(z)
