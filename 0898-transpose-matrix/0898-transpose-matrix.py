class Solution(object):
    def transpose(self, matrix):
        m = len(matrix)
        n = len(matrix[0])

        transpose = []

        for j in range (n):
            newrow = []
            for i in range(m):
                newrow.append(matrix[i][j])
            transpose.append(newrow)

        return transpose
        