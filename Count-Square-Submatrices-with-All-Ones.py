class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        row, col = len(matrix), len(matrix[0])

        dp = [[-1] * col for _ in range(row)]

        def solve(i, j):
            if i >= row or j >= col:
                return 0

            if matrix[i][j] == 0:
                return 0

            if dp[i][j] != -1:
                return dp[i][j]

            down = solve(i + 1, j)
            right = solve(i, j + 1)
            diag = solve(i + 1, j + 1)

            dp[i][j] = 1 + min(down, right, diag)
            return dp[i][j]

        ans = 0
        for i in range(row):
            for j in range(col):
                ans += solve(i, j)

        return ans