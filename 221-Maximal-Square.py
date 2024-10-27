class Solution:
    def maximalSquare(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0

        row = len(matrix)
        column = len(matrix[0])
        max_side = 0

        t = [[0] * (column + 1) for _ in range(row + 1)]  

        for i in range(row):
            for j in range(column):
                if matrix[i][j] == '1': 
                    t[i + 1][j + 1] = min(t[i][j + 1], t[i + 1][j], t[i][j]) + 1
                    max_side = max(max_side, t[i + 1][j + 1])  

        return max_side * max_side  
