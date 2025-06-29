class Solution:
    def climbStairs(self, n: int) -> int:

        def solve(n,dp):

            if n<0:
                return 0

            if n==0 or n==1:
                return 1

            if dp[n]!=-1:
                return dp[n]

            oneStep = solve(n-1,dp)
            twoStep = solve(n-2,dp)

            dp[n]= oneStep +twoStep 
            return dp[n]

        dp = [-1]*(n+1)
        return solve(n,dp)

        