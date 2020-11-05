#Not finished yet

# intervals = [[1,3],[2,6],[8,10],[15,18]]
# intervals = [[1,4],[4,5]]
intervals = [[2,3],[4,5],[6,7],[8,9],[1,10]]
intervals.sort(key = lambda it : it[0])
myList = [intervals[0]]

for i in range(1,len(intervals)):
    # print(myList)
    comp1i, comp1j = myList.pop()
    comp2i, comp2j = intervals[i]
    if comp2i > comp1j:
        myList.append([comp1i, comp1j])
        myList.append(intervals[i])
    elif comp2j < comp1i:
        myList.append([comp2i, comp2j])
        myList.append([comp1i, comp1j])
    else:
        if comp2i <= comp1i:
            first = comp2i
        else:
            first = comp1i

        if comp1j <= comp2j:
            end = comp2j
        else:
            end = comp1j

        if comp1j == comp2i:
            first = comp1i
            end = comp2j
        # myList.pop()
        myList.append([first, end])
print(myList)
