from keygen import keyGen, shiftRows, subBytes,xorTable
import numpy as np
import re

test = [["000", "100", "000", "000"],
        ["000", "101", "000", "000"],
        ["000", "110", "000", "000"],
        ["000", "111", "000", "000"], ]

mixColumnsArray = [["001", "010", "100", "110"],
                   ["010", "001", "110", "100"],
                   ["100", "110", "001", "010"],
                   ["110", "100", "010", "001"], ]

mixColumnsMultiplication = [["---", "---", "---", "---", "---", "---", "---", "---"],
                            ["000", "001", "010", "011", "100", "101", "110", "111"],
                            ["000", "010", "100", "110", "011", "001", "111", "101"],
                            ["---", "---", "---", "---", "---", "---", "---", "---"],
                            ["000", "100", "011", "111", "110", "010", "101", "001"],
                            ["---", "---", "---", "---", "---", "---", "---", "---"],
                            ["000", "110", "111", "001", "101", "011", "010", "100"]]

def encryptionRound(block,afterSubBytes,afterShiftRows,afterMixColumns):
    for i in range(4):
        for j in range(4):
            block[i][j] = subBytes(block[i][j])
    afterSubBytes.append(block)
    print("afterSubBytes\n",np.matrix(block))
    shiftRows(block)
    afterShiftRows.append(block)
    print("afterShiftRows\n",np.matrix(block))

    temp = [] 
    xor_arr = "000"
    for i in range(4):
        temp2 = []
        for j in range(4):
            for x in range(4):
                xor_arr = xorTable[int(hex(int(xor_arr,2)).replace("0x",""))][int(hex(int(mixColumnsMultiplication[int(hex(int(mixColumnsArray[j][x],2)).replace("0x",""))][int(hex(int(block[i][x],2)).replace("0x",""))],2)).replace("0x",""))]
            temp2.append(xor_arr)
            xor_arr = "000"
        temp.append(temp2)
    block = temp
    #print("---------------\n","afterMixColumns\n",np.matrix(block))
    afterMixColumns.append(block)
    return block

#keys = keyGen()

def keysToArray(keys):
    newKeys = []
    temp = []
    for i in range(len(keys)):
        for x in range(len(keys[i])):
            # print(keys[i][x])
            temp.append(keys[i][x])
            if(len(temp) == 16):
                # print(temp)
                newKeys.append(temp)
                temp = []
    #print(newKeys)
    # for i in range(len(newKeys)):
    #     # print("--",np.matrix(newKeys[i]))
    return newKeys

#keysToArray(keys)

# def mixcolumns(block):
#     array = np.rot90(block)[::-1]
#     print(np.matrix(array))
#     array = np.rot90(block,k=4)
#     print(np.matrix(array))
   

# mixcolumns(test)