class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        if not matrix:
            return []

        rows, cols = len(matrix), len(matrix[0])

        zero_row = [False] * rows
        zero_col = [False] * cols

        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 0:
                    zero_row[row] = True 
                    zero_col[col] = True  

        for row in range(rows):
            for col in range(cols):
                if zero_row[row] or zero_col[col]:
                    matrix[row][col] = 0
