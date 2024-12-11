file = open(r'C:\Users\user\Desktop\Κ\Vigenere.txt' , 'r')
content = file.read()
print(content)
file.close()
##########################################################################
letterDict = {}
lengthOfPartition = 0
for i in range(len(content)):
    if i%7 == 0:
        lengthOfPartition += 1
        letter = content[i]
        if letter not in letterDict:
            letterDict[letter] = {"count": 1, "frequency": 0}
        if letter in letterDict:
            letterDict[letter]["count"] += 1
for key in letterDict.keys():
    letterDict[key]["frequency"] = letterDict[key]["count"]/lengthOfPartition

for key, subDict in letterDict.items():
    print(f"Statistics for {key=}", end=" ")
    for subKey, subValue in subDict.items():
        print(f"{str(subKey)} = {str(subValue)}", end=" | ")
    print("")
print("#################")
sorLetDict = dict(sorted(letterDict.items(), key=lambda item: item[1]["count"], reverse= True))
for letter, stats in sorLetDict.items():
    print(letter, end=": ")
    for key, value in stats.items():
        print(key,value,end=" = ")
    print("")

frequencyTable = {}
cnt = 0
for key in sorLetDict:
    frequencyTable[key] = cnt
    cnt += 1
for key in frequencyTable:
    print(key, frequencyTable[key])
store = []
for key in frequencyTable:
    store.append([key, frequencyTable[key]])
for element in store:
    frequencyTable[element[0]] = element[1]
for key in frequencyTable.keys():
    print(key, frequencyTable[key])
