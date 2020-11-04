
arr = [91,4,64,78]
pieces = [[78],[4,64],[91]]

myDictionary = {x[0]:x for x in pieces}

arrCompare = []

for i in arr:
    arrCompare.extend(myDictionary.get(i, []))

return (arr == arrCompare)
