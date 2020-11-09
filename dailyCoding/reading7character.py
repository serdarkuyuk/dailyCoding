import inspect
def read2():

    with open("/Users/serdar/Documents/udel/python/dailyCoding/dailyCoding/random.txt","r") as file:
        string = file.read()
        # print(string)

    nameOfFile = inspect.stack()[0][3][-1]
    i = 0
    while i < len(string):
        yield string[i:i+int(nameOfFile)]
        i += int(nameOfFile)
    else:
        yield ""

generator = read2()

print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
