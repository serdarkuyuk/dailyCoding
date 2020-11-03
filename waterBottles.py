numBottles = 9
numExchange = 3
myNumber = numBottles
while numBottles >= numExchange:

    exchangebleBottle = numBottles // numExchange
    myNumber += exchangebleBottle
    numBottles = exchangebleBottle + numBottles % numExchange

print(myNumber)
