import database


def vak_naar_bin(v1, v2, v3, v4, v5, v6, v7, v8, v9, v10):
    binary = 0b10
    if v1:
        binary += 1
        # print("v1")
    binary = binary << 1
    if v2:
        binary += 1
        # print("v2")
    binary = binary << 1
    if v3:
        binary += 1
        # print("v3")
    binary = binary << 1
    if v4:
        binary += 1
        # print("v4")
    binary = binary << 1
    if v5:
        binary += 1
        # print("v5")
    binary = binary << 1
    if v6:
        binary += 1
        # print("v6")
    binary = binary << 1
    if v7:
        binary += 1
        # print("v7")
    binary = binary << 1
    if v8:
        binary += 1
        # print("v8")
    binary = binary << 1
    if v9:
        binary += 1
        # print("v9")
    binary = binary << 1
    if v10:
        binary += 1
        # print("v10")
    return bin(binary)


def delays():
    a = 10_000_000
    b = 0
    for i in range(a):
        b += i
    return b


def run():
    daguur = database.get_daguur()
    print("daguur data: \n", daguur)
    dagen = daguur[1]
    uuren = daguur[2]
    print(dagen, uuren)

    leerlingen = database.get_leerlingen()
    print("leerlingen data: \n", leerlingen)

    l = leerlingen[0,3]
    print(l)

