import math

def encrypt(str, key):
    # Encryption
    keyLen = len(key)
    padLen = len(s) % keyLen

    # pads the message s so with spaces so that it can be encrypted
    if padLen > 0:
        for i in range(0, keyLen - padLen):
            str = str + " "

    sList = []
    ind = 0
    while ind < len(s):
        sList.append(list(str[ind: ind + keyLen]))
        ind = ind + keyLen
    keyList = list(key)
    keyList.sort()

    newS = ""
    for i in range(0, len(keyList)):
        for x in range(0, len(sList)):
            newS = newS + sList[x][keyList.index(key[i: i + 1])]

    return newS


def decrypt(str, key):
    # Decryption
    keyLen = len(key)
    keyList = list(key)

    outlist = []
    for i in range(0, keyLen):
        outlist.append([])

    numrows = math.ceil(len(str) / keyLen)

    fullcols = len(s) % keyLen
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

        colslice = str[begslice: begslice + lenslice]
        begslice += lenslice

        outlist[keyindex] = list(colslice)

    outstr = ""

    for index in range(0, len(str)):
        row = index // keyLen
        col = index % keyLen
        outstr += outlist[col][row]

    return outstr


s = input("Type your message: ")
key = input("Type your key: ")
s = encrypt(s, key)
print("Encrypted String is: ", s)

outstr = decrypt(s, key)

print("Decrypted string is: ", outstr)