import database
import algorithm
import numpy as np


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
    print("daguur data: \n", daguur)
    dagen = daguur[1]
    uuren = daguur[2]
    print(dagen, uuren)

    leerlingenRaw = database.get_leerlingen()
    print("leerlingen data: \n", leerlingenRaw)

    leerlingen = np.empty((0, 4))

    for leerling in leerlingenRaw:
        leerlingVakkenMet0 = np.frombuffer(leerling[3], dtype=np.int16)
        leerlingVakken = np.array(leerlingVakkenMet0[leerlingVakkenMet0 != 0])
        newRow = np.array(
            [[int(leerling[0]), leerling[1], leerling[2], leerlingVakken]], dtype=object)
        leerlingen = np.append(leerlingen, newRow, 0)
        print(leerlingVakken)
    print(leerlingen)


if __name__ == "__main__":
    a = run()
    print(a)
    z = database.get_vakken()
    # print(z)
