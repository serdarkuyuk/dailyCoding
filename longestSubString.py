

string = 'afassdfasdfa'

start = maxLength = 0

mydict = {}

for i, c in enumerate(string):

    if c in mydict and start <= mydict[c]:
        start = mydict[c] + 1
    else:
        maxLength = max(maxLength, i-start+1)

    mydict[c] = i
    print(mydict)

print(maxLength, mydict )
