class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        def solve(i, dp):

            if i>= len(cost):
                return 0

            if dp[i] !=-1:
                return dp[i]

            one = solve(i+1, dp)+cost[i]
            two = solve(i+2, dp)+cost[i]

            dp[i] = min(one, two)
            return dp[i]

        dp = [-1]*len(cost)

        return  min(solve(0,dp), solve(1,dp))
        