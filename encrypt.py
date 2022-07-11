from test import test
import re
from statistics import variance
import numpy as np
from test import encryptionRound, keysToArray
from keygen import shiftRows, subBytes, xorTable
import copy


mixColumnsArray = [["001", "010", "100", "110"],
                   ["010", "001", "110", "100"],
                   ["100", "110", "001", "010"],
                   ["110", "100", "010", "001"], ]

mixColumnsMultiplication = [["---", "---", "---", "---", "---", "---", "---", "---"],
                            ["000", "001", "010", "011",
                                "100", "101", "110", "111"],
                            ["000", "010", "100", "110",
                                "011", "001", "111", "101"],
                            ["---", "---", "---", "---",
                                "---", "---", "---", "---"],
                            ["000", "100", "011", "111",
                                "110", "010", "101", "001"],
                            ["---", "---", "---", "---",
                                "---", "---", "---", "---"],
                            ["000", "110", "111", "001", "101", "011", "010", "100"]]


def lastRound(block):
    for a in range(4):
        for b in range(4):
            block[a][b] = subBytes(block[a][b])
    return shiftRows(block)


def addRoundKey(block, keyCounter, keys):
    print(keyCounter)
    for j in range(4):  # each block goes through a matris multiplication with a key block
        for k in range(4):
            block[j][k] = (xorTable[int(hex(int(block[j][k], 2)).replace(
                "0x", ""))][int(hex(int(keys[keyCounter][k], 2)).replace("0x", ""))])
        keyCounter += 1
    return block


def encryptionRound(block, afterSubBytes, afterShiftRows, afterMixColumns):
    #print("first\n",np.matrix(block),"\n")
    if (len(afterSubBytes) % 9 == 0):
        afterSubBytes.append([["X" for i in range(4)] for i in range(4)])
        afterShiftRows.append([["X" for i in range(4)] for i in range(4)])
        afterMixColumns.append([["X" for i in range(4)] for i in range(4)])
    for i in range(4):
        for j in range(4):
            block[i][j] = subBytes(block[i][j])
    #print("first\n",np.matrix(block),"\n")
    afterSubBytes.append(copy.deepcopy(block))
    #print("afterSubBytes\n", np.matrix(block))
    shiftRows(block)
    #print("first\n",np.matrix(block),"\n")
    afterShiftRows.append(copy.deepcopy(block))
    #print("afterShiftRows\n", np.matrix(block))
    #print("second\n",np.matrix(block),"\n")
    block = np.rot90(block)[::-1]
    #print("third\n",np.matrix(block),"\n")
    temp = []
    xor_arr = "000"
    for i in range(4):
        temp2 = []
        for j in range(4):
            for x in range(4):
                xor_arr = xorTable[int(hex(int(xor_arr, 2)).replace("0x", ""))][int(hex(int(mixColumnsMultiplication[int(hex(int(
                    mixColumnsArray[j][x], 2)).replace("0x", ""))][int(hex(int(block[i][x], 2)).replace("0x", ""))], 2)).replace("0x", ""))]
            temp2.append(xor_arr)
            xor_arr = "000"
        temp.append(temp2)
    block = temp
    # print("---------------\n","afterMixColumns\n",np.matrix(block))
    block = np.rot90(block)[::-1]
    afterMixColumns.append(copy.deepcopy(block))
    #print("fourth\n",np.matrix(block),"\n")
    return block


def binaryConversionToHex(blockArray):
    string = ""
    tempString = ""
    stringArray = []

    for i in range(len(blockArray)):
        for x in range(4):
            for y in range(4):
                string += "".join(blockArray[i][x][y])
    for i in range(0, len(string)):
        tempString = tempString + string[i]
        if(len(tempString) == 3):
            stringArray.append(tempString)
            tempString = ""
    string = ""
    for i in range(len(stringArray)):
        stringArray[i] = hex(int(stringArray[i], 2)).replace("0x", "")
        string += stringArray[i]
    print("string\n", string)
    return string


def textToBlockArray(string, count, plainText, blockArray):
    binary = ""
    for i in range(len(string.upper())):
        #print(bin(ord(string[i])).replace("b", ""))
        binary += bin(ord(string[i])).replace("b", "")
    while (len(binary) % 48 != 0):
        binary += "0"

    binary = re.findall("...", binary)
    # print(binary)

    for k in range(int(len(binary)/4)):
        matris = [0 for i in range(4)]
        for j in range(4):
            matris[j] = binary[count]
            count += 1
        plainText.append(matris)
    for i in range(0, int(len(plainText)), 4):
        temp = []
        for j in range(4):
            temp.append(plainText[i+j])
        blockArray.append(temp)


def plainTextToCipherText(encryptionRequest, generatedkeys, firstBlock, afterSubBytes, AfterShiftRows, afterMixColumns):
    count = 0
    keyCounter = 0
    plainText = []
    blockArray = []
    keys = generatedkeys
    afterSubBytes = []
    AfterShiftRows = []
    afterMixColumns = []
    firstBlock = []
    keysBlock = []

    afterSubBytes.insert(0, [["X" for i in range(4)] for i in range(4)])
    AfterShiftRows.insert(0, [["X" for i in range(4)] for i in range(4)])
    afterMixColumns.insert(0, [["X" for i in range(4)] for i in range(4)])

    textToBlockArray(string=encryptionRequest, count=count,
                     plainText=plainText, blockArray=blockArray)
    for i in range(len(blockArray)):
        print("***", blockArray[i])
    for i in range(len(blockArray)):
        for v in range(9):
            keysBlock.append(keysToArray(keys)[v])
        firstBlock.append(copy.deepcopy(blockArray[i]))
        print("*****", blockArray[i])
        blockArray[i] = addRoundKey(blockArray[i], keyCounter, keys)
        keyCounter +=4

        # for z in range(len(firstBlock)):
        #     print(f"first{z}\n", np.matrix(firstBlock[z]))
        for x in range(8):  # each block goes through 8 encryption rounds
            firstBlock.append(copy.deepcopy(blockArray[i]))
            if(x < 8):
                blockArray[i] = encryptionRound(
                    blockArray[i], afterSubBytes, AfterShiftRows, afterMixColumns)
                blockArray[i] = addRoundKey(blockArray[i], keyCounter, keys)
                keyCounter +=4
                #print("afterEachRound\n",np.matrix() )
            else:
                blockArray[i] = lastRound(blockArray[i])
                blockArray[i] = addRoundKey(blockArray[i], keyCounter, keys)
                keyCounter +=4
        keyCounter = 0

    # for i in range(len(afterSubBytes)):
    #     print("\n", "subbytes\n", np.matrix(afterSubBytes[i]), "\n")
    # for i in range(len(afterSubBytes)):
    #     print("shiftrows\n", np.matrix(AfterShiftRows[i]), "\n")
    # for i in range(len(afterSubBytes)):
    #     print("mixcolumns\n", np.matrix(afterMixColumns[i]), "\n")
    for z in range(len(firstBlock)):
        print(f"first{z}\n", np.matrix(firstBlock[z]))

    
    print("----",keysBlock,"***",len(keysBlock))

    return {
        "encryptedMessage": binaryConversionToHex(blockArray),
        "startofRound": np.array(firstBlock).tolist(),
        "SubBytes": np.array(afterSubBytes).tolist(),
        "ShiftRows": np.array(AfterShiftRows).tolist(),
        "MixColumns": np.array(afterMixColumns).tolist(),
        "keys": np.array(keysBlock).tolist()
    }

encryptionRound(test,[],[],[])