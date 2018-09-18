import math

s = input("Type your message: ")
key = input("Type your key: ")

# Encryption
keyLen = len(key)
padLen = len(s) % keyLen

# pads the message s so with spaces so that it can be encrypted
if padLen > 0:
    for i in range(0, keyLen - padLen):
        s = s + " "

sList = []
ind = 0
while ind < len(s):
    sList.append(list(s[ind: ind + keyLen]))
    ind = ind + keyLen
keyList = list(key)
keyList.sort()

newS = ""
for i in range(0, len(keyList)):
    for x in range(0, len(sList)):
        newS = newS + sList[x][keyList.index(key[i: i + 1])]
print("Encrypted String is: ", newS)

# Decryption
outlist = []
for i in range(0, keyLen):
    outlist.append([])

numrows = math.ceil(len(newS) / keyLen)

fullcols = len(newS) % keyLen
if fullcols == 0:
    fullcols = keyLen
lenslice = 0
begslice = 0

for index in range(0, keyLen):
    keyletter = key[index]
    keyindex = keyList.index(keyletter)

    if keyindex >= fullcols:
        lenslice = numrows - 1
    else:
        lenslice = numrows

    colslice = newS[begslice: begslice + lenslice]
    begslice += lenslice

    outlist[keyindex] = list(colslice)

outstr = ""

for index in range(0, len(newS)):
    row = index // keyLen
    col = index % keyLen
    outstr += outlist[col][row]

print("Decrypted string is: ", outstr)
