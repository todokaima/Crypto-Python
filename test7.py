file = open(r'C:\Users\user\Desktop\Κ\Vigenere.txt' , 'r')
content = file.read()
print(content)
file.close()
miden = [content[i] for i in range(len(content)) if i%7 == 0]
ena = [content[i] for i in range(len(content)) if i%7 == 1]
duo = [content[i] for i in range(len(content)) if i%7 == 2]
tria = [content[i] for i in range(len(content)) if i%7 == 3]
tessera = [content[i] for i in range(len(content)) if i%7 == 4]
pente = [content[i] for i in range(len(content)) if i%7 == 5]
exi = [content[i] for i in range(len(content)) if i%7 == 6]
lista = [miden, ena, duo, tria, tessera, pente, exi]
print(lista)
dictL = {}
for i in range(len(lista)):
    dictL[i] = {}
    for element in lista[i]:
        if element not in dictL[i].keys():
            dictL[i][element] = 1
        if element in dictL[i].keys():
            dictL[i][element] += 1
    print(i,"==========")
    for letter,frequency in dictL[i].items():
        print(f"{letter=}, {round(frequency/len(miden),4)}")

newdict = {}
for i in range(len(lista)):
    newdict[i] = dict(sorted(dictL[i].items(), key = lambda item: item[1]))
fList = []

for i in range(len(lista)):
    fList.append([])
    print(i,"============================")
    for letter, frequency in newdict[i].items():
        print(f"{letter = }@{round(frequency/len(miden),4)}")
        fList[i].append((letter, round(frequency/452,5)))

print(fList[0])
replacement = ["E","T","A","O","I","N","S","R","H","D","L","U","C","M","F","Y","W","G","P","B","V","K","X","Q", "J","Z"]
replacement.reverse()
for i in range(len(fList)):
    for k in range(len(fList[i])):
        fList[i][k] = replacement[k]

print(fList)
frequency = []
for i in range(len(fList)):
    frequency.append(fList[i])
print(frequency)

"""string = ""
for item in newlista:
    print(len(item))
for k in range(452):
    for i in range(len(newlista[k])):
        string += newlista[i][k]
    string += "-"
print(content+"\n"+string)"""