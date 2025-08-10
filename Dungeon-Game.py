class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:

        def solve(i,j,dp):

            if i==len(dungeon)-1 and j==len(dungeon[0])-1:
                return max(1,1-dungeon[i][j])

            if i>=len(dungeon) or j>=len(dungeon[0]):
                return float('inf')

            if dp[i][j]!=-1:
                return dp[i][j]
            
            right = solve(i,j+1,dp)-dungeon[i][j]
            down = solve(i+1,j,dp)-dungeon[i][j]

            dp[i][j] = max(1,min(right, down))
            return dp[i][j]

        dp = [[-1 for _ in range(len(dungeon[0]))] for _ in range(len(dungeon))]

        return solve(0,0,dp)
        