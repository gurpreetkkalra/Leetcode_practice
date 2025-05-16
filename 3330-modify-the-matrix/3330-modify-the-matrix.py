class Solution(object):
    def modifiedMatrix(self, matrix):
        m = len(matrix)
        n = len(matrix[0])

        colMax = []
        for j in range (n):
            maximum = matrix[0][j]
            for i in range (m):
                if matrix[i][j] > maximum:
                    maximum = matrix[i][j]
            colMax.append(maximum)
        for i in range (m):
            for j in range (n):
                if matrix[i][j] == -1:
                    matrix[i][j] = colMax[j]

        return matrix
            