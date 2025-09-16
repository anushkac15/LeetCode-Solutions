class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        def solve(i,j, dp):

            if i>=m or j>=n :
                return 0

            if i==m-1 and j==n-1:
                return 1

            if dp[i][j]!=-1:
                return dp[i][j]

            right = solve(i+1, j, dp)
            down = solve(i, j+1, dp)

            dp[i][j] = right+down

            return dp[i][j]

        dp=[[-1 for _ in range(n+1)] for _ in range(m+1)]

        return solve(0,0, dp)