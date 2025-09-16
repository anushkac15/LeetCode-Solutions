class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        def solve(i, j, dp):


            if i >=m or j >=n :
                return float('inf')

            if i==m-1 and j==n-1:
                return grid[i][j]

            if dp[i][j]!=-1:
                return dp[i][j]

            right = grid[i][j]+solve(i+1, j, dp)
            down = solve(i, j+1, dp)+grid[i][j]

            dp[i][j] = min(right, down)
            return dp[i][j]

        m = len(grid)
        n = len(grid[0])
        dp = [[-1 for _ in range(n+1)] for _ in range(m+1)]

        return solve(0,0,dp)