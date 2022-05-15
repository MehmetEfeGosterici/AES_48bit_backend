from keygen import shiftRows, subBytes
import numpy as np


test = [["000","100","000","000"],
        ["000","100","000","000"],
        ["000","100","000","000"],
        ["000","100","000","000"],]


def encryptionRound(block):
    for i in range(4):
        for j in range(4):
            block[i][j] = subBytes(block[i][j])
    shiftRows(block)
    print(np.matrix(block))



encryptionRound(test)

# shiftRows(test)
# print(np.matrix(test))