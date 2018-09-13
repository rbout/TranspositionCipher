s = input("Type your message: ")
key = input("Type your key: ")
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
print(newS)
