import numpy as np
import re


keyWord = "abcdef"
myString = ""
binary = []
matris = [[0 for x in range(4)] for y in range(4)]
keys = []
a = 0

for i in range(len(keyWord)):
    myString += (bin(ord(keyWord[i])).replace("b", ""))

while(len(myString) < 48):
    myString += "0"

binary = re.findall("...", myString)

for k in range(4):
    for j in range(4):
        matris[k][j] = binary[a]
        a += 1

keys.append(matris)

""" for i in keys:
    print(np.matrix(i))
 """


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
        shiftcount += 1
    return x


def rotWord(x):
    for i in range(len(x)):
        x[i] = np.roll(x, -1)
    return x


print(np.matrix(matris), "\n\n\n")
matris = shiftRows(matris)
print(np.matrix(matris), "\n\n\n")
