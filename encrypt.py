import re
import numpy as np

from keygen import keyGen, subBytes, xorTable

string = "abcdefghijklmnoprstvy"
binary = ""
plainText = []
count = 0


for i in range(len(string)):
    binary += bin(ord(string[i])).replace("0b","")
while (len(binary)%48!=0):
    binary += "0"

binary = re.findall("...",binary)

for k in range(int(len(binary)/4)):
    matris=[0 for i in range(4)]
    for j in range(4):
        matris[j] = binary[count]
        count+=1
    plainText.append(matris)
        
keys = keyGen()

#print(np.matrix(binary),"\n\n\n")
print("plainText\n",np.matrix(plainText),"\n\n")
blockArray = []
for i in range(0,int(len(plainText)),4):
    temp=[]
    for j in range(4):
        temp.append(plainText[i+j])
    blockArray.append(temp)
for i in range(len(blockArray)):
    print("blockArray\n",np.matrix(blockArray[i]),"\n\n""")


for i in range(len(blockArray)):
    keyCounter = 0
    xor = []
    for j in range(4):
        temp=[]
        for k in range(4):
            #print(blockArray[i][j][k])
            blockArray[i][j][k] = (xorTable[int(hex(int(blockArray[i][j][k],2)).replace("0x",""))][int(hex(int(keys[keyCounter][k],2)).replace("0x",""))])
        #xor.append(temp)
        keyCounter += 1
    #print(np.matrix(xor))
    # for x in range(4):
    #     for y in range(4):
    #         blockArray[i][j][k] = subBytes(blockArray[i][j][k])
    print(keyCounter,"bbb")
    

print("---")
for i in range(len(blockArray)):
    print("blockArray\n",np.matrix(blockArray[i]),"\n\n""")


