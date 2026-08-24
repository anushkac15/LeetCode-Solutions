class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        def solve(i, j, dp):

            if i>=m or j>=n :
                return 0

            if obstacleGrid[i][j] ==1:
                return 0

            if i== m-1 and j ==n-1:
                return 1

            if dp[i][j] !=-1:
                return dp[i][j]

            right = solve(i+1, j, dp)
            down = solve(i, j+1, dp)

            dp[i][j] = right + down 

            return dp[i][j]

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        dp = [[-1 for _ in range(n+1)] for _ in range(m+1)]

        return solve(0,0, dp)