class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        def solve(i, j, dp):

            if i == m - 1 or j == n - 1:
                return 1

            if i >= m and j >= n:
                return 0

            if dp[i][j] != -1:
                return dp[i][j]

            right = solve(i + 1, j, dp)
            down = solve(i, j + 1, dp)

            dp[i][j] = right + down

            return dp[i][j]

        dp = [[-1] * n for _ in range(m)]
        return solve(0, 0, dp)
