from keygen import shiftRows, subBytes,xorTable
import numpy as np


test = [["000", "100", "000", "000"],
        ["000", "100", "000", "000"],
        ["000", "100", "000", "000"],
        ["000", "100", "000", "000"], ]

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


def encryptionRound(block):
    for i in range(4):
        for j in range(4):
            block[i][j] = subBytes(block[i][j])
    #print("afterSubBytes\n",np.matrix(block))
    shiftRows(block)
    #print("afterShiftRows\n",np.matrix(block))

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
    print("---------------\n","afterMixColumns\n",np.matrix(block))
    return block