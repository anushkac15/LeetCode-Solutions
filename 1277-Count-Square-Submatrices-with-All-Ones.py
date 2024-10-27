class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:

        row = len(matrix)
        column = len(matrix[0])
        res =0

        t = [[0] * (column+1) for _ in range(row+1)]  

        for i in range(row):
            for j in range(column):

                if matrix[i][j]:
                    t[i+1][j+1] = min(t[i][j+1],t[i+1][j],t[i][j])+1

                res += t[i+1][j+1]
        
        return res
