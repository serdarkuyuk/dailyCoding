numBottles = 9
numExchange = 3
myNumber = numBottles
while numBottles >= numExchange:

    exchangebleBottle = numBottles // numExchange
    unchangebleBottle = numBottles % numExchange

    myNumber += exchangebleBottle

    numBottles = exchangebleBottle + unchangebleBottle
    # unchangebleBottle = numBottles



print(myNumber)
