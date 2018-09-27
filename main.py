import math


def encrypt(userS, key):
    # Encryption
    keyLen = len(key)
    padLen = len(userS) % keyLen

    # pads the message s so with spaces so that it can be encrypted
    if padLen > 0:
        for i in range(0, keyLen - padLen):
            userS = userS + " "

    sList = []
    ind = 0
    while ind < len(userS):
        sList.append(list(userS[ind: ind + keyLen]))
        ind = ind + keyLen
    keyList = list(key)
    keyList.sort()

    newS = ""
    for i in range(0, len(keyList)):
        for x in range(0, len(sList)):
            newS = newS + sList[x][keyList.index(key[i: i + 1])]

    return newS


def decrypt(newUserS, key):
    # Decryption
    keyLen = len(key)
    keyList = list(key)
    keyList.sort()

    outlist = []
    for i in range(0, keyLen):
        outlist.append([])

    numrows = math.ceil(len(newUserS) / keyLen)

    fullcols = len(newUserS) % keyLen
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

        colslice = newUserS[begslice: begslice + lenslice]
        begslice += lenslice

        outlist[keyindex] = list(colslice)

    outstr = ""

    for index in range(0, len(newUserS)):
        row = index // keyLen
        col = index % keyLen
        outstr += outlist[col][row]

    return outstr


s = input("Type your message: ")
k = input("Type your key: ")
s = encrypt(s, k)
print("Encrypted String is: ", s)

outstr = decrypt(s, k)

print("Decrypted string is: ", outstr)