import itertools

# print(itertools.count())

input = 153232
# inputDigit = input // 10 + input % 10

def getDigit(number):
    if number < 10:
        print(number)
    remain = number // 10
    getDigit(remain)
    print(remain)

# getDigit(input)

def getDigitEfficientStack(number):
    myList = []
    while number:
        digit = number % 10
        number //= 10
        myList.append(digit)

    for i in myList:
        print(i)


getDigitEfficientStack(input)

def getDigitStack(number):
    myList = []
    while number > 10:
        dividend = number % 10
        myList.append(dividend)
        number = (number - dividend) // 10
    myList.append(number)

    while myList:
        print(myList.pop())
    return myList

def getDigitStackSum(number):
    myList = []
    sum = 0
    while number > 10:
        dividend = number % 10
        myList.append(dividend)
        number = (number - dividend) // 10
    myList.append(number)

    while myList:
        sum += myList.pop()
    return sum

# print(getDigitStackSum(input))


# print(inputDigit)
# perfectNumber = 10
# i = 1
# while i < perfectNumber:
#     counterpart = perfectNumber - i
#
#     if i == inputDigit:
#         print(i*10+counterpart)
#     i += 1
