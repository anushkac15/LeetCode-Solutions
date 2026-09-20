class Solution:
    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:

        def solve(i, j):

            if dp[i][j] != -1:
                return dp[i][j]

            right = left = up = down = 0

            if i + 1 < len(matrix) and matrix[i + 1][j] > matrix[i][j]:
                right = solve(i + 1, j) + 1

            if i - 1 >= 0 and matrix[i - 1][j] > matrix[i][j]:
                left = solve(i - 1, j) + 1

            if j + 1 < len(matrix[0]) and matrix[i][j + 1] > matrix[i][j]:
                up = solve(i, j + 1) + 1

            if j - 1 >=0 and matrix[i][j - 1] > matrix[i][j]:
                down = solve(i, j - 1) + 1

            dp[i][j] = max(left, right, up, down)
            return dp[i][j]

        dp = [[-1] * len(matrix[0]) for _ in range(len(matrix))]

        res = 0

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                res = max(res, solve(i, j))

        return res + 1
