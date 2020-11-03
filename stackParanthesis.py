string = "{({["
def parantMatch(string):
    openParanthesis = ["(", "{", "["]
    closeParanthesis = [")", "}", "]"]
    dictParanthesis = {")":"(", "}":"{", "]":"["}
    stack = []
    for i in string:
        #print(i in openParanthesis)
        if i in openParanthesis:
            stack.append(i)
            # print(stack)

        # else i == closeParanthesis:
        #     return False
        elif i in closeParanthesis:
                if stack == []:
                    return False
                lastElement = stack.pop()
                if dictParanthesis[i] != lastElement:
                    return False
    # print(stack == None)
    if stack == []:
        return True
    elif stack:
        return False

    #print(stack)
print(parantMatch(string))

    # if i == closeParanthesis:
    #     return False
