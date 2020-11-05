listm = [1,1,0,0,0,0,0,1,1,1]

'''listm = []
maxcount = count = i = 0
prev = None
while i < len(listm):
    if listm[i] == prev and listm[i] == 1:
        count += 1
    elif listm[i] != prev and listm[i] == 1:
        count = 1
        prev = listm[i]
    else:
        count = 0
    maxcount = max(maxcount, count)
    i += 1
print(maxcount)'''

maxcount = 0
count = 0
for i in listm:
    if i == 0:
        count = 0
    elif i == 1:
        count += 1
    maxcount = max(maxcount, count)

print(maxcount)
