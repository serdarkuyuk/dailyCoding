matrix =   [['1','1','0','0'],['1','1','0','0'],['0','0','1','0'],['0','0','0','1']]

class Solution:

    def search(self, matrix):
        if not matrix:
            return 0

        count = 0
        rowLength = len(matrix)
        colLength = len(matrix[0])
        for row in range(rowLength):
            for col in range(colLength):
                if matrix[row][col] == '1':

                    count += 1
                    # print(matrix)
                    matrix = self.dfs(matrix, row, col)
                    # print(count)
        return count

    def dfs(self, matrix, row, col):
        rowLength = len(matrix)
        colLength = len(matrix[0])
        if row < 0 or col < 0 or row >= rowLength or col >= colLength or matrix[row][col] != '1':
            # print("1")
            return

        matrix[row][col] == '0'
        # print(matrix[row][col])

        self.dfs(matrix, row+1, col)
        self.dfs(matrix, row-1, col)
        self.dfs(matrix, row, col+1)
        self.dfs(matrix, row, col-1)

        return matrix



result = Solution()
print(result.search(matrix))
# result.search(matrix)
