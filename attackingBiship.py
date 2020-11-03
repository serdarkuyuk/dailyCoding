import pprint
from collections import defaultdict
m = 5
matrix = [[0 for i in range(m)] for k in range(m)]
pprint.pprint(matrix)
givenTuples = [(0,0), (1,2), (2,2), (4,0)]

for i in givenTuples:
    matrix[i[0]][i[1]] = 'b'
pprint.pprint(matrix)


# test = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
test = matrix

max_col = len(test[0])
max_row = len(test)
maxColRow = max_col + max_row
fdiag = defaultdict(list)
bdiag = defaultdict(list)

print(fdiag)
print(bdiag)

for col in range(max_col):
    for row in range(max_row):
        if col+row > 0 and col+row < maxColRow-2:

            fdiag[col+row].append(test[row][col])
        if abs(col-row) < maxColRow-1:

            bdiag[col-row].append(test[row][col])

        # fdiag[col+row].append(test[row][col])
        # bdiag[col-row-min_bdiag].append(test[row][col])

print(fdiag)
print(bdiag)
