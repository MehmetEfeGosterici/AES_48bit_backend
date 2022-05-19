import re
import numpy as np
from test import encryptionRound
from keygen import keyGen, xorTable

string = "abcdefghijklmnoprstvy"
binary = ""
plainText = []
count = 0

for i in range(len(string)):
    binary += bin(ord(string[i])).replace("0b", "")
while (len(binary) % 48 != 0):
    binary += "0"

binary = re.findall("...", binary)

for k in range(int(len(binary)/4)):
    matris = [0 for i in range(4)]
    for j in range(4):
        matris[j] = binary[count]
        count += 1
    plainText.append(matris)

keys = keyGen()

blockArray = []
for i in range(0, int(len(plainText)), 4):
    temp = []
    for j in range(4):
        temp.append(plainText[i+j])
    blockArray.append(temp)

for i in range(len(blockArray)):
    print("blockArray\n", np.matrix(blockArray[i]), "\n\n")


for i in range(len(blockArray)):
    keyCounter = 0
    result = []
    for j in range(4):
        for k in range(4):
            blockArray[i][j][k] = (xorTable[int(hex(int(blockArray[i][j][k], 2)).replace("0x", ""))][int(hex(int(keys[keyCounter][k], 2)).replace("0x", ""))])
        keyCounter += 1
    print("block x keys\n",np.matrix(blockArray[i]))
    for x in range(8):
        blockArray[i] = encryptionRound(blockArray[i])
        for j in range(4):
            for k in range(4):
                blockArray[i][j][k] = (xorTable[int(hex(int(blockArray[i][j][k], 2)).replace("0x", ""))][int(hex(int(keys[keyCounter][k], 2)).replace("0x", ""))])
            keyCounter += 1
        print("afterEachRound\n",np.matrix(blockArray[i]))