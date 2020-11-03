import pprint
m = 5
n = 5

# matrix = [[0] * m] * n
#print(matrix)

def pathway(m, n):
    if m == 0 and n == 0:
        return 0
    if m == 0 or n == 0:
        return 1

    if matrix[m][n] != 0:
        print(matrix)
        return matrix[m][n]
    else:
        matrix[m][n] = pathway(m-1, n) + pathway(m, n-1)

    return matrix[m][n]

# matrix = [[0] * m] * n

def pathwayDynamic(m, n):

    matrix = [[0 for x in range(m)] for y in range(n)]
    # for i in range(1, n):
    #     matrix[0][i] = 1



    # for i in range(1,n):
    #     matrix[i][0] = 1
    matrix[0][1:] = [1] * (n-1)
    for i in range(1, m):
        matrix[i][0] = 1
    print(matrix)
    for i in range(1, m):
        for j in range(1, n):
            matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]
    pprint.pprint(matrix)



# print(pathway(m-1,n-1))
pathwayDynamic(m,n)
# mylist = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
# mylist[0][1:] = [1] * 2
# print(mylist)
