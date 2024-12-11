# Vigenere
# 1 Read cipher
import math

file = open(r'C:\Users\user\Desktop\Κ\Vigenere.txt', 'r')
content = file.read()
file.close()
print(content)

def searchPattern(string, start, sub_length, matchDict):
    for k in range(start + 1, len(string) - sub_length + 1):
        substring = string[start:start + sub_length]
        if substring not in matchDict:
            matchDict[substring] = {"positions": [start], "gaps": [], "counter": 1}
        if string[k:k + sub_length] == substring:
            matchDict[substring]["positions"].append(k)
            matchDict[substring]["counter"] += 1

    # Remove substrings with only one occurrence
    toBeDeleted = [key for key, value in matchDict.items() if value["counter"] == 1]
    for key in toBeDeleted:
        del matchDict[key]
    for substring, data in matchDict.items():
        positions = data["positions"]
        data["gaps"] = [positions[i + 1] - positions[i] for i in range(len(positions) - 1)]
    toBeDeleted = []
    keys = list(matchDict.keys())  # Create a list of keys to iterate safely
    for item in keys:  # Iterate through the keys
        for key in keys:
            if key != item and key in item:  # Check if `key` is a substring of `item`
                if matchDict[key]["gaps"] == matchDict[item]["gaps"]:  # Compare gaps
                    toBeDeleted.append(key)  # Remove the smaller substring
    for key in toBeDeleted:
        del matchDict[key]
    for key in matchDict.keys():
        matchDict[key]["gcd"] = math.gcd(*matchDict[key]["gaps"])

matches = {}
for subLengths in range(3,6):
    for start in range(len(content) - subLengths + 1):
        searchPattern(content, start, subLengths, matches)

if matches:
    for key, dictionary in matches.items():
        print("\n" + key, end=" ")
        for item, value in dictionary.items():
            print(f"{item}: {value}", end=" ")
else:
    print("No matches found.")