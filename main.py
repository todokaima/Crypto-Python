#Vigenere
# 1 Read cipher
file = open(r'C:\Users\user\Desktop\Κ\Vigenere.txt' , 'r')
content = file.read()
file.close()
print(content)
# 2 Look to the right for matches
def searchPattern(string, sub_length, start, matchDict, gcdDict):
    k = start + 1
    while k + sub_length < len(string):
        substring = string[start:start + sub_length]
        if substring == string[k :k + sub_length]:
            if substring not in matchDict:
                matchDict[substring] = [start]
                gcdDict[substring] = []
            if k not in matchDict[substring]:
                matchDict[substring].append(k)
        k += 1
    for substring, positions in matchDict.items():
        gcdDict[substring] = [matchDict[substring][i+1] - matchDict[substring][i] for i in range(len(matchDict[substring])-1)]

gcdCalc = {}
matches = {}
for i in range(len(content)//2+1):
    for subLength in range(3, 20):
        searchPattern(content, subLength, i, matches, gcdCalc) #The same outside dict is being referenced in memory
print("\nMatches found in the text:")
for substring, positions in matches.items():
    print(f"Substring: '{substring}' -> Positions: {sorted(set(positions))}")
# 3 Finding the key length
import math
keyCount = {}
for subString, distances in gcdCalc.items():
    proposed = math.gcd(*distances)
    print(f"{subString=} found at intervals: {distances} proposed key = {proposed}")
    if proposed != 1 and proposed < 100 and proposed not in keyCount:
        keyCount[proposed] = 0
    if proposed in keyCount:
        keyCount[proposed] += 1
toBeDeleted = []
for key, frequency in keyCount.items():
    if frequency == 1 or key > 100:
        toBeDeleted.append(key)
for element in toBeDeleted:
    del keyCount[element]

for keylength, frequency in keyCount.items():
    print(f"{keylength=} encountered {frequency=} times")

