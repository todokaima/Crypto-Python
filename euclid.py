file = open(r'C:\Users\user\Desktop\Κ\Vigenere.txt' , 'r')
content = file.read()
print(content)
file.close()
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
letterData = {
    0: {'letter': 'E', 'frequency': 0.1270}, 1: {'letter': 'T', 'frequency': 0.0906}, 2: {'letter': 'A', 'frequency': 0.0817}, 3: {'letter': 'O', 'frequency': 0.0751},
    4: {'letter': 'I', 'frequency': 0.0697}, 5: {'letter': 'N', 'frequency': 0.0675}, 6: {'letter': 'R', 'frequency': 0.0599}, 7: {'letter': 'H', 'frequency': 0.0609}, 8: {'letter': 'D', 'frequency': 0.0425}, 9: {'letter': 'S', 'frequency': 0.0633},
    10: {'letter': 'L', 'frequency': 0.0403}, 11: {'letter': 'C', 'frequency': 0.0278}, 12: {'letter': 'M', 'frequency': 0.0241}, 13: {'letter': 'W', 'frequency': 0.0236}, 14: {'letter': 'F', 'frequency': 0.0223}, 15: {'letter': 'P', 'frequency': 0.0193}, 16: {'letter': 'G', 'frequency': 0.0202},
    17: {'letter': 'U', 'frequency': 0.0276}, 18: {'letter': 'Y', 'frequency': 0.0197}, 19: {'letter': 'B', 'frequency': 0.0149}, 20: {'letter': 'V', 'frequency': 0.0098},
    21: {'letter': 'K', 'frequency': 0.0077}, 22: {'letter': 'Z', 'frequency': 0.0007}, 23: {'letter': 'X', 'frequency': 0.0015}, 24: {'letter': 'J', 'frequency': 0.0015}, 25: {'letter': 'Q', 'frequency': 0.0010}
}
toDecrypt = {}
matches = {}
message = {}
for mod in [0,1,2,3,4,5,6]:
    letterDict = {}
    lengthOfPartition = 0
    toDecrypt[mod] = []
    for i in range(len(content)):
        if i % 7 == mod:
            lengthOfPartition += 1
            letter = content[i]
            toDecrypt[mod].append(letter)
            if letter not in letterDict:
                letterDict[letter] = {"count": 1}
            if letter in letterDict:
                letterDict[letter]["count"] += 1
    for key in letterDict.keys():
        letterDict[key]["frequency"] = letterDict[key]["count"] / lengthOfPartition
    for element in alphabet:
        if element not in letterDict.keys():
            letterDict[element] = {"count": 0, "frequency": 0}

    for key, subDict in letterDict.items():
        print(f"Statistics for {key=}", end=" :")
        for subKey, subValue in subDict.items():
            print(f"{str(subKey)} = {str(subValue)}", end=" | ")
        print("")
    print("#################")

    sorLetDict = dict(sorted(letterDict.items(), key=lambda item: item[1]["count"], reverse=True))

    for letter, stats in sorLetDict.items():
        print(letter, end=": ")
        for key, value in stats.items():
            print(key, value, end=" = ")
        print("")

    frequencyTable = {}
    cnt = 0
    for key in sorLetDict:
        frequencyTable[key] = {}
        frequencyTable[key]["rank"] = cnt
        frequencyTable[key]["frequency"] = letterDict[key]["frequency"]
        cnt += 1
    for key in frequencyTable:
        print(key, frequencyTable[key])

    MAX = 0
    SHIFT = 0
    mulTable = []
    for shift in range(26):
        mul = 0
        for letter, indRank in zip(list(frequencyTable.keys()), list(letterData.keys())):
            mul += frequencyTable[letter]["frequency"] * letterData[(indRank + shift) % 26]["frequency"]
        mulTable.append([mul, shift])
        if MAX < mul:
            MAX = mul
            SHIFT = shift
    print(MAX, SHIFT)
    print(mulTable)
    if SHIFT != 0:
        break
    matches[mod] = {}
    for letter, indRank in zip(list(frequencyTable.keys()), list(letterData.keys())):
        matches[mod][letter] = letterData[indRank - SHIFT % 26]["letter"]
    for key in matches[mod].keys():
        print(key, matches[mod][key])
print(matches)
print(toDecrypt)

for mod in [0,1,2,3,4,5,6]:
    message[mod] = []
    for letter in toDecrypt[mod]:
        message[mod].append(matches[mod][letter])
finalMessage = ""

for i in range(452):
    for mod in [0,1,2,3,4,5,6]:
        for letter in toDecrypt[mod][i]:
            finalMessage += matches[mod][letter]
print(content)
print(finalMessage)
