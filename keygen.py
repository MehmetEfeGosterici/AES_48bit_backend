from random import Random
import numpy as np

keys = []
temporarys = []
xorTable = [["000", "001", "010", "011", "100", "101", "110", "111"],
            ["001", "000", "011", "010", "101", "100", "111", "110"],
            ["010", "011", "000", "001", "110", "111", "100", "101"],
            ["011", "010", "001", "000", "111", "110", "101", "100"],
            ["100", "101", "110", "111", "000", "001", "010", "011"],
            ["101", "100", "111", "110", "001", "000", "011", "010"],
            ["110", "111", "100", "101", "010", "011", "000", "001"],
            ["111", "110", "101", "100", "011", "010", "001", "000"]]

rconTable = [["000", "010", "000", "000"],
             ["000", "111", "000", "000"],
             ["000", "011", "000", "000"],
             ["000", "110", "000", "000"],
             ["000", "101", "000", "000"],
             ["000", "001", "000", "000"],
             ["000", "100", "000", "000"],
             ["101", "000", "000", "000"],
             ["111", "000", "000", "000"]]


def subBytes(bits):
    Switch = {
        "000": "100",
        "001": "101",
        "010": "001",
        "011": "010",
        "100": "011",
        "101": "110",
        "110": "111",
        "111": "000"
    }
    return Switch.get(bits, "error")


def shiftRows(x):
    shiftcount = 0
    for i in range(len(x)):
        x[i] = np.roll(x[i], shiftcount)
        shiftcount += 3
    return x


def rotWord(x):
    x = np.roll(x, -1)
    return x


def temporary(x, num):
    array = rotWord(x)
    temp = [0 for i in range(len(array))]
    # print(array,"\n\n\n")
    for i in range(len(array)):
        array[i] = subBytes(array[i])
    # print(array,"\n\n\n")
    for i in range(len(array)):
        temp[i] = xorTable[int(hex(int(rconTable[num][i], 2)).replace(
            "0x", ""))][int(hex(int(array[i], 2)).replace("0x", ""))]
    # print(temp,"\n\n\n")
    return temp


def keyGen():
    for i in range(4):
        temp = []
        for j in range(4):
            integer = Random().randint(0, 7)
            binary = bin(integer).replace("0b", "")
            reverse = binary[::-1]
            while len(reverse) < 3:
                reverse += "0"
            binary = reverse[::-1]
            temp.append(binary)
        keys.append(temp)

    # print(np.matrix(keys))

    for i in range(4, 36):
        if(i % 4 == 0):
            key = [0 for x in range(4)]
            tempArray = (temporary(keys[i-1], int(i/4-1)))
            temporarys.append(tempArray)
            for j in range(4):
                key[j] = xorTable[int(hex(int(tempArray[j], 2)).replace("0x", ""))][int(
                    hex(int(keys[i-4][j], 2)).replace("0x", ""))]
            keys.append(key)
        else:
            key = [0 for i in range(4)]
            for j in range(4):
                key[j] = xorTable[int(hex(int(keys[i-1][j], 2)).replace("0x", ""))
                                  ][int(hex(int(keys[i-4][j], 2)).replace("0x", ""))]
            keys.append(key)
    print("Round Keys\n", np.matrix(keys), "\n\n")
    print("T values\n", np.matrix(temporarys))
    return keys