import re
import numpy as np


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
        

#print(np.matrix(binary),"\n\n\n")
print(np.matrix(plainText))
tempArray = []
for i in range(0,int(len(plainText)),4):
    temp=[]
    for j in range(4):
        temp.append(plainText[i+j])
    tempArray.append(temp)
    tempArray.append(["-","-","-","-"])
print(np.matrix(tempArray))